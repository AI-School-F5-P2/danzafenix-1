from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from models.mod_prices import ModelPacks


class ModelClasses(Base):

    __tablename__ = "classes"

    id_cla = Column(Integer, primary_key = True, index = True)
    name_cla = Column(String(50), nullable = False)
    levels1 = relationship("ModelLevels", secondary = "classes-levels", back_populates = "classes1")


class ModelLevels(Base):

    __tablename__ = "Levels"
    
    id_level = Column(Integer, primary_key = True, index = True)
    name_level = Column(String(50), nullable = False)
    classes1 = relationship("ModelClasses", secondary = "classes-levels", back_populates = "levels1")


class ClassesLevels(Base):

    __tablename__ = "classes-levels"

    id_cla_level = Column(Integer, primary_key = True, index = True)
    id_cla1 = Column(Integer, ForeignKey("classes.id_cla"))
    id_level1 = Column(Integer, ForeignKey("Levels.id_level"))
    classes1 = relationship("ModelClasses", back_populates = "levels1")
    levels1 = relationship("ModelLevels", back_populates = "classes1")
    id_pac1 = Column(Integer, ForeignKey("packs.id_pac"))
    packs1 = relationship("ModelPacks", back_populates = "class_level")

