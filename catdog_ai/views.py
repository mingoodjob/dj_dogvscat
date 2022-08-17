from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from catdog_ai.serializers import PetSerializer

class PetView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Pet!"}, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
