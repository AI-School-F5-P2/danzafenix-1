from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


#Tabla principal de Estudiantes: incluye las distintas columnas y el tipo de dato que debería tener cada una con algunas validaciones
class ModelStudents(Base):

    __tablename__ = "students"

    id_stu = Column(Integer, primary_key = True, index = True)
    name_stu = Column(String(50), nullable = False)
    last1_stu = Column(String(50), nullable = False)
    last2_stu = Column(String(50))
    DNI_stu = Column(String(9), unique = True, nullable = False)
    birth_date = Column(Date, nullable = False)
    age_stu = Column(Integer, nullable = False)
    tel_stu = Column(String(20))
    mail_stu = Column(String(100), nullable = False)
    active_stu = Column(Boolean, default = True, nullable = False)
    fam_discount = Column(Boolean, default = False, nullable = False)
    classes_levels = relationship("StudentsClasses", back_populates = "students")
    invoices = relationship("ModelInvoices", back_populates = "students1")


#Tabla intermedia que relaciona Estudiantes con ClasesNiveles
class StudentsClasses(Base):

    __tablename__ = "students_classes"

    id_stu_cla_level = Column(Integer, primary_key = True, index = True)
    id_stu1 = Column(Integer, ForeignKey("students.id_stu"))
    id_cla_level1 = Column(Integer, ForeignKey("classes_levels.id_cla_level"))
    registration_date = Column(Date, nullable = False)
    active_stu_cla = Column(Boolean, default = True, nullable = False)
    students = relationship("ModelStudents", back_populates = "classes_levels")
    classes_levels = relationship("ClassesLevels", back_populates = "students")