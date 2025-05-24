from sqlalchemy import Column, Integer, String
from Data.connection_db import Base, session


class UsersAdmin(Base):
    
    __tablename__ = "users_admin"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    disabled = Column(Integer, default=0)


    def find_by_filter(**kwargs):
        try:
            response = session.query(UsersAdmin).filter_by(**kwargs).first()
            return response
        except Exception as e:
            return e
        finally:
            session.close()