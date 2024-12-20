# Asistente Conversacional de Recursos Humanos 🤖💼

Este proyecto tiene como objetivo desarrollar un **Asistente Conversacional** que responde consultas sobre recursos humanos utilizando datos en tiempo real obtenidos de la **API de LinkedIn**. El sistema implementa un enfoque de **Generación Aumentada por Recuperación (RAG)** utilizando **Cohere** y **FAISS** para mejorar la precisión y relevancia de las respuestas. 🌐

Este proyecto fue desarollado para poder aprender y aprobar el curso de IA y Desarrollo de Asistentes Conversacionales del Silicon Misiones con el Profesor Daniel Vallejos

![image](https://github.com/user-attachments/assets/c5e1937e-315a-4daf-a279-c77e11b5250d)

## Tecnologías y Herramientas Utilizadas 🛠️

- **LangChain**: Para la lógica de procesamiento de consultas e integración con Cohere (embeddings) y FAISS (motor de búsqueda semántica).
- **Streamlit**: Para crear una interfaz de usuario interactiva y amigable.
- **API de LinkedIn (RapidAPI)**: Para obtener datos en tiempo real sobre personas, empleos y empresas.
Suscribirse a el, es una API gratuita https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api - Hecho por RockApi
- **FAISS**: Para realizar búsquedas semánticas dentro de la base de conocimiento.

## Funcionalidades Clave 🚀

- **Generación Aumentada por Recuperación (RAG)** con **Cohere** y **FAISS**.
- Interfaz de usuario interactiva usando **Streamlit**.
- Búsqueda semántica eficiente mediante **FAISS**.
- **Gestión del historial de la conversación** a través de **st.session_state**.
- Integración con la **API de LinkedIn** para obtener datos en tiempo real sobre personas, trabajos y empresas.

## Proceso General 🔄

1. **Carga de Documentos**: Se cargan datos de la API de LinkedIn para alimentar la base de conocimiento.
2. **Creación de Embeddings**: Los documentos se convierten en embeddings con el modelo **Cohere**.
3. **Almacenamiento en FAISS**: Los embeddings se almacenan en la base de datos vectorial **FAISS** para permitir búsquedas rápidas.
4. **Consulta del Usuario**: La consulta del usuario se convierte en un embedding usando **Cohere**.
5. **Recuperación por Similitud**: El embedding de la consulta se compara con los embeddings en **FAISS**.
6. **Generación de Respuesta**: Se crea un prompt para generar una respuesta coherente usando el modelo de lenguaje **Cohere**.
7. **Interfaz de Usuario**: La respuesta se presenta al usuario mediante **Streamlit**.

## Modelos Utilizados 🧠

- **Embeddings**: `embed-multilingual-v3.0` de **Cohere**.
- **MML**: `command-xlarge-nightly` de **Cohere**.
- **API**: **RapidAPI** Real-Time LinkedIn Scraper API
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api
 (para integrar LinkedIn).


## Descripción del Código 👨‍💻

### Librerías Importadas:
- **streamlit**: Para la interfaz de usuario interactiva.
- **langchain_cohere**: Para trabajar con embeddings y el modelo de chat de **Cohere**.
- **requests**: Para interactuar con la API de **LinkedIn**.
- **dotenv**: Para gestionar las variables de entorno (como las claves API).
- **os y json**: Para la manipulación de datos y entorno.
- **time**: Para gestionar pausas entre solicitudes API si es necesario.

### Funciones Principales:
- **Interacción con la API de LinkedIn**: Funciones para buscar personas, trabajos y empresas.
- **Análisis de Intenciones (LangChain)**: Se analizan las intenciones de las consultas y se integran con el modelo de Cohere.
- **Manejo de Errores**: Función `safe_api_call()` que gestiona los posibles errores de la API de LinkedIn.
- **Base de Datos Vectorial (FAISS)**: Índices y busca resultados relevantes basados en la similitud semántica.

### Memoria y Gestión del Historial:
- Uso de **st.session_state** en **Streamlit** para almacenar el historial de la conversación.
- **InMemoryChatMessageHistory**: Gestión avanzada del historial con LangChain.

### Instalación 🔧
1_ Clona o descarga este repositorio:
git clone https://github.com/trobias/AsistenteIALinkedIn

2_ Crea tu Entorno Virtual con python -m venv venv desde la terminal.

3_ Desde la misma terminal entra a venv/Scripts y ejecuta activate, esto activará el entorno.

4_ Instala las dependencias:
pip install -r requirements.txt

5_ Configura las variables de entorno:
Crea un archivo .env en el directorio raíz del proyecto.
Añade las siguientes claves API:

Registrate en RAPIDAPI, suscribete gratis a la API: https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api y luego coloca tu apikey:
RAPIDAPI_KEY="tu_clave_api"

Registrate en COHERE y coloca tu APIKEY:
COHERE_API_KEY="tu_clave_api_de_Cohere"

6_ Ejecuta la aplicación:
streamlit run LinkedInIARAGTarnowski.py

y ya...

Archivos Principales 📂
LinkedInIARAGTarnowski.py: Archivo principal que gestiona la interfaz de usuario de Streamlit.
requirements.txt: Contiene todas las dependencias necesarias para ejecutar el proyecto.
env. Gestiona las configuraciones, incluidas las claves API.

Contribuciones 🤝
Si deseas contribuir a este proyecto, por favor, sigue estos pasos:
Fork este repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz un commit (git commit -am 'Añadir nueva funcionalidad').
Push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.

Licencia 📄
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

¡Gracias por usar este asistente conversacional! 😊 Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactarme. ¡Feliz programación! 💻

