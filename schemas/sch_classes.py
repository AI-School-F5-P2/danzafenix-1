from pydantic import BaseModel, Field


#Esquema de validación de Clases
class ClassSchema(BaseModel):
    name_cla: str


#Esquema de validación de Niveles
class LevelSchema(BaseModel):
    name_level:str


#Esquema de validación de la tabla intermedia de ClasesNiveles
#Se especifica que las claves foráneas deben ser iguales o mayores a 1 con la función Field
class ClassLevelSchema(BaseModel):
    id_cla1: int = Field(ge = 1)
    id_level1: int = Field(ge = 1)
    id_pac1: int = Field(ge = 1)


#Esquema de validación de Registros para poder segregar las inscripciones de los Estudiantes por mes en rou_students
#El campo DNI_stu tiene como validación una expresión regular que coincide con el patrón del DNI y el NIE español
class RegistrationSchema(BaseModel):
    name_stu: str
    DNI_stu: str = Field(pattern = r'^([XYZ]\d{7}[A-Z]|\d{8}[A-HJ-NP-TV-Z])$') 
    name_cla: str
    name_level: str