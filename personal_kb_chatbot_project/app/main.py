from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from .ingest import ingest_pdf
from .query import query_knowledge_base
import os, uuid

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class QueryInput(BaseModel):
    question: str

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4()) + "_" + file.filename
    path = os.path.join(UPLOAD_FOLDER, file_id)
    with open(path, "wb") as f:
        f.write(await file.read())
    ingest_pdf(path)
    return {"msg": "PDF ingested", "file": file.filename}

@app.post("/ask")
def ask_question(data: QueryInput):
    docs = query_knowledge_base(data.question)
    return {"matches": docs}