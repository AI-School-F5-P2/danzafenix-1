from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, column_property
from config.database import Base

class ModelPacks(Base):

    __tablename__ = "packs"

    id_pac = Column(Integer, primary_key = True, index = True)
    name_pac = Column(String(50), nullable = False)
    class_level = relationship("ClassesLevels", back_populates = "packs1")


class ModelPrices(Base):

    __tablename__ = "prices-discounts"

    id_pd = Column(Integer, primary_key = True, index = True)
    type_pd = Column(String(50))
    individual_price = Column(Float, nullable = False, default = 35.00)
    discount2 = Column(Float, nullable = False, default = 0)
    price2 = column_property((individual_price*(100 - discount2))/100)
    discount3 = Column(Float, nullable = False, default = 0)
    price3 = column_property((individual_price*(100 - discount3))/100)
