from keyhandler import llm


class LLMClient:
    """
    Thin wrapper around AzureChatOpenAI.
    Ensures all callers get plain text output.
    """

    def invoke(self, prompt: str) -> str:
        response = llm.invoke(prompt)
        return response.content



def get_llm() -> LLMClient:
    return LLMClient()
