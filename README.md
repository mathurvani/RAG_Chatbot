###  Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers user questions based on an eBay training/policy document.

The system uses semantic search to retrieve relevant information from the document and provides context-aware responses using a Large Language Model (LLM).

The objective is to ensure that answers are grounded in the provided document rather than relying solely on the model's general knowledge.

### Features
PDF document ingestion
Document chunking using LangChain
Semantic embeddings using HuggingFace Sentence Transformers
Vector storage using ChromaDB
Context retrieval using similarity search
Response generation using Mistral (via Ollama)
Streamlit-based chat interface
Source attribution for transparency and explainability

### Architecture
User Question --> Retriever (ChromaDB) --> Relevant Chunks --> Prompt Construction --> Mistral (Ollama) --> Generated Answer --> Answer + Retrieved Sources
### Preprocessing Pipeline
PDF Document
Text Extraction
Chunking
Embedding Generation
Chroma Vector Database

### Tech Stack
## Backend
Python
LangChain
ChromaDB
HuggingFace Embeddings
Ollama
Mistral LLM
## Frontend
Streamlit
### Development Environment
Google Colab (Data Processing & Vector Database Creation)
VS Code (Application Development)

### Project Structure
RAG_Chatbot/

├── app.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── retriever.py
│   ├── rag.py
│   └── prompt.py
│
└── vectordb/
### Implementation Details
1. Document Loading: The PDF document is loaded using LangChain's PDF loader.

2. Chunking: The document is split into smaller overlapping chunks using:
Chunk Size: 1000 characters
Chunk Overlap: 200 characters
This preserves context between chunks and improves retrieval quality.

3. Embeddings: Embeddings are generated using:

BAAI/bge-small-en-v1.5

This model converts text chunks into vector representations suitable for semantic similarity search.

4. Vector Database: ChromaDB is used to store document embeddings.

The vector database is persisted locally and reused during application execution, avoiding repeated embedding generation.

5. Retrieval: For every user query:

The query is embedded.
Top 3 most relevant chunks are retrieved.
Retrieved chunks are used as context for the LLM.
6. Response Generation: The retrieved context and user query are combined into a prompt and sent to the Mistral model running locally through Ollama.

The model generates responses grounded in the retrieved context.

### Installation
Clone Repository
git clone <repository-url>
cd RAG_Chatbot
Install Dependencies
pip install -r requirements.txt
Install Ollama

Download and install Ollama from:

https://ollama.com

Pull Mistral Model
ollama pull mistral
Running the Application

Start the Streamlit application:

python -m streamlit run app.py

The application will be available at:

http://localhost:8501
### Screenshots:

<img width="976" height="627" alt="Screenshot 2026-06-07 232749" src="https://github.com/user-attachments/assets/632ba78e-87ac-44f2-bb6b-66c2f8aced3f" />
<img width="1919" height="1067" alt="Screenshot 2026-06-07 232400" src="https://github.com/user-attachments/assets/9a7d5caa-d31c-4f54-8489-948a4963bc19" />

<img width="1911" height="1081" alt="Screenshot 2026-06-07 232414" src="https://github.com/user-attachments/assets/70209a10-8d9d-4bc1-b56c-d2ecd9d05bbf" />

<img width="1900" height="596" alt="Screenshot 2026-06-07 232423" src="https://github.com/user-attachments/assets/8c8bcc08-8d22-4b9e-aec1-7098afa98b34" />
<img width="627" height="768" alt="Screenshot 2026-06-07 232620" src="https://github.com/user-attachments/assets/5f802ebf-f414-442c-87d2-e0b23e6e1481" />
<img width="616" height="389" alt="Screenshot 2026-06-07 232708" src="https://github.com/user-attachments/assets/1d8a4ee4-1e5a-4e35-b83c-d9d252103237" />
