from .forma_geometrica import FormaGeometrica
from .retangulo import Retangulo 

class Figura():
    def __init__(self, lista_formas=[]):
        self.formas = lista_formas
    
    def calcular_area_total(self):
        area = 0
        for forma in self.formas:
            area += forma.area
        return area

    def adicionar_forma(self, forma):
        self.formas.append(forma)

    def momento_total(self):
        Itotal = 0
        for forma in self.formas:
            Itotal += forma.momento(forma)
        
        return Itotal
    
    def momento_em(self, eixo):
        Ieixo = 0
        for forma in self.formas:
            Ieixo += forma.momento_em(eixo)
        return Ieixo