from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from schemas.sch_classes import ClassSchema, LevelSchema
from config.database import Session
from models.mod_classes import ModelClasses, ModelLevels


classes = APIRouter(prefix = "/api/class", tags = ["Classes"])


@classes.get("/get_all", response_model = List[ClassSchema], status_code = HTTP_200_OK)
def get_classes():
    db = Session()
    result = db.query(ModelClasses).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@classes.get("/{id_cla}", response_model = ClassSchema)
def get_classes(id_cla: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelClasses).filter(ModelClasses.id_cla == id_cla).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@classes.post("/create", status_code = HTTP_201_CREATED)
def create_class(data_class:ClassSchema):
    db = Session()
    new_class = ModelClasses(**data_class.model_dump())
    db.add(new_class)
    db.commit()
    return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro clase se ha creado correctamente"})


@classes.put("/{id_cla}", response_model = ClassSchema)
def update_class(data_update: ClassSchema, id_cla: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelClasses).filter(ModelClasses.id_cla == id_cla).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.name_cla = data_update.name_cla
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos de la clase se han modificado correctamente"})


@classes.delete("/{id_cla}", status_code = HTTP_200_OK)
def delete_class(id_cla: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelClasses).filter(ModelClasses.id_cla == id_cla).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})



levels = APIRouter(prefix = "/api/level", tags = ["Levels"])


@levels.get("/get_all", response_model = List[LevelSchema], status_code = HTTP_200_OK)
def get_levels():
    db = Session()
    result = db.query(ModelLevels).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@levels.get("/{id_level}", response_model = LevelSchema)
def get_levels(id_level: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelLevels).filter(ModelLevels.id_level == id_level).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@levels.post("/create", status_code = HTTP_201_CREATED)
def create_level(data_level:LevelSchema):
    db = Session()
    new_level = ModelLevels(**data_level.model_dump())
    db.add(new_level)
    db.commit()
    return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro nivel se ha creado correctamente"})


@levels.put("/{id_level}", response_model = LevelSchema)
def update_level(data_update: LevelSchema, id_level: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelLevels).filter(ModelLevels.id_level == id_level).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.name_level = data_update.name_level
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos del nivel se han modificado correctamente"})


@levels.delete("/{id_level}", status_code = HTTP_200_OK)
def delete_level(id_level: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelLevels).filter(ModelLevels.id_level == id_level).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})