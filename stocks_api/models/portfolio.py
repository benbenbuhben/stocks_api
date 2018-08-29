from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from .stock import Stock
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)
from sqlalchemy import ForeignKey

from .meta import Base


class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())
    stocks = relationship(Stock, back_populates='portfolios')
    account_id = Column(Integer, ForeignKey('accounts.id'))
    accounts = relationship('Account', back_populates='portfolios')

    @classmethod
    def new(cls, request, **kwargs):
        """Method to create new portfolio in database
        """
        if request.dbsession is None:
            raise DBAPIError
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.name == kwargs['name']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        """Method to retrieve a portfolio by primary key
        """
        if request.dbsession is None:
            raise DBAPIError
        return request.dbsession.query(cls).get(pk)
