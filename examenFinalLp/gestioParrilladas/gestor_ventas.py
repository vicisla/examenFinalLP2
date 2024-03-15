class GestorVentas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def mostrar_ventas(self):
        for venta in self.ventas:
            print(f"Comprador: {venta.comprador.nombre}, Evento: {venta.evento.nombre}")