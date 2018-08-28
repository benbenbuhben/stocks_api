from ..models.schemas import StockSchema
from ..models import Stock
from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import json


class StockAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        """
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
        """
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        # Placeholder for if conditional at ~27:00, not sure if needed here

        try:
            stock = Stock.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Stock already exists.', status=409)

        schema = StockSchema()
        data = schema.dump(stock).data

        return Response(json=data, status=201)

        # message = 'Stock record for Portfolio ID#{} created for {} (Ticker Symbol: {})'.format(portfolio_id, name, symbol)
        # return Response(json={'message': message}, status=201)

    def destroy(self, request, id):
        """
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            Stock.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)
