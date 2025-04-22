from shapely.geometry import box
from shapely.ops import unary_union
from shapely.geometry import Polygon
from shapely.geometry.base import BaseGeometry
from shapely.geometry import MultiPolygon
import numpy as np

from .geometria import Geometria

class Retangulo(Geometria):
    def __init__(self, base_b, altura_h, cx, cy, operacao=1):
        super().__init__(operacao)
        self.b = base_b
        self.h = altura_h
        self.cx = cx
        self.cy = cy
        self.box = box(cx - base_b/2, cy - altura_h/2, cx + base_b/2, cy + altura_h/2)

    def area(self):
        areaRetangulo = self.b * self.h
        return areaRetangulo
    
    def centroide(self):
        return self.cx, self.cy
    

def criar_retangulo(b, h, cx, cy):
    return box(cx - b/2, cy - h/2, cx + b/2, cy + h/2)

class Figura():
    def __init__(self, retangulos):        
        self.completa = retangulos

    @property
    def completa(self):
        return self.__completa
    
    @completa.setter
    def completa(self, retangulos):
        if isinstance(retangulos, BaseGeometry):
            self.__completa = retangulos
        else:
            formas_da_figura = [Retangulo(b, h, cx, cy).box for (b, h, cx, cy) in retangulos]
            self.__completa = unary_union(formas_da_figura)

    @property
    def area(self):
        return self.completa.area if self.completa else 0

    def momento_inercia(self, eixo='x', eixo_coordenada=0.0):
        if not isinstance(self.completa, Polygon):
            momentos = [p.momento_inercia(eixo, eixo_coordenada) for p in self.completa.geoms]
            return sum(momentos)

        x, y = self.completa.exterior.coords.xy
        x = np.array(x)
        y = np.array(y)
        I = 0
        for i in range(len(x) - 1):
            xi, yi = x[i], y[i]
            xi1, yi1 = x[i+1], y[i+1]
            det = xi * yi1 - xi1 * yi 
            if eixo == 'x':
                I += (yi**2 + yi*yi1 + yi1**2) * det
            elif eixo == 'y':
                I += (xi**2 + xi*xi1 + xi1**2) * det
        I *= 1/12
        I = abs(I)
        #print(I)

        '''
        # Teorema dos Eixos Paralelos para eixo arbitrário
        c = self.completa.centroid
        A = self.completa.area
        #print(A)
        d = abs((c.y - eixo_coordenada) if eixo == 'x' else (c.x - eixo_coordenada))
        #print(d)
        #print(A * d**2)
        I += A * d**2
        '''

        return I
    
    def momento_polar(self, eixo_coordenada=0.0):
        Ip = self.momento_inercia('x', eixo_coordenada) + self.momento_inercia('y', eixo_coordenada)
