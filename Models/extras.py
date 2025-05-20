from sqlalchemy import Column, ForeignKey, Integer, String
from Data.connection_db import Base, session



class Extras(Base):

    __tablename__ = "invitados_adicionales"
   
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_invitado = Column(String(36), ForeignKey("invitados.id"), nullable=False)
    nombre = Column(String, nullable=False)


    def find_all():
        try:
            response = session.query(Extras).all()
            return response
        except Exception as e:
            return e
        finally:
            session.close()

        
    def find_by_id(id):
        try:
            response = session.query(Extras).filter(Extras.id == id).first()
            return response
        except Exception as e:
            return e
        finally:
            session.close()



    def find_by_filter(**kwargs):
        try:
            response = session.query(Extras).filter_by(**kwargs).all()
            return response
        except Exception as e:
            return e
        finally:
            session.close()
        

    def create(**kwargs):
        try:
            response = Extras(**kwargs)
            session.add(response)
            session.commit()
            return response
        except Exception as e:
            return e
        finally:
            session.close()


    def update(**kwargs):
        try:
            response = session.query(Extras).filter(Extras.id == kwargs["id"]).update(kwargs)
            session.commit()
            return response
        except Exception as e:
            return e
        finally:
            session.close()


    def delete_by_filter(**kwargs):
        try:
            response = session.query(Extras).filter_by(**kwargs).delete()
            session.commit()
            return response
        except Exception as e:
            return e
        finally:
            session.close()