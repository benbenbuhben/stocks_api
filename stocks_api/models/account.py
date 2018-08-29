from .associations import roles_association
from .portfolio import Portfolio
from datetime import datetime as dt
from .meta import Base
from .role import AccountRole
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    DateTime,
)


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    # locations = relationship(WeatherLocation, back_populates='account')  # Change this one
    portfolios = relationship(Portfolio, back_populates='accounts')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email, password=None):
        self.email = email
        self.password = password  # NOTE: This is unsafe and will be fixed.

    @classmethod
    def new(cls, request, email=None, password=None):
        """Register a new user
        """
        if not request.dbsession:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        # TODO: Assign roles to new user

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """Validate that user exists and they are who they say they are
        """
        # TODO: Complete this tomorrow as part of the login process
        pass
