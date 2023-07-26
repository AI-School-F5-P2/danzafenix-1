from sqlalchemy import Column, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from config.database import Base


#Tabla principal de Facturas. La columna tot_month se calcula con la función invoice_calculation en rou_invoices a través de la ruta Post
class ModelInvoices(Base):

    __tablename__ = "invoices"

    id_inv = Column(Integer, primary_key = True, index = True)
    issuance_date = Column(Date, nullable = False)
    tot_month = Column(Float, nullable = False)
    id_stu2 = Column(Integer, ForeignKey("students.id_stu"))
    students1 = relationship("ModelStudents", back_populates = "invoices")