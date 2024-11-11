from sqlalchemy import Column, Integer, String

from database.db_engine import Base


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    username = Column(String, unique=True, nullable=False)
