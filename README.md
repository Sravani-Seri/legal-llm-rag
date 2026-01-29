# 📘 Legal Document Q&A System using LLMs (RAG)

## 🔍 Overview
This project implements a Retrieval-Augmented Generation (RAG) system that enables users to ask natural language questions over legal and policy documents and receive accurate, context-aware answers powered by Large Language Models (LLMs).

The system focuses on production-oriented AI engineering, including dataset preparation, embeddings, API-based model integration, evaluation, and deployment-ready architecture — aligning with real-world AI applications in legal technology.

## 🎯 Key Features
- Ingests and processes legal or regulatory documents (PDF / TXT)
- Splits documents into semantic chunks for efficient retrieval
- Generates vector embeddings and stores them in a vector database
- Performs similarity-based search to retrieve relevant context
- Uses an LLM to generate grounded answers based on retrieved content
- Exposes functionality through a REST API
- Includes basic evaluation metrics to assess response quality

## 🧠 Architecture
User Query  
↓  
API (FastAPI)  
↓  
Embedding Model (OpenAI)  
↓  
Vector Store (FAISS / Chroma)  
↓  
Context Retrieval  
↓  
LLM Answer Generation  
↓  
Response with Source References  

## 🛠️ Tech Stack
- Language: Python
- LLM Provider: OpenAI API
- Framework: FastAPI
- Vector Database: FAISS / Chroma
- Embeddings: OpenAI Embeddings
- Data Processing: LangChain
- Evaluation: Custom relevance & latency metrics
- Deployment: Docker
- Cloud Ready: AWS-compatible

## 📂 Project Structure

