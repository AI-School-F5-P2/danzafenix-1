from sqlalchemy import Column, Integer, String
from config.database import Base


#Tabla principal de Profesores
class ModelTeachers(Base):

    __tablename__ = "teachers"

    id_teacher = Column(Integer, primary_key = True, index = True)
    name_teacher = Column(String(50), nullable = False)