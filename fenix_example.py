#llenamos las tablas con las especificaciones del briefing

data_teachers = [{"name_teacher": "Mar"}, 
                 {"name_teacher": "Flor"},
                 {"name_teacher": "Nayara"},
                 {"name_teacher": "Marifé"},
                 {"name_teacher": "Álvaro"},
                 {"name_teacher": "Nieves"},
                 {"name_teacher": "Sofía"}]


data_classes = [{"name_cla": "Bachata"},
                {"name_cla": "Salsa"},
                {"name_cla": "Kizomba"},
                {"name_cla": "Estilo para todos"},
                {"name_cla": "Lady Style"},
                {"name_cla": "Role Rotation"},
                {"name_cla": "Pilates"},
                {"name_cla": "Yoga"},
                {"name_cla": "Flamenco"},
                {"name_cla": "Zouk"}]


data_levels = [{"name_level": "Cero"},
               {"name_level": "Iniciación"},
               {"name_level": "Medio"},
               {"name_level": "Avanzado"},
               {"name_level": "Único"}]


data_packs = [{"name_pac": "Latino", "id_pd1": 1},
              {"name_pac": "Estilo-Zouk", "id_pd1": 2},
              {"name_pac": "Relajación", "id_pd1": 2},
              {"name_pac": "Otros", "id_pd1": 3}]


data_prices = [{"type_pd": "Normal", "individual_price": 35.00, "discount2": 50.0, "discount3": 75.0},
               {"type_pd": "Premium", "individual_price": 40.00, "discount2": 50.0, "discount3": 75.0},
               {"type_pd": "Premium Individual", "individual_price": 40.00, "discount2": 0.0, "discount3": 0.0}]


data_classes_levels_packs = [{"id_cla1": 1, "id_level1": 1, "id_pac1": 1},
                             {"id_cla1": 1, "id_level1": 2, "id_pac1": 1},
                             {"id_cla1": 1, "id_level1": 3, "id_pac1": 1},
                             {"id_cla1": 1, "id_level1": 4, "id_pac1": 1},
                             {"id_cla1": 2, "id_level1": 2, "id_pac1": 1},
                             {"id_cla1": 2, "id_level1": 3, "id_pac1": 1},
                             {"id_cla1": 3, "id_level1": 2, "id_pac1": 1},
                             {"id_cla1": 3, "id_level1": 3, "id_pac1": 1},
                             {"id_cla1": 3, "id_level1": 4, "id_pac1": 1},
                             {"id_cla1": 4, "id_level1": 5, "id_pac1": 2},
                             {"id_cla1": 5, "id_level1": 5, "id_pac1": 4},
                             {"id_cla1": 6, "id_level1": 2, "id_pac1": 1},
                             {"id_cla1": 6, "id_level1": 3, "id_pac1": 1},
                             {"id_cla1": 7, "id_level1": 5, "id_pac1": 3},
                             {"id_cla1": 8, "id_level1": 5, "id_pac1": 3},
                             {"id_cla1": 9, "id_level1": 5, "id_pac1": 4},
                             {"id_cla1": 10, "id_level1": 2, "id_pac1": 2},
                             {"id_cla1": 10, "id_level1": 3, "id_pac1": 2}]


data_students = [{"name_stu": "Catalina", "last1_stu": "de", "last2_stu": "Aragón", "DNI_stu": "12345678J", 
                  "birth_date": "1973-02-04", "age_stu": 50, "tel_stu": "98765432", "mail_stu": "catalina-aragon@hotmail.com", 
                  "active_stu": True, "fam_discount": False}]


data_students_classes = [{"id_stu1": 1, "id_cla_level1": 3, "registration_date": "2023-03-01", "active_stu_cla": True},
                         {"id_stu1": 1, "id_cla_level1": 4, "registration_date": "2023-03-01", "active_stu_cla": True},
                         {"id_stu1": 1, "id_cla_level1": 5, "registration_date": "2023-03-01", "active_stu_cla": True},
                         {"id_stu1": 1, "id_cla_level1": 8, "registration_date": "2023-03-01", "active_stu_cla": True},
                         {"id_stu1": 1, "id_cla_level1": 17, "registration_date": "2023-03-01", "active_stu_cla": True},
                         {"id_stu1": 1, "id_cla_level1": 10, "registration_date": "2023-03-01", "active_stu_cla": True}]