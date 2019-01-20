import factory
from faker import Faker
import datetime, pytz
from cuentas.models import Person, Cuenta

class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person
    id_type = 'CC'
    id_number = '19211'
    name = factory.Sequence(lambda n: "{}{}".format(Faker().name(), n)) 
    salary = 1000

class CuentaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cuenta
    tipo="ahorros"
    banco="davivienda"
    numero_cuenta="12"
