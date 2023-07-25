from fastapi import FastAPI
from routers.rou_students import student, student_class
from routers.rou_teachers import teacher
from routers.rou_classes import classes, levels
from routers.rou_prices import packs, prices
from routers.rou_invoices import invoices
from config.database import engine, Session
from models.mod_students import ModelStudents, StudentsClasses
from models.mod_teachers import ModelTeachers
from models.mod_classes import ModelClasses, ModelLevels, ClassesLevels
from models.mod_prices import ModelPacks, ModelPrices
from models.mod_invoices import ModelInvoices
from fenix_example import data_teachers, data_classes, data_levels, data_packs, data_prices, data_classes_levels_packs, data_students, data_students_classes
import os


#creamos una instancia de FastAPI llamada app
app = FastAPI()
app.title = "Danza Fénix"
app.version = "1.0.0"


ModelStudents.metadata.create_all(bind = engine)
ModelTeachers.metadata.create_all(bind = engine)
ModelClasses.metadata.create_all(bind = engine)
ModelLevels.metadata.create_all(bind = engine)
ClassesLevels.metadata.create_all(bind = engine)
ModelPacks.metadata.create_all(bind = engine)
ModelPrices.metadata.create_all(bind = engine)
StudentsClasses.metadata.create_all(bind = engine)
ModelInvoices.metadata.create_all(bind = engine)


app.include_router(student)
app.include_router(teacher)
app.include_router(classes)
app.include_router(levels)
app.include_router(packs)
app.include_router(prices)
app.include_router(invoices)
app.include_router(student_class)


#datos de ejemplo para hacer verificaciones del funcionamiento del programa
def tables_completion():
    
    db = Session()
    
    #comprobamos si el archivo "database_initialized.txt" existe
    if os.path.exists("database_initialized.txt"):
        print("La base de datos ya está inicializada. No se realizará la inserción de datos nuevamente.")
        return
    
    for data in data_teachers:
        teacher = ModelTeachers(**data)
        db.add(teacher)
        db.commit()

    for data in data_classes:
        classes = ModelClasses(**data)
        db.add(classes)
        db.commit()

    for data in data_levels:
        level = ModelLevels(**data)
        db.add(level)
        db.commit()
    
    for data in data_prices:
        price = ModelPrices(**data)
        db.add(price)
        db.commit()
    
    for data in data_packs:
        pack = ModelPacks(**data)
        db.add(pack)
        db.commit()

    for data in data_students:
        student = ModelStudents(**data)
        db.add(student)
        db.commit()
    
    for data in data_classes_levels_packs:
        cla_level_pack = ClassesLevels(**data)
        db.add(cla_level_pack)
        db.commit()
    
    for data in data_students_classes:
        student_cla_level = StudentsClasses(**data)
        db.add(student_cla_level)
        db.commit()
    
    with open("database_initialized.txt", "w") as file:
        file.write("La base de datos está inicializada.")

tables_completion()