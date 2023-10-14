from django.shortcuts import render
from .serializers import VagaSerializer
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class VagaList(APIView):
    def post(self, request):
        try:
            serializer = VagaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
