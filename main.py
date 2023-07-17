from fastapi import FastAPI
from routers.rou_students import student
from routers.rou_teachers import teacher
from config.database import engine, Session
from models.mod_students import ModelStudents
from models.mod_teachers import ModelTeachers


#creamos una instancia de FastAPI llamada app
app = FastAPI()
app.title = "Danza Fénix"
app.version = "1.0.0"

ModelStudents.metadata.create_all(bind = engine)
ModelTeachers.metadata.create_all(bind = engine)

#dependencia: consultar más sobre cómo usarla correctamente
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

app.include_router(student)
app.include_router(teacher)
