from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from openai import OpenAI

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
    def get(self, request):
        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "Write a haiku about recursion in programming."
                }
            ]
        )

        print(completion.choices[0].message)
        return Response(status=status.HTTP_200_OK)