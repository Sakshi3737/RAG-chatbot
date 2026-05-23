# RAG Chatbot using LangChain, FAISS, OCR and FastAPI

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that can answer questions from PDF documents.

The system performs:

- PDF ingestion
- OCR for scanned PDFs
- Text chunking
- Embedding generation
- Vector database creation using FAISS
- Retrieval of relevant content
- Response generation using an LLM
- Source citations with page numbers
- FastAPI interface for interaction

---

## Features

✔ Supports multiple PDF files  
✔ OCR support for scanned documents  
✔ Semantic search using embeddings  
✔ FAISS vector database  
✔ Context-based answer generation  
✔ Source and page citations  
✔ REST API support using FastAPI  

---

## Technologies Used

- Python
- LangChain
- FAISS
- Sentence Transformers
- Hugging Face Transformers
- PyMuPDF
- Tesseract OCR
- FastAPI
- Uvicorn

---

## Project Structure

```text
rag-chatbot/
│
├── app.py
├── ingest.py
├── chatbot.py
├── requirements.txt
├── README.md
│
├── pdfs/
│ ├── ML_Basics.pdf
│ ├── DeepLearning.pdf
│
└── vector_store/
    ├── index.faiss
    └── index.pkl
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install pymupdf
pip install sentence-transformers
pip install transformers
pip install torch
pip install langchain
pip install langchain-community
pip install langchain-huggingface
pip install faiss-cpu
pip install pytesseract
pip install pillow
pip install fastapi
pip install uvicorn
```

Or install all packages together:

```bash
pip install pymupdf sentence-transformers transformers torch langchain langchain-community langchain-huggingface faiss-cpu pytesseract pillow fastapi uvicorn
```

---

## Add PDF Documents

Place all PDF files inside:

```text
pdfs/
```

Example:

```text
pdfs/
├── ML_Basics.pdf
├── DeepLearning.pdf
```

---

## Generate Vector Database

Run:

```bash
python ingest.py
```

Expected output:

```text
Total chunks created: 2458
PDF ingestion complete
Vector database saved successfully
```

Generated files:

```text
vector_store/
├── index.faiss
├── index.pkl
```

---

## Run Application

Start FastAPI server:

```bash
python app.py
```

Server runs at:

```text
http://localhost:8000
```

---

## API Endpoint

### POST Request

```text
POST /chat
```

Request body:

```json
{
    "question":"What is machine learning?"
}
```

Example response:

```json
{
    "answer":"Machine learning is a field of AI that enables systems to learn patterns from data.",
    "sources":[
        "ML_Basics.pdf Page:12",
        "DeepLearning.pdf Page:45"
    ]
}
```

---

## Workflow

1. Load PDF documents
2. Extract text using PyMuPDF
3. Apply OCR if document is scanned
4. Split text into chunks
5. Generate embeddings
6. Store vectors in FAISS
7. Retrieve relevant chunks
8. Generate response
9. Return answer with sources

---

## Future Improvements

- Add chat history memory
- Streamlit UI
- Support for DOCX and TXT files
- Use larger LLM models
- Deploy using Docker


Sakshi Gholap
