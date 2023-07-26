from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


#Los schemas (esquemas) sirven para validar y serializar objetos:
#la validación de objetos se refiere a asegurarse de que los datos proporcionados 
#cumplan con ciertas reglas o restricciones predefinidas. Esto implica verificar que los valores proporcionados sean del tipo correcto.
#La serialización de objetos se refiere a convertir objetos en una representación que se pueda almacenar, transmitir o intercambiar fácilmente. 
#Esto implica convertir objetos en un formato estandarizado, como JSON, XML o binario, que pueda ser interpretado por otros sistemas o componentes.
class StudentSchema(BaseModel):
    name_stu: str
    last1_stu: str
    last2_stu: Optional[str]
    DNI_stu: str = Field(pattern = r'^([XYZ]\d{7}[A-Z]|\d{8}[A-HJ-NP-TV-Z])$')
    birth_date: date
    age_stu: int = Field(gt = 1, lt = 110)
    tel_stu: Optional[str]
    mail_stu: str = Field(pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    active_stu: bool
    fam_discount: bool
    
    #La clase config permite establecer valores predeterminados que facilitan la completación de los campos
    class Config:
        json_schema_extra = {"example": {"name_stu": "Nombre", "last1_stu": "Primer Apellido", "last2_stu": "Segundo Apellido",
                                    "DNI_stu": "12345678L", "birth_date": "2023-07-18", "age_stu": 20, "tel_stu": "+3412345678", 
                                    "mail_stu": "nombre156@gmail.com", "active_stu": True, "fam_discount": False}}


#Esquema de validación de la tabla intermedia EstudiantesClases
class StudentClassSchema(BaseModel):
    id_stu1: int = Field(ge = 1)
    id_cla_level1: int = Field(ge = 1)
    registration_date: date
    active_stu_cla: bool = Field(default = True)