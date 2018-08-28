from ..models.schemas import PortfolioSchema
from ..models import Portfolio
from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import json


class PortfolioAPIView(APIViewSet):
    def create(self, request):
        """
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        # Placeholder for if conditional at ~27:00, not sure if needed here

        try:
            portfolio = Portfolio.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Portfolio already exists.', status=409)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json=data, status=201)

    def retrieve(self, request, id=None):
        """
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

