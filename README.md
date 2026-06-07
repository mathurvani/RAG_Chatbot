###  Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers user questions based on an eBay training/policy document.

The system uses semantic search to retrieve relevant information from the document and provides context-aware responses using a Large Language Model (LLM).

The objective is to ensure that answers are grounded in the provided document rather than relying solely on the model's general knowledge.

Features
PDF document ingestion
Document chunking using LangChain
Semantic embeddings using HuggingFace Sentence Transformers
Vector storage using ChromaDB
Context retrieval using similarity search
Response generation using Mistral (via Ollama)
Streamlit-based chat interface
Source attribution for transparency and explainability
Architecture
User Question
      │
      ▼
Retriever (ChromaDB)
      │
      ▼
Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Mistral (Ollama)
      │
      ▼
Generated Answer
      │
      ▼
Answer + Retrieved Sources
Preprocessing Pipeline
PDF Document
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Chroma Vector Database
Tech Stack
Backend
Python
LangChain
ChromaDB
HuggingFace Embeddings
Ollama
Mistral LLM
Frontend
Streamlit
Development Environment
Google Colab (Data Processing & Vector Database Creation)
VS Code (Application Development)
Project Structure
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
Implementation Details
1. Document Loading

The PDF document is loaded using LangChain's PDF loader.

2. Chunking

The document is split into smaller overlapping chunks using:

Chunk Size: 1000 characters
Chunk Overlap: 200 characters

This preserves context between chunks and improves retrieval quality.

3. Embeddings

Embeddings are generated using:

BAAI/bge-small-en-v1.5

This model converts text chunks into vector representations suitable for semantic similarity search.

4. Vector Database

ChromaDB is used to store document embeddings.

The vector database is persisted locally and reused during application execution, avoiding repeated embedding generation.

5. Retrieval

For every user query:

The query is embedded.
Top 3 most relevant chunks are retrieved.
Retrieved chunks are used as context for the LLM.
6. Response Generation

The retrieved context and user query are combined into a prompt and sent to the Mistral model running locally through Ollama.

The model generates responses grounded in the retrieved context.

Installation
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
