from django.shortcuts import render
from .serializers import VagaSerializer
from django.http import JsonResponse
from .models import Vaga

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class VagaList(APIView):
    def get(self, request):           # Exibir todos registros do nosso banco de dados
        try:            
            lista_vagas = Vaga.objects.all()
            serializer = VagaSerializer(lista_vagas, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):         # Insire um  registro no banco de dados
        try:
            serializer = VagaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class VagaDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga)
            return Response(serializer.data)
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
