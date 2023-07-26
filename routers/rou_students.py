from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_406_NOT_ACCEPTABLE
from schemas.sch_students import StudentSchema, StudentClassSchema
from schemas.sch_classes import RegistrationSchema
from config.database import Session
from models.mod_students import ModelStudents, StudentsClasses
from models.mod_classes import ModelClasses, ModelLevels, ClassesLevels
from sqlalchemy import extract
import logging


#CRUD de la tabla principal Estudiantes
student = APIRouter(prefix = "/api/student", tags = ["Students"])


#Prueba rápida para verificar que la ruta raíz funciona
@student.get("/")
def root():
    return {"message": "La API Danza Fénix contiene todos los endpoints para gestionar la base de datos de la Academia y facilitar la facturación"}


#READ
@student.get("/get_all", response_model = List[StudentSchema], status_code = HTTP_200_OK)
def get_students():
    logging.info("Se ha recibido una solicitud para obtener los estudiantes")
    db = Session()
    result = db.query(ModelStudents).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#READ utilizando la clave primaria para filtrar a un estudiante en específico
@student.get("/{id_stu}", response_model = StudentSchema)
def get_student(id_stu: int = Path(ge = 1)):
    logging.info(f"Se ha recibido una solicitud para obtener a un estudiante con ID {id_stu}")
    db = Session()
    result = db.query(ModelStudents).filter(ModelStudents.id_stu == id_stu).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#READ utilizando el DNI para filtrar a un estudiante en específico
#La validación de query tiene una expresión regular para el campo DNI_stu
@student.get("/{DNI_stu}/", response_model = StudentSchema)
def get_student_by_DNI(DNI_stu: str = Path(pattern = r'^([XYZ]\d{7}[A-Z]|\d{8}[A-HJ-NP-TV-Z])$')):
    logging.info(f"Se ha recibido una solicitud para obtener a un estudiante con DNI {DNI_stu}")
    db = Session()
    result = db.query(ModelStudents).filter(ModelStudents.DNI_stu == DNI_stu).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El DNI no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#CREATE
#Se pasa como parámetro el StudentSchema para hacer la validación de tipos
#new_student = ModelStudents(**data_student.model_dump()). Los ** indica que se toman todos los datos como parámetros
@student.post("/create", status_code = HTTP_201_CREATED)
def create_student(data_student: StudentSchema):
    logging.info("Se ha recibido una solicitud para crear un registro de estudiante")
    db = Session()
    verification = db.query(ModelStudents).filter(ModelStudents.DNI_stu == data_student.DNI_stu).first()
    if not verification:
        new_student = ModelStudents(**data_student.model_dump())
        db.add(new_student)
        db.commit()
        return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro estudiante se ha creado correctamente"})
    return JSONResponse(status_code = HTTP_406_NOT_ACCEPTABLE, content = {"message": "El DNI ya se ha registrado previamente"})


#UPDATE
@student.put("/{id_stu}", response_model = StudentSchema)
def update_student(data_update: StudentSchema, id_stu: int = Path(ge = 1)):
    logging.info("Se ha recibido una solicitud para actualizar un registro de estudiante")
    db = Session()
    result = db.query(ModelStudents).filter(ModelStudents.id_stu == id_stu).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.name_stu = data_update.name_stu
    result.last1_stu = data_update.last1_stu
    result.last2_stu = data_update.last2_stu
    result.DNI_stu = data_update.DNI_stu
    result.birth_date = data_update.birth_date
    result.age_stu = data_update.age_stu
    result.tel_stu = data_update.tel_stu
    result.mail_stu = data_update.mail_stu
    result.active_stu = data_update.active_stu
    result.fam_discount = data_update.fam_discount
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos del estudiante se han modificado correctamente"})


#DELETE
@student.delete("/{id_stu}", status_code = HTTP_200_OK)
def delete_student(id_stu: int = Path(ge = 1)):
    logging.info("Se ha recibido una solicitud para eliminar un registro de estudiante")
    db = Session()
    result = db.query(ModelStudents).filter(ModelStudents.id_stu == id_stu).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})



#CRUD de la tabla intermedia EstudiantesClases
student_class = APIRouter(prefix = "/api/student_class", tags = ["Students - Classes"])


#READ
@student_class.get("/get_all", response_model = List[StudentClassSchema], status_code = HTTP_200_OK)
def get_students_classes():
    logging.info("Se ha recibido una solicitud para obtener los estudiantes y sus clases")
    db = Session()
    result = db.query(StudentsClasses).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#READ utilizando la clave primaria para filtrar a un estudiante y sus respectivas clases en específico
@student_class.get("/{id_stu1}", response_model = List[StudentClassSchema])
def get_student_classes(id_stu1: int = Path(ge = 1)):
    logging.info(f"Se ha recibido una solicitud para obtener a un estudiante y sus clases con ID {id_stu1}")
    db = Session()
    result = db.query(StudentsClasses).filter(StudentsClasses.id_stu1 == id_stu1).all()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#CREATE
@student_class.post("/create", status_code = HTTP_201_CREATED)
def create_student_class(data_student_class: StudentClassSchema):
    logging.info("Se ha recibido una solicitud para crear un registro de estudiante y clases")
    db = Session()
    new_student_class = StudentsClasses(**data_student_class.model_dump())
    db.add(new_student_class)
    db.commit()
    return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro estudiante y su respectiva clase se ha creado correctamente"})


#UPDATE
@student_class.put("/{id_stu1}/{id_cla_level1}", response_model = StudentSchema)
def update_student(data_update: StudentClassSchema, id_stu1: int = Path(ge = 1), id_cla_level1: int = Path(ge = 1)):
    logging.info("Se ha recibido una solicitud para actualizar un registro de estudiante y clases")
    db = Session()
    result = db.query(StudentsClasses).filter(StudentsClasses.id_stu1 == id_stu1, StudentsClasses.id_cla_level1 == id_cla_level1).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.id_stu1 = data_update.id_stu1
    result.id_cla_level1 = data_update.id_cla_level1
    result.registration_date = data_update.registration_date
    result.active_stu_cla = data_update.active_stu_cla
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos del estudiante y su respectiva clase se han modificado correctamente"})


#DELETE
@student_class.delete("/{id_stu1}/{id_cla_level1}", status_code = HTTP_200_OK)
def delete_student_class(id_stu1: int = Path(ge = 1), id_cla_level1: int = Path(ge = 1)):
    logging.info("Se ha recibido una solicitud para eliminar un registro de estudiante y clases")
    db = Session()
    result = db.query(StudentsClasses).filter(StudentsClasses.id_stu1 == id_stu1, StudentsClasses.id_cla_level1 == id_cla_level1).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})


#READ: ingresando el año y el mes se obtiene una lista de diccionarios que contiene 
#el nombre del estudiante y las clases en las que se inscribió en ese mes
#El bucle For se utiliza para convertir la query en una lista de diccionarios
@student_class.get("/by_month/{year}/{month}/", response_model = List[RegistrationSchema], status_code = HTTP_200_OK)
def students_classes_by_month(year: int, month: int = Path(ge = 1, le = 12)):
    logging.info(f"Se ha recibido una solicitud para obtener los estudiantes y clases del año: {year} y el mes: {month}")
    db = Session()
    result = db.query(ModelStudents.name_stu, ModelStudents.DNI_stu, ModelClasses.name_cla, ModelLevels.name_level
                      ).join(StudentsClasses, ModelStudents.id_stu == StudentsClasses.id_stu1
                             ).join(ClassesLevels, StudentsClasses.id_cla_level1 == ClassesLevels.id_cla_level
                                    ).join(ModelClasses, ClassesLevels.id_cla1 == ModelClasses.id_cla
                                           ).join(ModelLevels, ClassesLevels.id_level1 == ModelLevels.id_level
                                                  ).filter(extract("month", StudentsClasses.registration_date) == month, 
                                                          extract("year", StudentsClasses.registration_date) == year).all()
    response_data = []
    for name_stu, DNI_stu, name_cla, name_level in result:
        response_data.append({
            "name_stu": name_stu,
            "DNI_stu": DNI_stu,
            "name_cla": name_cla,
            "name_level": name_level})
        logging.info(f"Los datos convertidos son: {name_stu}, {DNI_stu}, {name_cla}, {name_level}")
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(response_data))