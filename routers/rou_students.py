from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_406_NOT_ACCEPTABLE
from schemas.sch_students import StudentSchema
from config.database import Session
from models.mod_students import ModelStudents


student = APIRouter(prefix = "/api/student", tags = ["Students"])


#creamos la ruta raíz para probar que la API funciona
@student.get("/")
def root():
    return {"message": "Hola, soy una nueva ruta"}


@student.get("/get_all", response_model = List[StudentSchema], status_code = HTTP_200_OK)
def get_students():
    db = Session()
    result = db.query(ModelStudents).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@student.get("/{id_stu}", response_model = StudentSchema)
def get_student(id_stu: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelStudents).filter(ModelStudents.id_stu == id_stu).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@student.get("/{DNI_stu}/", response_model = StudentSchema)
def get_student_by_DNI(DNI_stu: str = Path(pattern = r'^([XYZ]\d{7}[A-Z]|\d{8}[A-HJ-NP-TV-Z])$')):
    db = Session()
    result = db.query(ModelStudents).filter(ModelStudents.DNI_stu == DNI_stu).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El DNI no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#con la ruta post podemos dar de alta a un nuevo estudiante en la base de datos
#pasamos como parámetro el esquema Student para hacer la validación de tipos
#new_student = ModelStudents(**data_student.model_dump()). Los **indica que tomamos todos los datos como parámetros
@student.post("/create", status_code = HTTP_201_CREATED)
def create_student(data_student:StudentSchema):
    db = Session()
    verification = db.query(ModelStudents).filter(ModelStudents.DNI_stu == data_student.DNI_stu)
    if not verification:
        new_student = ModelStudents(**data_student.model_dump())
        db.add(new_student)
        db.commit()
        return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro estudiante se ha creado correctamente"})
    return JSONResponse(status_code=HTTP_406_NOT_ACCEPTABLE, content = {"message": "El DNI ya se ha registrado previamente"})



@student.put("/{id_stu}", response_model = StudentSchema)
def update_student(data_update: StudentSchema, id_stu: int = Path(ge = 1)):
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


@student.delete("/{id_stu}", status_code = HTTP_200_OK)
def delete_student(id_stu: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelStudents).filter(ModelStudents.id_stu == id_stu).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})