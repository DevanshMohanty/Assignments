from langchain_groq import ChatGroq
from config import Settings

def get_llm():
    return ChatGroq(
        api_key=Settings.GROQ_API_KEY,
        model=Settings.GROQ_MODEL,
        temperature=Settings.TEMPERATURE,
        max_tokens=Settings.MAX_TOKENS,
        verbose=Settings.VERBOSE
    )
