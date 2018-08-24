from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import json


class StockAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        """
        """
        unique_id = id
        return Response(json={'company': f'''Here's the id for that company... {unique_id}'''}, status=200)

    def create(self, request):
        """
        """
        my_database_is_a_variable = request.body
        name = json.loads(my_database_is_a_variable)['name']
        symbol = json.loads(my_database_is_a_variable)['symbol']
        portfolio_id = json.loads(my_database_is_a_variable)['portfolio_id']
        return Response(json={'message': f'''Stock record for Portfolio ID#{portfolio_id} created for {name} (Ticker Symbol: {symbol})'''}, status=201)

    def destroy(self, request, id):
        """
        """
        return Response(json={'message': 'Successfully deleted the record for ID#{id}'}, status=204)
