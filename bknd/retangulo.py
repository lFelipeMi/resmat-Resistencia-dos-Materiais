from .forma_geometrica import FormaGeometrica
from shapely.geometry import box
from shapely.ops import unary_union
from shapely.geometry import Polygon
import numpy as np

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura, cx, cy):
        #centroide é uma lista [x, y]
        self.retangulo = box(cx - base/2, cy - altura/2, cx + base/2, cy + altura/2)

    def momento(self, forma:'Retangulo'):
        return forma.momento_em('x') + forma.momento_em('y')
    
    def momento_em(self, eixo):
        if(eixo == 'x'):
            return (self.base * (self.altura ** 3)/12) + self.area * self.cy ** 2 #Distancia do eixo Y
        return (self.altura * (self.base ** 3)/12) + self.area * self.cx ** 2 #Distancia do eixo X
    
