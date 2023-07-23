from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from schemas.sch_prices import PackSchema
from config.database import Session
from models.mod_prices import ModelPacks


packs = APIRouter(prefix = "/api/packs", tags = ["Packs"])


@packs.get("/get_all", response_model = List[PackSchema], status_code = HTTP_200_OK)
def get_packs():
    db = Session()
    result = db.query(ModelPacks).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@packs.get("/{id_pac}", response_model = PackSchema)
def get_packs(id_pac: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPacks).filter(ModelPacks.id_pac == id_pac).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@packs.post("/create", status_code = HTTP_201_CREATED)
def create_pack(data_pack:PackSchema):
    db = Session()
    new_pack = ModelPacks(**data_pack.model_dump())
    db.add(new_pack)
    db.commit()
    return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro pack se ha creado correctamente"})


@packs.put("/{id_pac}", response_model = PackSchema)
def update_pack(data_update: PackSchema, id_pac: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPacks).filter(ModelPacks.id_pac == id_pac).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.name_pac = data_update.name_pac
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos del pack se han modificado correctamente"})


@packs.delete("/{id_pac}", status_code = HTTP_200_OK)
def delete_pack(id_pac: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPacks).filter(ModelPacks.id_pac == id_pac).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})

