from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore

class HelloApiView(APIView):
    """Test API VIEW"""

    def get(self,request,format = None):
        """Returns a lst of alphabets"""
        li = ['a','b','c','d']

        return Response({'message':'Success!','list':li})