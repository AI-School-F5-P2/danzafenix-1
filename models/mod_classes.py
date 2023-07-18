from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class ModelClasses(Base):

    __tablename__ = "classes"

    id_cla = Column(Integer, primary_key = True, index = True)
    name_cla = Column(String(50), nullable = False)


class ModelLevels(Base):

    __tablename__ = "Levels"
    
    id_level = Column(Integer, primary_key = True, index = True)
    name_level = Column(String(50), nullable = False)