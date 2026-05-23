from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import ask_question

app=FastAPI()

class Query(BaseModel):
    question:str

@app.post("/chat")

def chat(query:Query):

    result=ask_question(
        query.question
    )

    return result


if __name__=="__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
