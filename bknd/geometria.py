from abc import ABC
from abc import abstractmethod

class Geometria(ABC):
    def __init__(self, operacao = 1):
        self.operacao = operacao

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def centroide(self):
        pass

    def area_com_sinal(self):
        return self.operacao*self.area()
    
    def centroide_vezes_area(self):
        cx, cy = self.centroide()
        #cy = self.centroide() gerando erro pq é tupla
        Area = self.area_com_sinal()

        return cx * Area, cy * Area