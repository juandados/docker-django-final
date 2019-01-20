from rest_framework import serializers
from cuentas.models import Person, Cuenta

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id_type', 'id_number', 'name', 'salary', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('numero_cuenta', 'tipo', 'banco', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
