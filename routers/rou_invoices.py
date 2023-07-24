from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from config.database import Session
from models.mod_prices import ModelPacks, ModelPrices
from models.mod_students import ModelStudents, StudentsClasses
from models.mod_classes import ClassesLevels
from datetime import date


#función calcular precios
def invoice_calculation():
    db = Session()
    result = db.query(ModelStudents.DNI_stu, ModelPrices.id_pd
                      ).join(StudentsClasses, ModelStudents.id_stu == StudentsClasses.id_stu1
                            ).join(ClassesLevels, StudentsClasses.id_cla_level1 == ClassesLevels.id_cla_level
                                   ).join(ModelPacks, ClassesLevels.id_pac1 == ModelPacks.id_pac
                                          ).join(ModelPrices, ModelPacks.id_pd1 == ModelPrices.id_pd
                                                 ).filter(StudentsClasses.active_stu_cla == False).all()
    try:
        prices = [element[1] for element in result]
        max_value = max(prices)
        tot_month = 0
        for i in range(1, max_value + 1,):
            y = prices.count(i)
            if y == 1:
                tot_month += db.query(ModelPrices.individual_price).filter(ModelPrices.id_pd == i).scalar()
            elif y == 2:
                individual_price = db.query(ModelPrices.individual_price).filter(ModelPrices.id_pd == i).scalar()
                price2 = db.query(ModelPrices.price2).filter(ModelPrices.id_pd == i).scalar()
                tot_month += individual_price + price2
            elif y >= 3:
                individual_price = db.query(ModelPrices.individual_price).filter(ModelPrices.id_pd == i).scalar()
                price2 = db.query(ModelPrices.price2).filter(ModelPrices.id_pd == i).scalar()
                price3 = db.query(ModelPrices.price3).filter(ModelPrices.id_pd == i).scalar()
                tot_month += individual_price + price2 + ((y - 2)*price3)
            else:
                tot_month = tot_month
        print(tot_month)

    except ValueError:
        print("El estudiante no está activo en ninguna clase este mes")

invoice_calculation()