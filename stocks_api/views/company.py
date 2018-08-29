from pyramid_restful.viewsets import APIViewSet
from pyramid.view import view_config
from pyramid.response import Response
import requests

# This is how we hit the 3rd party API in class, but based on my interpretation of the lab instructions, I also put this functionality below in the /api/v1/company/{symbol} route
@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """Lookup method that's probably not necessary because I incorporated the same functinoality below.
    """
    url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(request.matchdict['symbol'])
    response = requests.get(url)
    return Response(json=response.json(), status=200)


class CompanyAPIView(APIViewSet):

    def retrieve(self, request, id=None):
        """Hit IEX API to retrieve info one one stock.
        """
        url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(id)
        response = requests.get(url)
        return Response(json=response.json(), status=200)
        # message = 'Here is the info for Ticker Symbol: {}'.format(id)
        # return Response(json={'company': message}, status=200)

