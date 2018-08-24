from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIView(APIViewSet):

    def retrieve(self, request, id=None):
        """
        """
        return Response(json={'company': f'''Here's the info for Ticker Symbol: {id}'''}, status=200)

