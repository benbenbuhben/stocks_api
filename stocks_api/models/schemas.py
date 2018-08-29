from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio, Stock, Account, AccountRole


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio


class StockSchema(ModelSchema):
    class Meta:
        model = Stock
