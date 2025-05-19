from sqlalchemy import Column, ForeignKey, Boolean, UUID
from sqlalchemy.types import Integer, String
from Data.connection_db import Base, session



class Members(Base):

    __tablename__ = "miembros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_invitado = Column(String(36), ForeignKey("invitados.id"), nullable=False)
    nombre = Column(String, nullable=False)
    asistira = Column(Boolean, nullable=False)


    def find_all():
        try:
            response = session.query(Members).all()
            return response
        except Exception as e:
            return e
        finally:
            session.close()



    def find_by_id(id):
        try:
            response = session.query(Members).filter(Members.id == id).first()
            return response
        except Exception as e:
            return e
        finally:
            session.close()


    def update(**kwargs):
        try:
            response = session.query(Members).filter(Members.id == kwargs["id"]).update(kwargs)
            session.commit()
            return response
        except Exception as e:
            return e
        finally:
            session.close()