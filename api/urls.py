from django.urls import path
from .views import VagaList, VagaDetalhes

urlpatterns = [
    path('vagas', VagaList.as_view()),
    path('vagas/<int:pk>', VagaDetalhes.as_view()),
]
