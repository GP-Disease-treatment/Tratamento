from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
import google.generativeai as genai

class TratamentoView(APIView):
    def post(self, request):
        data = request.data.get('prognostico')
        pront = request.data.get('prontuario')
        genai.configure()
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("""Baseado no seguinte prognóstico e condição de saúde do usuário relacionada aDado o prognostico:"""+data+""" e o seguinte prontuário de paciente:"""+pront+""". Gere um tratamento adequado e separe em parágrafos da seguinte forma: principal tratamento, medicamentos e por fim recomendações para recuperação.
Por fim um parágrafo breve agradecendo o paciente e desejando melhoraso fígado, por favor, indique as melhores opções de tratamento e recomendações médicas detalhadas . Prognóstico do usuário:""")
        return Response({'tratamento': response.text},status=status.HTTP_200_OK)