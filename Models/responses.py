from Data.connection_db import Base, session
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, UUID
from sqlalchemy.dialects.postgresql import UUID



class Invites(Base):

    __tablename__ = "invitaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_invitado = Column(String(36), ForeignKey("invitados.id"), nullable=False)
    respuesta = Column(Boolean, nullable=False)
    asistira = Column(Boolean, default=None)
    buzon = Column(Text, default=None)
    


    def find_by_id_guest(id):
        try:
            id = str(id)
            response = session.query(Invites).filter(Invites.id_invitado == id).first()
            return response
        except Exception as e:
            return e
        finally:
            session.close()


