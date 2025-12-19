from fastapi import FastAPI, Query
from query import ask_question

app = FastAPI()

@app.get("/ask")
def ask(q: str = Query(..., min_length=3)):
    try:
        answer = ask_question(q)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
