from core.llm_manager import get_llm
from core.memory_manager import load_memory, save_message, format_memory_for_prompt
from core.prompt_manager import get_prompt 

class LinkedInPostGenerator:
    def __init__(self, role: str = "LinkedIn content writer"):
        self.llm = get_llm()                  # Initialize your LLM
        self.role = role                      # Role injected into prompt
        self.prompt_template = get_prompt()   # Load template

    def generate(self, topic: str) -> str:
        # Load memory from disk
        memory = load_memory()

        #Format memory for prompt
        memory_context = format_memory_for_prompt(memory)

        #Fill prompt template
        prompt = self.prompt_template.format(
            role=self.role,
            topic=topic,
            memory=memory_context
        )

        #Generate post using your LLM
        response = self.llm.invoke(prompt)
        post_text = response.content

        #Save both user input and assistant response
        save_message("user", topic)
        save_message("assistant", post_text)

        #Return only the current generated post 
        return post_text
