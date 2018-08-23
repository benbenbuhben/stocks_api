from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIView(APIViewSet):

    def retrieve(self, request, id):
        company_symbol = id
        return Response(json={'company': f'''Here's the info for Ticker Symbol: {company_symbol}'''}, status=200)

