from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIViews feature"""
        an_apiview = [
            'uses HTTP method as functions (get, post, patch, put, delete)',
            'Is similar to traditional Django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
    
        return Response({'message': 'hello!', 'an_apiview': an_apiview})
