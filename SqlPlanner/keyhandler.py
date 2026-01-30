from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("endpoint")
api_version = os.getenv("api_version")
api_key = os.getenv("OPENAI_KEY")
deploment_name = os.getenv("deploment_name")

llm = AzureChatOpenAI(
    azure_deployment=deploment_name,
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version=api_version,
    temperature=0,
    max_retries=5,
)