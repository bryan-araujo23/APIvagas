from django.urls import path
from .views import VagaList

urlpatterns = [
    path('vagas', VagaList.as_view()),
]
