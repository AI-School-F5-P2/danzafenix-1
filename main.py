#Importación inicial de todos los módulos y librerías
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
import logging
from fenix_example import data_teachers, data_classes, data_levels, data_packs, data_prices, data_classes_levels_packs, data_students, data_students_classes
import os


#Creación del archivo logging para trazabilidad
logging.basicConfig(filename = "logfenix.log", level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s', datefmt = '%Y/%m/%d %I:%M:%S %p')


#Creación de una instancia de FastAPI llamada app junto con su título y su versión
#Para lanzar el servidor y abrir Swagger se usa el comando uvicorn main:app --reload
app = FastAPI()
app.title = "Danza Fénix"
app.version = "1.0.0"


#Creación de todas las tablas (modelos)
ModelStudents.metadata.create_all(bind = engine)
ModelTeachers.metadata.create_all(bind = engine)
ModelClasses.metadata.create_all(bind = engine)
ModelLevels.metadata.create_all(bind = engine)
ClassesLevels.metadata.create_all(bind = engine)
ModelPacks.metadata.create_all(bind = engine)
ModelPrices.metadata.create_all(bind = engine)
StudentsClasses.metadata.create_all(bind = engine)
ModelInvoices.metadata.create_all(bind = engine)
logging.debug("Creación correcta de tablas")


#Se incluyen las rutas creadas en la carpeta routers para cada una de las entidades
app.include_router(student)
app.include_router(teacher)
app.include_router(classes)
app.include_router(levels)
app.include_router(packs)
app.include_router(prices)
app.include_router(invoices)
app.include_router(student_class)
logging.info("Creación de rutas")


def tables_completion():
    '''    
    Esta función completa la base de datos con los datos de ejemplo del archivo fenix_example.py para hacer las verificaciones de funcionamiento
    Se trata simplemente de bucles For que guardan cada línea en la base de datos
    Para que sólo se ejecute una vez, se crea el archivo "database_initialized.txt" como indicador de inicialización
    '''
    
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
        logging.info("Inicialización de la base de datos con las tablas de ejemplo")

tables_completion()