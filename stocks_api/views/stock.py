from ..models.schemas import StockSchema
from ..models import Stock
from ..models import Portfolio
from ..models import Account
from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import requests
import json


class StockAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        """Fetch one method to retrieve a specified stock from database
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            stock = Stock.one(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        schema = StockSchema()
        data = schema.dump(stock).data

        return Response(json={'message': data}, status=200)

    def create(self, request):
        """Post method to put a new stock in the database. Need to hit IEX API first and craft request to database accordingly.
        """
        try:
            # Add 3P API call here with parsed request. Make the response the kwargs below.
            symbol = json.loads(request.body)['symbol']
            # portfolio_id = json.loads(request.body)['portfolio_id']
            url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(symbol)
            response = requests.get(url)
            kwargs = response.json()
            del kwargs['tags']
            # kwargs['portfolio_id'] = portfolio_id  # Delete?

        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        # Should I delete the way I was doing it before? We would want to use the
        if request.authenticated_userid:
            # import pdb; pdb.set_trace()
            account = Account.one(request, request.authenticated_userid)
            portfolio = Portfolio.oneByKwarg(request, account.id) #  Some logic to extract portfolio id by account_id
            kwargs['portfolio_id'] = portfolio.id

        try:
            print(kwargs)
            stock = Stock.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Stock already exists.', status=409)

        schema = StockSchema()
        data = schema.dump(stock).data

        return Response(json=data, status=201)

        # message = 'Stock record for Portfolio ID#{} created for {} (Ticker Symbol: {})'.format(portfolio_id, name, symbol)
        # return Response(json={'message': message}, status=201)

    def destroy(self, request, id):
        """Delete method to remove stock from the database, by id.
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            Stock.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)
