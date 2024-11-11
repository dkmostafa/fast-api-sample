import os
from dotenv import load_dotenv

from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker, DeclarativeBase)

load_dotenv()

db_url = os.getenv('db_url')

engine = create_engine(db_url)


def get_session():
    session = sessionmaker(bind=engine, expire_on_commit=False)
    return session()


class Base(DeclarativeBase):
    ...
