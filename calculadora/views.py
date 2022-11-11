from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework import status

class Adicao(APIView):
    def get(self, request: HttpRequest, a: int, b: int) -> HttpResponse:
        r = a + b
        return Response(data={"resultado": str(r)}, status=status.HTTP_200_OK)

class Substituicao(APIView):
    def get(self, request: HttpRequest, a: int, b: int) -> HttpResponse:
        r = a - b
        return Response(data={"resultado": str(r)}, status=status.HTTP_200_OK)
    
class Multiplicacao(APIView):
    def get(self, request: HttpRequest, a: int, b: int) -> HttpResponse:
        r = a * b
        return Response(data={"resultado": str(r)}, status=status.HTTP_200_OK)

class Divisao(APIView):
    def get(self, request: HttpRequest, a: int, b: int) -> HttpResponse:
        if b != 0:
            r = a / b
            return Response(data={"resultado": str(r)}, status=status.HTTP_200_OK)
        else:
            return Response(data={'Erro': "Não é possível fazer divisão por zero."}, status=status.HTTP_400_BAD_REQUEST)