from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from config.database import Session
from models.mod_prices import ModelPacks, ModelPrices
from models.mod_students import ModelStudents, StudentsClasses
from models.mod_invoices import ModelInvoices
from models.mod_classes import ClassesLevels
from schemas.sch_invoices import InvoiceSchema
from datetime import date


invoices = APIRouter(prefix = "/api/invoices", tags = ["Invoices"])


@invoices.get("/get_all", response_model = List[InvoiceSchema], status_code = HTTP_200_OK)
def get_invoices():
    db = Session()
    result = db.query(ModelInvoices).all()
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@invoices.get("/{id_inv}", response_model = List[InvoiceSchema])
def get_invoice_id(id_inv: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelInvoices).filter(ModelInvoices.id_inv == id_inv).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@invoices.get("/{DNI_stu}/", response_model = List[InvoiceSchema])
def get_invoice_DNI(DNI_stu: str = Path(pattern = r'^([XYZ]\d{7}[A-Z]|\d{8}[A-HJ-NP-TV-Z])$')):
    db = Session()
    result = db.query(ModelInvoices).join(ModelStudents, ModelInvoices.id_stu2 == ModelStudents.id_stu
                                          ).filter(ModelStudents.DNI_stu == DNI_stu).all()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El DNI no se ha encontrado en la base de datos"})
    return JSONResponse(status_code = HTTP_200_OK, content = jsonable_encoder(result))


@invoices.post("/generate", status_code = HTTP_201_CREATED)
def generate_invoice():
    db = Session()
    today = date.today()
    formatted_today = today.strftime("%Y-%m-%d")
    active_students = db.query(StudentsClasses).filter(StudentsClasses.active_stu_cla == True).all()
    for student in active_students:
        # Verificamos si el estudiante ya tiene una factura para la fecha de hoy
        existing_invoice = db.query(ModelInvoices).filter(ModelInvoices.id_stu2 == student.id_stu1, ModelInvoices.issuance_date == formatted_today).first()

        # Si no hay una factura existente para el estudiante en la fecha de hoy, generamos una nueva factura
        if not existing_invoice:
            # Calculamos el total de la factura para el estudiante
            total_invoice = invoice_calculation(student.id_stu1)

            # Creamos una nueva instancia de la tabla ModelInvoices
            new_invoice = ModelInvoices(issuance_date = formatted_today, tot_month = total_invoice, id_stu2 = student.id_stu1)
            db.add(new_invoice)
            db.commit()
    return JSONResponse(status_code = HTTP_201_CREATED, content = {"message": "Las facturas se han generado correctamente"})


@invoices.put("/{id_inv}", response_model = InvoiceSchema)
def update_invoice(data_update: InvoiceSchema, id_inv: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelInvoices).filter(ModelInvoices.id_inv == id_inv).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    result.issuance_date = data_update.issuance_date
    result.tot_month = data_update.tot_month
    result.id_stu2 = data_update.id_stu2
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Los datos de la factura se han modificado correctamente"})


@invoices.delete("/{id_inv}", status_code = HTTP_200_OK)
def delete_invoice(id_inv: int = Path(ge = 1)):
    db = Session()
    result = db.query(ModelInvoices).filter(ModelInvoices.id_inv == id_inv).first()
    if not result:
        return JSONResponse(status_code = HTTP_404_NOT_FOUND, content = {"message": "El ID no se ha encontrado en la base de datos"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = HTTP_200_OK, content = {"message": "Se ha eliminado el registro correctamente"})


#función calcular precios
def invoice_calculation(id_stu1):
    db = Session()
    result = db.query(ModelStudents.DNI_stu, ModelPrices.id_pd
                      ).join(StudentsClasses, ModelStudents.id_stu == StudentsClasses.id_stu1
                            ).join(ClassesLevels, StudentsClasses.id_cla_level1 == ClassesLevels.id_cla_level
                                   ).join(ModelPacks, ClassesLevels.id_pac1 == ModelPacks.id_pac
                                          ).join(ModelPrices, ModelPacks.id_pd1 == ModelPrices.id_pd
                                                 ).filter(StudentsClasses.active_stu_cla == True, StudentsClasses.id_stu1 == id_stu1).all()
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
        
        fam_discount = db.query(ModelStudents.fam_discount).filter(ModelStudents.id_stu == id_stu1).first()
        
        if fam_discount == True:
            tot_month = 0.9*tot_month
        return tot_month

    except ValueError:
        print("El estudiante no está activo en ninguna clase este mes")
        return 0