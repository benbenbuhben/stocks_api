from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class PortfolioAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        """
        """
        unique_id = id
        message = 'The id you sent was {}'.format(unique_id)
        return Response(json={'message': message}, status=200)

