from config import Settings
from utils.file_handler import save_json

def clear_memory():
    """
    Clears the memory_store.json and memory_log.json files.
    """
    # Clear main memory
    save_json(Settings.MEMORY_FILE, [])

    # Clear full memory log
    log_file = Settings.DATA_DIR / "memory_log.json"
    save_json(log_file, [])

    print("All memory cleared. You can start fresh now.")

if __name__ == "__main__":
    clear_memory()
