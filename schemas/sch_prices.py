from pydantic import BaseModel, Field

class PackSchema(BaseModel):
    name_pac: str


class PriceSchema(BaseModel):
    type_pd: str
    individual_price: float = Field(ge = 0)
    discount2: float = Field(ge = 0)
    discount3: float = Field(ge = 0)