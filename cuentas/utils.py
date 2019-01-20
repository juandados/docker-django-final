class EstudioCredito:
    def __init__(self, persona, cuenta):
        self.persona = persona
        self.cuenta = cuenta

    def capacidad_pago(self):
        capacidad_pago = self.persona.salary * 0.3
        return capacidad_pago

    def calificacion_crediticia(self):
        calificaciones_dict = {"d":1, "b":2}
        banco = self.cuenta.banco
        inicial = banco[0]
        calificacion = calificaciones_dict.get(inicial, 0)
        return calificacion
