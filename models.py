from sqlalchemy import Column, String, create_engine, Integer, Float, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from reference import BASE_DIR, AssetsCategory

_base = declarative_base()
_database_name = 'test.db'
_engine = create_engine(f"sqlite:///{BASE_DIR.joinpath(_database_name)}", echo=False)


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


_base.metadata.bind = _engine
_base.metadata.create_all()
_session = sessionmaker(bind=_engine)

session = _session()


def sum_assets():
    return session.query(func.sum(Assets.balance)).scalar()


def sum_debt():
    return session.query(func.sum(Debt.balance)).scalar()


def sum_income():
    return session.query(func.sum(Income.number)).scalar()


def sum_expenses():
    return session.query(func.sum(Expenses.number)).scalar()
