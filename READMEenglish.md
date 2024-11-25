# HR Conversational Assistant 🤖💼

This project aims to develop a **Conversational Assistant** that responds to HR-related queries using real-time data fetched from the **LinkedIn API**. The system implements a **Retrieval-Augmented Generation (RAG)** approach using **Cohere** and **FAISS** to enhance response accuracy and relevance. 🌐

## Technologies and Tools Used 🛠️

- **LangChain**: For query processing logic and integration with Cohere (embeddings) and FAISS (semantic search engine).
- **Streamlit**: To create an interactive and user-friendly interface.
- **LinkedIn API (RapidAPI)**: To fetch real-time data about people, jobs, and companies.
- **FAISS**: For performing semantic searches in the knowledge base.

## Key Features 🚀

- **Retrieval-Augmented Generation (RAG)** with **Cohere** and **FAISS**.
- Interactive user interface built with **Streamlit**.
- Efficient semantic search using **FAISS**.
- **Conversation history management** with **st.session_state**.
- Integration with the **LinkedIn API** to fetch real-time data about people, jobs, and companies.

## General Process 🔄

1. **Document Loading**: Data from the LinkedIn API is loaded to populate the knowledge base.
2. **Embedding Creation**: Documents are converted into embeddings using **Cohere**.
3. **FAISS Storage**: Embeddings are stored in the **FAISS** vector database for fast retrieval.
4. **User Query**: The user’s query is converted into an embedding using **Cohere**.
5. **Similarity Retrieval**: The query embedding is compared with the stored embeddings in **FAISS**.
6. **Response Generation**: A prompt is created to generate a coherent response using the **Cohere** language model.
7. **User Interface**: The response is displayed to the user through **Streamlit**.

## Models Used 🧠

- **Embeddings**: `embed-multilingual-v3.0` by **Cohere**.
- **MML**: `command-xlarge-nightly` by **Cohere**.
- **API**: **RapidAPI** (for LinkedIn integration).

## Code Overview 👨‍💻

### Imported Libraries:
- **streamlit**: For building the interactive user interface.
- **langchain_cohere**: To work with embeddings and the **Cohere** chat model.
- **requests**: For interacting with the **LinkedIn API**.
- **dotenv**: For managing environment variables (e.g., API keys).
- **os and json**: For data and environment handling.
- **time**: To manage pauses between API requests if necessary.

### Main Functions:
- **LinkedIn API Interaction**: Functions to search for people, jobs, and companies.
- **Intent Analysis (LangChain)**: Processes user queries and integrates with the Cohere model for analysis.
- **Error Handling**: `safe_api_call()` function manages potential errors from the LinkedIn API.
- **Vector Database (FAISS)**: Indexes and retrieves semantically relevant results based on user queries.

### Memory and History Management:
- **st.session_state** in **Streamlit**: Used to store conversation history.
- **InMemoryChatMessageHistory**: Advanced history management with LangChain.

## Requirements 🚧

Make sure to install all dependencies with the following command:

```bash
pip install -r requirements.txt

Installation 🔧
Clone this repository:
git clone https://github.com/your-username/hr-assistant.git

Install the dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py

Main Files 📂
app.py: Main file managing the Streamlit user interface.
requirements.txt: Contains all dependencies needed for the project.
env. Manages configurations, including API keys.

Contributions 🤝
If you want to contribute to this project, please follow these steps:

Fork this repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a Pull Request.

License 📄
This project is licensed under the MIT License. For more details, see the LICENSE file.

Thank you for using this conversational assistant! 😊 If you have any questions or suggestions, feel free to open an issue or reach out. Happy coding! 💻
