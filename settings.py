import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENV = os.getenv("ENV", "dev")
    PROMPT_ENGINE = os.getenv("PROMPT_ENGINE", "allmighty")
    USE_FALLBACKS = os.getenv("USE_FALLBACKS", "false").lower() == "true"
    DEPLOY_REGION = os.getenv("DEPLOY_REGION", "eu-west-1")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
    AGENT_MODE = os.getenv("AGENT_MODE", "manual")
    WORKSPACE_DIR = os.getenv("WORKSPACE_DIR", "/workspace/Allmighty")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROK_API_TOKEN = os.getenv("GROK_API_TOKEN")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GROQ_API_TOKEN = os.getenv("GROQ_API_TOKEN")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    REDIS_SECRET = os.getenv("REDIS_SECRET")
    RENDER_DEPLOY_HOOK = os.getenv("RENDER_DEPLOY_HOOK")

settings = Settings()
