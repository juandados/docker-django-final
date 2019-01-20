from django.test import TestCase
from cuentas.utils import EstudioCredito
from cuentas.models import Person, Cuenta
from cuentas.factories import PersonFactory

class EstudioCreditoTest(TestCase):
    def setUp(self):
        self.persona = PersonFactory()

    def test_capacidad_pago_retorna_30_porciento(self):
        cuenta = Cuenta(person=self.persona, tipo="ahorros", banco="davivienda", numero_cuenta="12")
        cuenta.save()
        estudio_credito = EstudioCredito(persona=self.persona, cuenta=cuenta)
        capacidad_pago = estudio_credito.capacidad_pago()
        self.assertEqual(capacidad_pago, 300)

    def test_calificacion_crediticia_retorna_1_cuando_banco_inicia_d(self):
        cuenta = Cuenta(person=self.persona, tipo="ahorros", banco="davivienda", numero_cuenta="12")
        cuenta.save()
        estudio_credito = EstudioCredito(persona=self.persona, cuenta=cuenta)
        calificacion_crediticia = estudio_credito.calificacion_crediticia()
        self.assertEqual(calificacion_crediticia, 1)

    def test_calificacion_crediticia_retorna_2_cuando_banco_inicia_b(self):
        cuenta = Cuenta(person=self.persona, tipo="ahorros", banco="bancolombia", numero_cuenta="12")
        cuenta.save()
        estudio_credito = EstudioCredito(persona=self.persona, cuenta=cuenta)
        calificacion_crediticia = estudio_credito.calificacion_crediticia()
        self.assertEqual(calificacion_crediticia, 2)

    def test_calificacion_crediticia_retorna_0_cuando_banco_no_inicia_con_d_o_b(self):
        cuenta = Cuenta(person=self.persona, tipo="ahorros", banco="falabella", numero_cuenta="12")
        cuenta.save()
        estudio_credito = EstudioCredito(persona=self.persona, cuenta=cuenta)
        calificacion_crediticia = estudio_credito.calificacion_crediticia()
        self.assertEqual(calificacion_crediticia, 0)
