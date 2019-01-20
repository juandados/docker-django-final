from django.shortcuts import render
from rest_framework import views
from cuentas.models import Person, Cuenta
from rest_framework.response import Response
from cuentas.serializers import PersonSerializer, CuentaSerializer

#class AddPersonView(views.APIView):
#    def post(self, request, *args, **kwargs):
#        try:
#            id_type = request.data.get('id_type')
#            id_number = request.data.get('id_number')
#            name = request.data.get('name')
#            salary = request.data.get('salary')
#            person = Person(id_type=id_type, id_number=id_number, name=name, salary=salary)
#            person.save()
#            return Response("se agrego la persona")
#        except:
#            return Response("error")

class AddPersonView(views.APIView):
    def post(self, request, *args, **kwargs):
        try:
            person_serializer = PersonSerializer(data=request.data)
            if person_serializer.is_valid():
                person_serializer.save()
                return Response("se agrego la persona")
            else:
                return Response(person_serializer.errors)
        except Exception as e:
                return Response(e.args)

#class AddCuentaView(views.APIView):
#    def post(self, request, *args, **kwargs):
#        # Capturando datos
#        person_name = request.data.get('person_name')
#        person = Person.objects.get(name=person_name)
#        numero_cuenta = request.data.get('numero_cuenta')
#        tipo = request.data.get('tipo')
#        banco = request.data.get('banco') 
#        # Creando cuenta
#        cuenta = Cuenta(person=person, numero_cuenta=numero_cuenta, tipo=tipo, banco=banco)
#        cuenta.save()
#        return Response("se agrego la cuenta")

class AddCuentaView(views.APIView):
    def post(self, request, *args, **kwargs):
        person_name = request.data.get('person_name')
        person = Person.objects.get(name=person_name)
        cuenta_serializer = CuentaSerializer(data=request.data)
        if cuenta_serializer.is_valid():
            cuenta_serializer.save(person=person)
            return Response("se creo cuenta")
        else:
            return Response(cuenta_serializer.errors)

class ListCuentasView(views.APIView):
    def get(self, request, *args, **kwargs):
        cuentas_query_set = Cuenta.objects.all() 
        cuentas_response = [{"person_name": cuenta.person.name, 
                    "numero_cuenta": cuenta.numero_cuenta,
                    "tipo": cuenta.tipo, 
                    "banco": cuenta.banco} 
                   for cuenta in cuentas_query_set]
        return Response(cuentas_response)



























