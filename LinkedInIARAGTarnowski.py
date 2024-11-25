import streamlit as st
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import HumanMessage, AIMessage
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import requests
import os
import json
import time

# %% Cargar variables de entorno
load_dotenv()

# %% Configurar claves API
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
BASE_URL = "https://linkedin-data-api.p.rapidapi.com"

# %% Configurar Cohere y embeddings
cohere = ChatCohere(model="command-xlarge-nightly", api_key=COHERE_API_KEY, temperature=0.7)
embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
    "Accept": "application/json"
}

def create_chain(question):
    """Crea una cadena LangChain para interpretar la consulta del usuario."""
    template = """
    Actúas como un asistente de recursos humanos especializado en interpretar consultas en lenguaje natural.
    Dado el texto de entrada, interpreta la intención del usuario para determinar qué tipo de búsqueda desea realizar.

    Si la consulta está relacionada con buscar personas, empleados, desarrolladores o similares en ese momento, diras "Intención: Personas".

    Si la consulta se refiere a trabajos, empleos, ofertas laborales o similares en ese momento, diras "Intención: Trabajos".

    Si la consulta no se ajusta a ninguno de los casos anteriores, responderás con un mensaje genérico.
    Si la consulta pide de alguna forma explicar que hacer, responderás con un mensaje de ayuda.
    Respeta parametros como Ubicacion o Localización, Habilidades, Experiencia, etc.
    No interpretes saludos o preguntas como búsquedas.
    Entrada del usuario:
    {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    output_parser = StrOutputParser()
    chain = prompt | cohere | output_parser
    return chain.invoke({"question": question})

def search_people(**kwargs):
    """Realiza una búsqueda de personas utilizando los filtros proporcionados."""
    params = {k: v for k, v in kwargs.items() if v is not None}
    return safe_api_call(f"{BASE_URL}/search-people", params)

def search_jobs(**kwargs):
    """Realiza una búsqueda de trabajos utilizando los filtros proporcionados."""
    params = {k: v for k, v in kwargs.items() if v is not None}
    return safe_api_call(f"{BASE_URL}/search-jobs-v2", params)

def safe_api_call(url, params, max_retries=3, wait_time=2):
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()  # Genera excepción para códigos de error HTTP
    return response.json()


def sort_with_langchain_faiss(response_json, key="name"):

    # Extraer los textos que se desean ordenar
    items = response_json.get("items", [])
    texts = [item.get(key, "") for item in items]

    # Verificar si hay datos válidos
    if not texts:
        return items  # Si no hay textos, regresar la lista original sin cambios

    # Crear el índice FAISS utilizando los textos
    faiss_store = FAISS.from_texts(texts, embeddings)

    # Consultar para obtener los textos en orden de similitud
    # Usamos un texto representativo para buscar ("clave genérica")
    query = "orden semántico"
    search_results = faiss_store.similarity_search(query, k=len(texts))

    # Ordenar los elementos originales según los resultados de FAISS
    sorted_items = [items[texts.index(result.metadata["text"])] for result in search_results]

    return sorted_items


def process_response_with_langchain_faiss(response):
    """
    Procesa la respuesta JSON y devuelve un JSON string ordenado con FAISS de LangChain.
    """
    sorted_response = sort_with_langchain_faiss(response)
    return json.dumps(sorted_response, indent=2)


def display_help():
    """Muestra un tutorial sobre qué buscar y cómo especificar parámetros relevantes."""
    st.markdown("""
    ### ¿Qué puedes buscar aquí?
    - **Personas**: Busca por palabras clave, nombre, ubicación o experiencia.
      - Ejemplo: "Busca un Senior Developer con 5 años de experiencia en Python"
    - **Trabajos**: Especifica títulos, ubicación y experiencia deseada.
      - Ejemplo: "Busca un Trabajo remoto en desarrollo de software con salario > 60k"
    """)

def initialize_chat():
    """Inicializa los mensajes en la sesión."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def update_chat_history(chat_history):
    """Actualiza el historial de mensajes desde chat_history a session_state."""
    for message in chat_history.messages:
        role = "user" if isinstance(message, HumanMessage) else "assistant"
        if {"role": role, "content": message.content} not in st.session_state.messages:
            st.session_state.messages.append({"role": role, "content": message.content})

def display_messages():
    """Muestra los mensajes almacenados en session_state."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def main():
    st.title("Asistente de LinkedIn")

    initialize_chat()

    if st.button("Cerrar sesión"):
        st.session_state.clear()
        st.rerun()

    if "session_id" not in st.session_state:
        st.session_state.session_id = f"session_{len(st.session_state)}"
    session_id = st.session_state.session_id

    if "store" not in st.session_state:
        st.session_state.store = {}

    def get_session_history(session_id: str):
        """Obtiene o inicializa el historial de mensajes de la sesión actual."""
        if session_id not in st.session_state.store:
            st.session_state.store[session_id] = InMemoryChatMessageHistory()
        return st.session_state.store[session_id]

    chat_history = get_session_history(session_id)

    update_chat_history(chat_history)

    display_messages()

    if user_input := st.chat_input("Escribe tu consulta (Escribe 'ayuda' o 'que hacer' para recibir ayuda):"):
        chat_history.add_user_message(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Procesando..."):

                    action = create_chain(user_input)
                    st.write(action)  # Mostrar input

                # Ayuda o consulta
                    if "ayuda" in user_input.lower() or "que hacer" in user_input.lower():
                        display_help()

                    if "Intención: Personas" in action:
                        response = search_people(keywords=user_input)
                    elif "Intención: Trabajos" in action:
                        response = search_jobs(keywords=user_input)



            # Si se ejecutó una de las funciones, procesar la respuesta en formato JSON
            if response:
                response_text = json.dumps(response, indent=2)
                st.json(response)  # Mejor visualización del JSON
                chat_history.add_ai_message(response_text)  # Añadir al historial
                st.session_state["messages"].append({"role": "assistant", "content": response_text})  # Mostrar en el chat
 

if __name__ == "__main__":
    main()


