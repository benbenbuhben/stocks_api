from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)
from sqlalchemy import ForeignKey
# from .portfolio import Portfolio
from .meta import Base
from sqlalchemy.orm import relationship


class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    companyName = Column(Text)
    exchange = Column(Text)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    CEO = Column(Text)
    issueType = Column(Text)
    sector = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'), nullable=False)
    portfolios = relationship('Portfolio', back_populates='stocks')

    @classmethod
    def new(cls, request, **kwargs):
        """Method to put a new stock in the database
        """
        if request.dbsession is None:
            raise DBAPIError
        stock = cls(**kwargs)
        request.dbsession.add(stock)

        return request.dbsession.query(cls).filter(
            cls.symbol == kwargs['symbol']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        """Method to retrieve one stock from the database
        """
        if request.dbsession is None:
            raise DBAPIError
        return request.dbsession.query(cls).get(pk)

    @classmethod
    def remove(cls, request=None, pk=None):
        """Method to delete a stock from the database
        """
        if request.dbsession is None:
            raise DBAPIError
        return request.dbsession.query(cls).filter(
            cls.id == pk).delete()
