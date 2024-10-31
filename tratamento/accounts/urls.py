from django.urls import path
from .views import TratamentoView

urlpatterns = [
    path('treatment/', TratamentoView.as_view(), name="treatment"),
]