from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import ExchangeSerializer
from .models import Exchange

@permission_classes([IsAuthenticated])
class ExchangesList(APIView):
    def get(self, request, format=None):
        exchanges = Exchange.objects.filter(user=self.request.user)
        serializer = ExchangeSerializer(exchanges, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExchangeSerializer(data={"valute1" : self.request.data["valute1"], "valute2" : self.request.data["valute2"], "user" : self.request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        exchanges = Exchange.objects.filter(user=self.request.user, valute1=self.request.data["valute1"], valute2=self.request.data["valute2"])
        print(exchanges)
        exchanges.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
