from pydantic import BaseModel, Field
from datetime import date


#Esquema de validación de la tabla Facturas
#Validaciones de los campos con el método Field
class InvoiceSchema(BaseModel):
    issuance_date: date
    tot_month: float = Field(ge = 0)
    id_stu2: int = Field(ge = 1)