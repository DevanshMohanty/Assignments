from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert document understanding system.

Rules:
- Extract only what is explicitly present
- Do NOT hallucinate
- If a value is missing, use null
- Keys must match the schema exactly
"""
        ),
        (
            "human",
            """
Document text:
{invoice_text}

Tasks:
1. Identify document type: "invoice" or "purchase_order"
2. Extract header fields:
   - company_name
   - company_address
   - invoice_number (if invoice)
   - po_number (if purchase order)
   - invoice_date
   - total_amount
3. Extract all line items

Return structured data only.
"""
        )
    ]
)
