# from fastapi.testclient import TestClient
# from main import app  # Asegúrate de que la ruta a tu archivo main.py sea correcta
# import unittest

# class TestStudents(unittest.TestCase):
#     def setUp(self):
#         self.client = TestClient(app)

#     def test_root(self):
#         response = self.client.get("/api/student/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"message": "Hola, soy una nueva ruta"})

#     def test_get_all(self):
#         response = self.client.get("/api/student/get_all")
#         # Comprueba que la respuesta tiene un código de estado 200
#         self.assertEqual(response.status_code, 200)
#         # Aquí podrías comprobar que la respuesta tiene el formato correcto, 
#         # pero eso dependería de los datos devueltos por tu API

#    

# if __name__ == "__main__":
#     unittest.main()

from fastapi.testclient import TestClient
from main import app
from fastapi import Path
import unittest

class TestStudents(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    # def test_root(self):
    #     response = self.client.get("/api/student/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {"message": "Hola, soy una nueva ruta"})

    # def test_get_all(self):
    #     response = self.client.get("/api/student/get_all")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsInstance(response.json(), list)

    # def test_get_student_by_id(self):
    #     response = self.client.get("/api/student/2")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsInstance(response.json(), dict)

    #     response = self.client.get("/api/student/1000")
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json(), {"message": "El ID no se ha encontrado en la base de datos"})

    # def test_get_student_by_DNI(self):
    #     response = self.client.get("/api/student/37213986F/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsInstance(response.json(), dict)
        

    #     response = self.client.get("/api/student/12345678")
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json(), {"message": "El ID no se ha encontrado en la base de datos"})

    def test_create_student(self):
        data = {
            "name_stu": "Nombre",
            "last1_stu": "Primer Apellido",
            "last2_stu": "Segundo Apellido",
            "DNI_stu": "76339855D",
            "birth_date": "1998-07-18",
            "age_stu": 20,
            "tel_stu": "+3412345678",
            "mail_stu": "nombre156@gmail.com",
            "active_stu": True,
            "fam_discount": False
        }
        response = self.client.post("/api/student/create", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "El registro estudiante se ha creado correctamente"})

        # Intentar crear un estudiante con el mismo DNI debería devolver un error
        response = self.client.post("/api/student/create", json=data)
        self.assertEqual(response.status_code, 406)

    # def test_update_student(self):
    #     data = {
    #         "name_stu": "John Updated",
    #         "last1_stu": "Doe Updated",
    #         "DNI_stu": "37213986F",
    #         "birth_date": "1990-01-01",
    #         "age_stu": 30,
    #         "tel_stu": "+34123456789",
    #         "mail_stu": "john.doe@gmail.com",
    #         "active_stu": True,
    #         "fam_discount": False
    #     }
    #     response = self.client.put("/api/student/1", json=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {"message": "Los datos del estudiante se han modificado correctamente"})

    #     response = self.client.put("/api/student/1000", json=data)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json(), {"message": "El ID no se ha encontrado en la base de datos"})

    # def test_delete_student(self):
    #     response = self.client.delete("/api/student/3")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {"message": "Se ha eliminado el registro correctamente"})

    #     response = self.client.delete("/api/student/1000")
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json(), {"message": "El ID no se ha encontrado en la base de datos"})

if __name__ == "__main__":
    unittest.main()
