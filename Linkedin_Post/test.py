from core.memory_manager import save_message, load_memory, format_memory_for_prompt

save_message("user", "My name is A")
save_message("assistant", "Nice to meet you!")
save_message("user", "What is my name?")

memory = load_memory()
print("RAW MEMORY:", memory)

print("\nFORMATTED MEMORY:")
print(format_memory_for_prompt(memory))
