from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class PortfolioAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        """
        """
        unique_id = id
        return Response(json={'message': f'''The id you sent was {unique_id}'''}, status=200)

