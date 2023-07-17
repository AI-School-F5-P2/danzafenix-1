from pydantic import BaseModel

class TeacherSchema(BaseModel):
    id_teacher: int
    name_teacher: str