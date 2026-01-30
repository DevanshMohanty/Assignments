from config import Settings
from utils.file_handler import load_json, save_json

MAX_MEMORY_MESSAGES = 10

# Separate log file to store full history for inspection
MEMORY_LOG_FILE = Settings.DATA_DIR / "memory_log.json"

def load_memory() -> list:
    """
    Load the main memory used for generating prompts.
    Returns a list of messages.
    """
    return load_json(Settings.MEMORY_FILE)

def save_message(role: str, content: str):
    """
    Save a single message to memory and also update memory log.
    """
    #Load current memory
    memory = load_memory()

    #Append new message
    memory.append({"role": role, "content": content})

    #Keep only last MAX_MEMORY_MESSAGES for prompt context
    memory_to_save = memory[-MAX_MEMORY_MESSAGES:]

    #Save limited memory back to main memory_store.json
    save_json(Settings.MEMORY_FILE, memory_to_save)

    #Save full memory to log for inspection
    save_json(MEMORY_LOG_FILE, memory)

def format_memory_for_prompt(memory: list) -> str:
    """
    Convert memory into a string suitable for prompt injection.
    Only the last 10 messages are used for context.
    """
    lines = []
    for msg in memory[-10:]:
        prefix = "User" if msg["role"] == "user" else "Assistant"
        lines.append(f"{prefix}: {msg['content']}")
    return "\n".join(lines)
