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
        genai.configure()
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Baseado no seguinte prognóstico e condição de saúde do usuário relacionada ao fígado, por favor, indique as melhores opções de tratamento e recomendações médicas detalhadas. Prognóstico do usuário:"+data)
        return Response({'tratamento': response.text},status=status.HTTP_200_OK)