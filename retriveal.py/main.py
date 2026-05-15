from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from retrieval import search

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):

    last_message = req.messages[-1].content

    if len(last_message.split()) < 3:

        return {
            "reply": "Please provide role and skills required.",
            "recommendations": [],
            "end_of_conversation": False
        }

    results = search(last_message)

    recommendations = []

    for r in results:

        recommendations.append({
            "name": r["name"],
            "url": r["url"],
            "test_type": r["test_type"]
        })

    return {
        "reply": "Here are recommended SHL assessments.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }