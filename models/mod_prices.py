from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class ModelPacks(Base):

    __tablename__ = "packs"

    id_pac = Column(Integer, primary_key = True, index = True)
    name_pac = Column(String(50), nullable = False)