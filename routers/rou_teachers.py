from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from schemas.sch_teachers import TeacherSchema
from config.database import Session
from models.mod_teachers import ModelTeachers


teacher = APIRouter()


@teacher.get("/api/teacher", response_model = List[TeacherSchema], tags = ["Teachers"], status_code = HTTP_200_OK)
def get_teachers():
    db = Session()
    result = db.query(ModelTeachers).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@teacher.get("/api/teacher/{id_teacher}", response_model = TeacherSchema, tags = ["Teachers"])
def get_teacher(id_teacher: int):
    db = Session()
    result = db.query(ModelTeachers).filter(ModelTeachers.id_teacher == id_teacher).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@teacher.post("/api/teacher", status_code = HTTP_201_CREATED, tags = ["Teachers"])
def create_teacher(data_teacher:TeacherSchema):
    db = Session()
    new_teacher = ModelTeachers(**data_teacher.model_dump())
    db.add(new_teacher)
    db.commit()
    return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro profesor se ha creado correctamente"})


@teacher.put("/api/teacher/{id_teacher}", response_model = TeacherSchema, tags = ["Teachers"])
def update_teacher(id_teacher: int, data_update: TeacherSchema):
    db = Session()
    result = db.query(ModelTeachers).filter(ModelTeachers.id_teacher == id_teacher).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.name_teacher = data_update.name_teacher
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos del profesor se han modificado correctamente"})


@teacher.delete("/api/teacher/{id_teache}", status_code = HTTP_200_OK, tags = ["Teachers"])
def delete_teacher(id_teacher: int):
    db = Session()
    result = db.query(ModelTeachers).filter(ModelTeachers.id_teacher == id_teacher).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})