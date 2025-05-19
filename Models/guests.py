from sqlalchemy import Column, Integer, String, UUID
from Data.connection_db import Base, session
import uuid

from Models.members import Members


class Guest(Base):

    __tablename__ = "invitados"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tipo_invitado = Column(String, nullable=False, default="Familia")
    nombre = Column(String, nullable=False)
    num_integrantes = Column(Integer, nullable=False,  default=1)
    menores = Column(Integer, nullable=False, default=0)
    adicionales = Column(Integer, nullable=False, default=0)
    telefono = Column(String(10), default=None)
    

    def find_all():
        try:
            response = session.query(Guest).all()
            return response
        except Exception as e:
            return e
        finally:
            session.close()


    def find_by_id(id):
        try:
            response = session.query(Guest).filter(Guest.id == id).first()
            return response
        except Exception as e:
            return e
        finally:
            session.close()


    def get_members(id):
        try:
            response = session.query(Members).filter(Members.id_invitado == id).all()
            return response
        except Exception as e:
            return e
        finally:
            session.close()


    def update(**kwargs):
        try:
            response = session.query(Guest).filter(Guest.id == kwargs["id"]).update(kwargs)
            session.commit()
            return response
        except Exception as e:
            return e
        finally:
            session.close()