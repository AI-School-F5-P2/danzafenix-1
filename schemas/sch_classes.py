from pydantic import BaseModel, Field

class ClassSchema(BaseModel):
    name_cla: str


class LevelSchema(BaseModel):
    name_level:str


class ClassLevelSchema(BaseModel):
    id_cla1: int = Field(ge = 1)
    id_level1: int = Field(ge = 1)
    id_pac1: int = Field(ge = 1)