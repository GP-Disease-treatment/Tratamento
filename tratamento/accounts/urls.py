from django.urls import path
from .views import GPTView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('gpt/', GPTView.as_view(), name="gpt"),
]