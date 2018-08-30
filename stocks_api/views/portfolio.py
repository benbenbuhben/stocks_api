from ..models.schemas import PortfolioSchema
from ..models import Portfolio
from ..models import Account
from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import json


class PortfolioAPIView(APIViewSet):
    def create(self, request, portfolio_id=None):
        """Post method to create new portfolio
        """
        try:
            kwargs = json.loads(request.body)
            # kwargs['account_id'] = portfolio_id
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        # I did it by the above way, he did it the below way...
        # What are we doing here? We're checking if the user is authenticated. If so, get the account and add it to the kwargs (this will become the foreign key to the corresponding account on the Portfolio table).
        if request.authenticated_userid:
            account = Account.one(request, request.authenticated_userid)
            kwargs['account_id'] = account.id
        try:
            portfolio = Portfolio.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Portfolio already exists.', status=409)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json=data, status=201)

    def retrieve(self, request, id=None):
        """Fetch one from database by id.
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            portfolio = Portfolio.one(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json={'message': data}, status=200)

