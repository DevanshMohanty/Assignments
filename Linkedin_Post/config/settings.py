import os
from pathlib import Path
from dotenv import load_dotenv

# ALWAYS resolve project root
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"


# Force load
load_dotenv(dotenv_path=ENV_PATH, override=True)

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "groq/compound")

    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))
    VERBOSE = os.getenv("VERBOSE", "true").lower() == "true"

    DATA_DIR = BASE_DIR / "data"
    MEMORY_FILE = DATA_DIR / "memory_store.json"
    PROFILES_FILE = DATA_DIR / "user_profiles.json"

    @classmethod
    def validate(cls):
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY missing")
        cls.DATA_DIR.mkdir(exist_ok=True)

Settings.validate()
