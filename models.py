from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from reference import BASE_DIR, AssetsCategory

_database_name = 'test.db'
_engine = create_engine(f"sqlite:///{BASE_DIR.joinpath(_database_name)}", echo=False)
_base = declarative_base()


class Assets(_base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project = Column(String(20), default='')
    category = Column(Integer, default=AssetsCategory.STATIC)
    balance = Column(Float, default=0.0)


class Debt(_base):
    __tablename__ = 'debt'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project = Column(String(20), default='')
    balance = Column(Float, default=0.0)


class Income(_base):
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project = Column(String(20), default='')
    number = Column(Float, default=0.0)


class Expenses(_base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project = Column(String(20), default='')
    number = Column(Float, default='')


_session = sessionmaker(bind=_engine)

session = _session()