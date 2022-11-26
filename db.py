from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# El engine permite a SQLAlchemy comunicarse con la base de datos

engine = create_engine("sqlite:///database/tareas.db", connect_args={"check_same_thread": False}) #Connect_arg conexiones simultaneas

#Ahora creamos la sesion, lo que nos permite realizar transacciones
Session = sessionmaker(bind=engine)
session = Session()

#Ahora vamos al fichero models.py y creamos nuestro modelo (nuestra clase) y la siguiente instruccion
#se encarga de mapear la clase o clases creadas y vincularlas a la base de datos
Base = declarative_base()