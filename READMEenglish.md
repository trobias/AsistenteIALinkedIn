
# Human Resources Conversational Assistant 🤖💼

This project aims to develop a **Conversational Assistant** that answers HR-related queries using real-time data obtained from the **LinkedIn API**. The system implements a **Retrieval-Augmented Generation (RAG)** approach using **Cohere** and **FAISS** to improve the accuracy and relevance of responses. 🌐

This project was developed to learn and pass the AI and Conversational Assistant Development course at Silicon Misiones with Professor Daniel Vallejos.

![image](https://github.com/user-attachments/assets/c5e1937e-315a-4daf-a279-c77e11b5250d)

## Technologies and Tools Used 🛠️

- **LangChain**: For query processing logic and integration with Cohere (embeddings) and FAISS (semantic search engine).
- **Streamlit**: For creating an interactive and user-friendly interface.
- **LinkedIn API (RapidAPI)**: For obtaining real-time data on people, jobs, and companies.
  Subscribe to it, it’s a free API [https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api) - Made by RockApi
- **FAISS**: For performing semantic searches within the knowledge base.

## Key Features 🚀

- **Retrieval-Augmented Generation (RAG)** with **Cohere** and **FAISS**.
- Interactive user interface using **Streamlit**.
- Efficient semantic search via **FAISS**.
- **Conversation history management** through **st.session_state**.
- Integration with the **LinkedIn API** to get real-time data on people, jobs, and companies.

## General Process 🔄

1. **Document Loading**: Data is loaded from the LinkedIn API to feed the knowledge base.
2. **Embedding Creation**: The documents are converted into embeddings using the **Cohere** model.
3. **Storage in FAISS**: The embeddings are stored in the **FAISS** vector database to allow fast searches.
4. **User Query**: The user's query is converted into an embedding using **Cohere**.
5. **Similarity Retrieval**: The query embedding is compared with the embeddings in **FAISS**.
6. **Response Generation**: A prompt is created to generate a coherent response using the **Cohere** language model.
7. **User Interface**: The response is presented to the user via **Streamlit**.

## Models Used 🧠

- **Embeddings**: `embed-multilingual-v3.0` from **Cohere**.
- **MML**: `command-xlarge-nightly` from **Cohere**.
- **API**: **RapidAPI** Real-Time LinkedIn Scraper API [https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api) (for integrating LinkedIn).

## Code Description 👨‍💻

### Imported Libraries:
- **streamlit**: For the interactive user interface.
- **langchain_cohere**: For working with embeddings and the **Cohere** chat model.
- **requests**: To interact with the **LinkedIn** API.
- **dotenv**: For managing environment variables (such as API keys).
- **os and json**: For data and environment manipulation.

### Main Functions:
- **Interaction with the LinkedIn API**: Functions to search for people, jobs, and companies.
- **Intent Analysis (LangChain)**: Analyzing the intents of the queries and integrating them with the Cohere model.
- **Error Handling**: `safe_api_call()` function that handles possible errors from the LinkedIn API.
- **Vector Database (FAISS)**: Indexes and searches for relevant results based on semantic similarity.

### Memory and Conversation History Management:
- Using **st.session_state** in **Streamlit** to store the conversation history.
- **InMemoryChatMessageHistory**: Advanced history management with LangChain.

## Installation 🔧

Clone this repository:
```bash
git clone https://github.com/trobias/AsistenteIALinkedIn
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Set up the environment variables:
- Create a `.env` file in the root directory of the project.
- Add the following API keys:
  - Register on **RAPIDAPI**, subscribe for free to the API: [https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api) and place your API key:
  ```bash
  RAPIDAPI_KEY="your_api_key"
  ```
  - Register on **COHERE** and place your API key:
  ```bash
  COHERE_API_KEY="your_cohere_api_key"
  ```

Run the application:
```bash
streamlit run LinkedInIARAGTarnowski.py
```

And you're ready to go!

## Main Files 📂
- **LinkedInIARAGTarnowski.py**: The main file managing the Streamlit user interface.
- **requirements.txt**: Contains all the dependencies needed to run the project.
- **.env**: Manages configurations, including the API keys.

## Contributions 🤝

If you'd like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License 📄
This project is licensed under the MIT License. For more details, please refer to the LICENSE file.

Thank you for using this conversational assistant! 😊 If you have any questions or suggestions, feel free to open an issue or contact me. Happy coding! 💻

--- 

Let me know if you need anything else!
