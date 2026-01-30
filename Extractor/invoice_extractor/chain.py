from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser

from invoice_extractor.schema import InvoiceExtraction
from invoice_extractor.prompt import prompt


def build_chain():
    # 1. LLM
    llm = ChatGroq(
        model="groq/compound",
        temperature=0
    )

    # 2. Output parser (forces schema)
    parser = PydanticOutputParser(
        pydantic_object=InvoiceExtraction
    )

    # 3. Pipeline 
    chain = prompt | llm | parser

    return chain
