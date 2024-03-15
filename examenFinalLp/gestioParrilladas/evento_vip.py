from evento import Evento

class EventoVIP(Evento):
    def __init__(self, nombre, precio, beneficios):
        self.nombre = nombre
        self.precio = precio
        self.beneficios = beneficios

    def mostrar_detalle(self):
        return f"Evento VIP: {self.nombre}, Precio: {self.precio}, Beneficios: {self.beneficios}"