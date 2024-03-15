from evento import Evento

class EventoParrillada(Evento):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_detalle(self):
        return f"Evento Parrillada: {self.nombre}, Precio: {self.precio}"