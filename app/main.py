from fastapi import FastAPI
from settings import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "🧠 Allmighty GPT running",
        "env": settings.ENV,
        "engine": settings.PROMPT_ENGINE
    }
