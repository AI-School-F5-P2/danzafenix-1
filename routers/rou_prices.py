from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from schemas.sch_prices import PackSchema, PriceSchema
from config.database import Session
from models.mod_prices import ModelPacks, ModelPrices


#CRUD de la tabla Packs
packs = APIRouter(prefix = "/api/packs", tags = ["Packs"])


#READ
@packs.get("/get_all", response_model = List[PackSchema], status_code = HTTP_200_OK)
def get_packs():
    db = Session()
    result = db.query(ModelPacks).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#READ utilizando la clave primaria para filtrar a una pack en específico
@packs.get("/{id_pac}", response_model = PackSchema)
def get_packs(id_pac: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPacks).filter(ModelPacks.id_pac == id_pac).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#CREATE
@packs.post("/create", status_code = HTTP_201_CREATED)
def create_pack(data_pack:PackSchema):
    db = Session()
    new_pack = ModelPacks(**data_pack.model_dump())
    db.add(new_pack)
    db.commit()
    return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro pack se ha creado correctamente"})


#UPDATE
@packs.put("/{id_pac}", response_model = PackSchema)
def update_pack(data_update: PackSchema, id_pac: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPacks).filter(ModelPacks.id_pac == id_pac).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.name_pac = data_update.name_pac
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos del pack se han modificado correctamente"})


#DELETE
@packs.delete("/{id_pac}", status_code = HTTP_200_OK)
def delete_pack(id_pac: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPacks).filter(ModelPacks.id_pac == id_pac).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})



#CRUD de la tabla Precios
prices = APIRouter(prefix = "/api/prices", tags = ["Prices"])


#READ
@prices.get("/get_all", response_model = List[PriceSchema], status_code = HTTP_200_OK)
def get_prices():
    db = Session()
    result = db.query(ModelPrices).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#READ utilizando la clave primaria para filtrar a unos precios en específico
@prices.get("/{id_pd}", response_model = PriceSchema)
def get_prices(id_pd: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPrices).filter(ModelPrices.id_pd == id_pd).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


#CREATE
@prices.post("/create", status_code = HTTP_201_CREATED)
def create_price(data_price: PriceSchema):
    db = Session()
    new_price = ModelPrices(**data_price.model_dump())
    db.add(new_price)
    db.commit()
    return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "El registro precio se ha creado correctamente"})


#UPDATE
@prices.put("/{id_pd}", response_model = PriceSchema)
def update_price(data_update: PriceSchema, id_pd: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPrices).filter(ModelPrices.id_pd == id_pd).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.type_pd = data_update.type_pd
    result.individual_price = data_update.individual_price
    result.discount2 = data_update.discount2
    result.discount3 = data_update.discount3
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos del precio se han modificado correctamente"})


#DELETE
@prices.delete("/{id_pd}", status_code = HTTP_200_OK)
def delete_price(id_pd: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelPrices).filter(ModelPrices.id_pd == id_pd).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})