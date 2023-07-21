import requests
import unittest


class TestStudents(unittest.TestCase):
    def test_root(self):
        response = requests.get("http://localhost:8000/docs/students")

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.json() == {"detail": "Not Found"})

        self.assertEqual(response.json(), {"detail": "Not Found"})


if __name__ == "__main__":
    unittest.main()

# Correr todos los test en la carpeta testing
# python -m unittest discover -sv testing

# Correr un test en especifico
# python -m unittest discover -sv testing -p test_students.py

# python nombre_del_fichero.py
