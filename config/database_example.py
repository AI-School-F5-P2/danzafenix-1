#from sqlalchemy import create_engine, MetaData
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

#Se crea la conexión a la base de datos
#engine = create_engine("mysql+pymysql://UserExample:PasswordExample@localhost:3306/NombreBaseDatos")

#meta_data = MetaData()

#Los cambios en la base de datos deben hacerse manualmente pues autocommit = False
#Session = sessionmaker(autocommit = False, bind = engine)

#Se crea una instancia de declarative_base() para que los Modelos/Tablas puedan heredar de esta clase
#Base = declarative_base()