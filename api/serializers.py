# Aqui vamos mapear como as vagas estão definidas


from rest_framework import serializers
from api.models import Vaga


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = [ 'id', 'titulo', 'descricao', 'salario', 'tipo_contrato', 'stauts' ]
