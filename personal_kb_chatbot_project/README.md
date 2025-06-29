# 📝 Personal Knowledge Base Chatbot

Upload PDFs, store their embeddings in Chroma, and query them via FastAPI.

## Features
- Upload PDFs -> extract text -> store embeddings
- Query with natural language to retrieve top matching snippets

## Run locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
uvicorn app.main:app --reload
```

## Example
```bash
curl -X POST /upload_pdf -F "file=@mydoc.pdf"
curl -X POST /ask -H "Content-Type: application/json" -d '{"question":"What did the document say about pricing?"}'
```