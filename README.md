![image](https://github.com/user-attachments/assets/1fd8475b-b2f3-4dc2-b573-8deed7d3282b)
# talk2pdf 🤖📄🧑‍🦰 [(Video Demo)](https://drive.google.com/file/d/1RvOhgdOeO08amTxghtTgWjwU_Py7VxUu/view?usp=sharing)
### A chatbot that can talk to PDF built using Langchain, Pinecone, Streamlit, LLama3.2. It enables users to ask questions about the content of three PDF documents and receive relevant, context-aware answers.

# Features
 - Processes and embeds content from multiple PDFs.
 - Retrieves relevant context from Pinecone for user queries.
 - Generates accurate responses using LLama3.2.
 - Interactive Streamlit chat interface.

### Screenshot   
![screencapture-localhost-8501-2024-11-30-12_05_02](https://github.com/user-attachments/assets/c788a102-941e-4b10-989a-ceb03ffbe633)

# Setup
### 1. Clone the Repository
```
git clone https://github.com/namankedia101/talk2pdf.git
```

### 2. Install Dependencies
```
pip install langchain langchain_pinecone langchain_community pinecone sentence-transformers pypdf streamlit
```

### 3. Configure Environment Variables
Create a .env file with your Pinecone API key:
```
PINECONE_API_KEY=your_pinecone_api_key
```

### 4. Initialize Pinecone#
Run the script to create the Pinecone index:
```
python create_index.py
```

### 6. Run the Chatbot
Start the Streamlit app:
```
streamlit run streamlit.py
```

# File Descriptions
 - streamlit.py: Chatbot interface and response generation.
 - ingest_data.py: Processes PDFs and stores embeddings in Pinecone.
 - create_index.py: Creates and initializes the Pinecone index.
 - retriever.py: Handles similarity search from Pinecone.

# Components Used
### 1. Vector Database
 - Pinecone is used to store and retrieve vector embeddings generated from PDF content.
Index Name: alemeno-assignment.
### 2. Embedding Model
 - Model: all-MiniLM-L6-v2 from Sentence Transformers.
### 3. Text Splitting
 - Method: RecursiveCharacterTextSplitter
 - Chunk Size: 1000 characters
 - Overlap: 100 characters
### 4. Language Model
 - Model: LLama3.2
 - Framework: Langchain
### 5. Frontend
 - Framework: Streamlit
 - UI: Interactive chat interface with context toggle for debugging.
