from pydantic import BaseModel

class ClassSchema(BaseModel):
    id_cla: int
    name_cla: str