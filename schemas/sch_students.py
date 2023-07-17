from pydantic import BaseModel
from datetime import date
from typing import Optional

#los archivos schemas (esquemas) sirven para validar y serializar objetos:
#la validación de objetos se refiere a asegurarse de que los datos proporcionados 
#cumplan con ciertas reglas o restricciones predefinidas. Esto implica verificar que los valores proporcionados sean del tipo correcto.
#La serialización de objetos se refiere a convertir objetos en una representación que se pueda almacenar, transmitir o intercambiar fácilmente. 
#Esto implica convertir objetos en un formato estandarizado, como JSON, XML o binario, que pueda ser interpretado por otros sistemas o componentes.

class StudentSchema(BaseModel):
    id_stu: int
    name_stu: str
    last1_stu: str
    last2_stu: Optional[str]
    birth_date: date
    age_stu: int
    tel_stu: Optional[str]
    mail_stu: str
    active_stu: bool
    fam_discount: bool