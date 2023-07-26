from pydantic import BaseModel, Field


#Esquema de validación de la tabla Packs
class PackSchema(BaseModel):
    name_pac: str


#Esquema de validación de la tabla Precios
class PriceSchema(BaseModel):
    type_pd: str
    individual_price: float = Field(ge = 0)
    discount2: float = Field(ge = 0)
    discount3: float = Field(ge = 0)