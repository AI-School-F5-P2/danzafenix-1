from pydantic import BaseModel


#Esquema de validación de la tabla Profesores
class TeacherSchema(BaseModel):
    name_teacher: str