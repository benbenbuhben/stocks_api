from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import json


class AuthAPIView(APIViewSet):
    def create(self, request):
        """POST method to api/v1/auth endpoint. Currently, no database setup.
        """
        my_database_is_a_variable = request.body
        username = json.loads(my_database_is_a_variable)['username']
        message = 'Created a record for {}!'.format(username)
        return Response(json={'message': message}, status=201)
