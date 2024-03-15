from abc import ABC, abstractmethod

class Evento(ABC):
    @abstractmethod
    def mostrar_detalle(self):
        pass