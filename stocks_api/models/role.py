from .meta import Base
from .associations import roles_association
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)


class AccountRole(Base):
    """
    """
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    accounts = relationship('Account', secondary=roles_association, back_populates='roles')



