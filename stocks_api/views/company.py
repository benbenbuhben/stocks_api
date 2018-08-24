from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIView(APIViewSet):

    def retrieve(self, request, id=None):
        """
        """
        message = 'Here is the info for Ticker Symbol: {}'.format(id)
        return Response(json={'company': message}, status=200)

