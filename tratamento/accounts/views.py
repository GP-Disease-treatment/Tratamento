from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
import google.generativeai as genai

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        cpf = request.data.get('CPF')
        password = request.data.get('password')

        user = authenticate(request, CPF=cpf, password=password)
        if user is not None:
            type = User.objects.values('type').get(CPF=cpf).get('type')
            if type != 'Captador':
                token = RefreshToken.for_user(user).access_token
                return Response({'message': 'Authenticated successfully', 'token': f'{token}', 'type': type}, status=status.HTTP_200_OK)
            else:
                return Response({'error:': 'User without permission to access system.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'There is no user with these access credentials'}, status=status.HTTP_404_NOT_FOUND)



class GPTView(APIView):
    def post(self, request):
        data = request.data.get('prognostico')
        genai.configure()
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Baseado no seguinte prognóstico e condição de saúde do usuário relacionada ao fígado, por favor, indique as melhores opções de tratamento e recomendações médicas detalhadas. Prognóstico do usuário:"+data)
        return Response({'tratamento': response.text},status=status.HTTP_200_OK)