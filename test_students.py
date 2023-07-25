from fastapi.testclient import TestClient
from main import app
from fastapi import Path
import unittest

class TestStudents(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root(self):
        response = self.client.get("/api/student/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hola, soy una nueva ruta"})

    def test_get_all(self):
        response = self.client.get("/api/student/get_all")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_student_by_id(self):
        response = self.client.get("/api/student/2")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

        response = self.client.get("/api/student/1000")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "El ID no se ha encontrado en la base de datos"})

    def test_get_student_by_DNI(self):
        response = self.client.get("/api/student/37213986F/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        

        response = self.client.get("/api/student/12345678J/")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "El DNI no se ha encontrado en la base de datos"})

    def test_create_student(self):
        data = {
            "name_stu": "Fulani",
            "last1_stu": "Mengani",
            "last2_stu": "Detali",
            "DNI_stu": "76339822T",
            "birth_date": "1970-07-18",
            "age_stu": 40,
            "tel_stu": "+3412345648",
            "mail_stu": "fulani156@gmail.com",
            "active_stu": True,
            "fam_discount": False
        }
        response = self.client.post("/api/student/create", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "El registro estudiante se ha creado correctamente"})

        # Intentar crear un estudiante con el mismo DNI debería devolver un error
        response = self.client.post("/api/student/create", json=data)
        self.assertEqual(response.status_code, 406)

    def test_update_student(self):
        data = {
            "name_stu": "John Updated",
            "last1_stu": "Doe Updated",
            "last2_stu": "lolailo",
            "DNI_stu": "37213969H",
            "birth_date": "1990-01-01",
            "age_stu": 30,
            "tel_stu": "+34123456789",
            "mail_stu": "john.do@gmail.com",
            "active_stu": True,
            "fam_discount": False
        }
        response = self.client.put("/api/student/2", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Los datos del estudiante se han modificado correctamente"})

        response = self.client.put("/api/student/1000", json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "El ID no se ha encontrado en la base de datos"})

    def test_delete_student(self):
        response = self.client.delete("/api/student/11")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Se ha eliminado el registro correctamente"})

        response = self.client.delete("/api/student/1000")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "El ID no se ha encontrado en la base de datos"})

if __name__ == "__main__":
    unittest.main()

# Antes de correr el test modificar Delete( el ID de la ruta), update(ID y DNI) y Post(DNI)