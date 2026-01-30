from pydantic import BaseModel, Field
from typing import List, Optional, Union


class LineItem(BaseModel):
    description: Optional[str] = None
    quantity: Optional[Union[str, int, float]] = None
    unit_price: Optional[Union[str, float, int]] = None
    amount: Optional[Union[str, float, int]] = None


class DocumentHeader(BaseModel):
    company_name: Optional[str] = None
    company_address: Optional[str] = None
    invoice_number: Optional[str] = None
    po_number: Optional[str] = None
    invoice_date: Optional[str] = None
    total_amount: Optional[Union[str, float, int]] = None

class InvoiceExtraction(BaseModel):
    document_type: Optional[str] = None  # invoice | purchase_order
    
    # Accept both "header" and "header_fields"
    header: Optional[DocumentHeader] = Field(
        default=None,
        alias="header_fields"
    )

    line_items: List[LineItem] = []

    class Config:
        populate_by_name = True
