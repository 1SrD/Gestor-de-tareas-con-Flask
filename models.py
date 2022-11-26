from sqlalchemy import Column, Integer, String, Boolean, Date
import db

class Tarea (db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) #Automaticamente esta PK se convertira en SERIAL (AUTOINCREMENT)
    contenido = Column(String(200), nullable=False) #No se puede crear una persona sin nombre
    hecha = Column(Boolean)
    fecha = Column(Date)

    def __init__(self, contenido, hecha, fecha):
        self.contenido = contenido
        self.hecha = hecha
        self.fecha = fecha

    def __fechaFormateada__(self):
        fechaFormateada = self.fecha.strftime('%d-%m-%Y')
        return "{}".format(fechaFormateada)

    def __str__(self):
        return "Tarea({}: {}, {}, ({}))".format(self.id, self.contenido, self.hecha, self.fecha)


