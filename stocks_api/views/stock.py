from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import json


class StockAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        """
        """
        unique_id = id
        message = 'Here\'s the id for that company... {}'.format(unique_id)
        return Response(json={'company': message}, status=200)

    def create(self, request):
        """
        """
        my_database_is_a_variable = request.body
        name = json.loads(my_database_is_a_variable)['name']
        symbol = json.loads(my_database_is_a_variable)['symbol']
        portfolio_id = json.loads(my_database_is_a_variable)['portfolio_id']
        message = 'Stock record for Portfolio ID#{} created for {} (Ticker Symbol: {})'.format(portfolio_id, name, symbol)
        return Response(json={'message': message}, status=201)

    def destroy(self, request, id):
        """
        """
        return Response(json={'message': 'Successfully deleted the record for that id'}, status=204)
