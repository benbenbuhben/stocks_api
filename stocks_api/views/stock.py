from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import json


class StockAPIView(APIViewSet):
    def create(self, request):
        my_database_is_a_variable = request.body
        name = json.loads(my_database_is_a_variable)['name']
        symbol = json.loads(my_database_is_a_variable)['symbol']
        portfolio_id = json.loads(my_database_is_a_variable)['portfolio_id']
        return Response(json=f'''{{'message': 'Stock record for Portfolio ID#{portfolio_id} created for {name} (Ticker Symbol: {symbol})'}}''', status=201)

