from pydantic import BaseModel, Field


class ClassSchema(BaseModel):
    name_cla: str


class LevelSchema(BaseModel):
    name_level:str


class ClassLevelSchema(BaseModel):
    id_cla1: int = Field(ge = 1)
    id_level1: int = Field(ge = 1)
    id_pac1: int = Field(ge = 1)


class RegistrationSchema(BaseModel):
    name_stu: str
    DNI_stu: str = Field(pattern = r'^([XYZ]\d{7}[A-Z]|\d{8}[A-HJ-NP-TV-Z])$') 
    name_cla: str
    name_level: str