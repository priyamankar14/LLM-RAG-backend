# LLM-RAG Backend (Django + FAISS + Ollama)

## Overview

This project implements a **Retrieval-Augmented Generation (RAG) backend system** using **Django**, **FAISS**, and **Ollama LLM**.

The system retrieves relevant information from a document dataset and generates accurate answers using a **local Large Language Model (LLM)**.

Instead of relying only on the LLM’s internal knowledge, the system first **retrieves relevant documents using vector search** and then provides them as **context to the model**, improving answer quality and factual accuracy.

---

## System Architecture

User Query
↓
Django Backend API
↓
Query Embedding Generation
↓
FAISS Vector Similarity Search
↓
Retrieve Relevant Documents
↓
Send Context to LLM (Ollama)
↓
Generated Answer

---

## Features

* Retrieval Augmented Generation (RAG)
* Context-aware LLM responses
* FAISS vector similarity search
* Document embedding pipeline
* Local LLM inference using Ollama
* Django backend API
* Scalable architecture for large document datasets
* Modular pipeline for retrieval and generation

---

## Tech Stack

### Backend

* Python
* Django

### Machine Learning

* Sentence Transformers
* FAISS (Vector Database)

### LLM

* Ollama
* Phi model

### Other Tools

* Git
* REST APIs

---

## Project Structure

```
LLM-RAG-backend
│
├── config
│   ├── settings.py
│   ├── urls.py
│
├── django_rag
│   ├── rag
│   │   ├── embeddings.py
│   │   ├── generator.py
│   │   ├── llm.py
│   │   ├── faiss_index.py
│   │   ├── load_docs.py
│   │
│   ├── views.py
│   ├── models.py
│
├── .gitignore
└── README.md
```

---

## Dataset

The dataset used for this project is **too large to be stored on GitHub**, so it is hosted separately.

Download the dataset from the link below:

DATASET LINK:
https://www.kaggle.com/datasets/ffatty/plain-text-wikipedia-simpleenglish

After downloading the dataset, place it inside the project directory:

```
archive/
```

This folder is ignored by `.gitignore`, so it will not be uploaded to GitHub.

---

## Installation

Clone the repository:

```
git clone https://github.com/priyamankar14/LLM-RAG-backend.git
```

Move into the project directory:

```
cd LLM-RAG-backend
```

Create a virtual environment:

```
python -m venv venv
```

Activate virtual environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Project

Start the Ollama model:

```
ollama run phi
```

Run the Django server:

```
python manage.py runserver
```

The backend API will run at:

```
http://127.0.0.1:8000
```

---

## How the RAG Pipeline Works

1. User submits a query
2. The query is converted into an embedding
3. FAISS performs vector similarity search
4. Most relevant documents are retrieved
5. Retrieved context is sent to the LLM
6. The LLM generates the final response

This process improves the **accuracy and relevance of generated answers**.

---

## Example Workflow

Example user question:

```
What topics are discussed in the dataset?
```

The system will:

* Convert the question into an embedding
* Retrieve relevant documents using FAISS
* Provide context to the LLM
* Generate a contextual response

---

## Future Improvements

* Docker containerization
* Support for multiple LLM models
* Streaming responses from LLM
* Deployment on cloud infrastructure

---

## Author

Priya Mankar
B.Tech Computer Science Engineering

---

## License

This project is intended for **educational and research purposes**.
