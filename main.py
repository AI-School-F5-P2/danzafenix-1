from fastapi import FastAPI
from routers.rou_students import student
from routers.rou_teachers import teacher
from routers.rou_classes import classes, levels
from routers.rou_prices import packs
from config.database import engine, Session
from models.mod_students import ModelStudents
from models.mod_teachers import ModelTeachers
from models.mod_classes import ModelClasses, ModelLevels
from models.mod_prices import ModelPacks


#creamos una instancia de FastAPI llamada app
app = FastAPI()
app.title = "Danza Fénix"
app.version = "1.0.0"

ModelStudents.metadata.create_all(bind = engine)
ModelTeachers.metadata.create_all(bind = engine)
ModelClasses.metadata.create_all(bind = engine)
ModelLevels.metadata.create_all(bind = engine)
ModelPacks.metadata.create_all(bind = engine)


#dependencia: consultar más sobre cómo usarla correctamente
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

app.include_router(student)
app.include_router(teacher)
app.include_router(classes)
app.include_router(levels)
app.include_router(packs)
