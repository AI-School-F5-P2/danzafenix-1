from pydantic import BaseModel, Field
from datetime import date


class InvoiceSchema(BaseModel):
    issuance_date: date
    tot_month: float = Field(ge = 0)
    id_stu2: int = Field(ge = 1)