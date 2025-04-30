from shapely.geometry import box
from shapely.ops import unary_union
from shapely.geometry import Polygon
from shapely.geometry.base import BaseGeometry
from shapely.geometry import MultiPolygon
import numpy as np

from .geometria import Geometria
from .retangulo import Retangulo

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
            momentos = [Figura(p).momento_inercia(eixo, eixo_coordenada) for p in self.completa.geoms]
            return sum(momentos)

        x, y = self.completa.exterior.coords.xy
        x = np.array(x)
        y = np.array(y)

        if eixo == 'x':
            y = y - eixo_coordenada
        elif eixo == 'y':
            x = x - eixo_coordenada

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

        return I
    
    def momento_polar(self, eixo_coordenada=0.0):
        return self.momento_inercia('x', eixo_coordenada) + self.momento_inercia('y', eixo_coordenada)
    
    def produto_inercia(self, eixo_coordenada_x = 0.0, eixo_coordenada_y = 0.0):
        if not isinstance(self.completa, Polygon):
            produtos = []
            for p in self.completa.geoms:
                resultado = Figura([[
                    (p.bounds[2] - p.bounds[0]),
                    (p.bounds[3] - p.bounds[1]),
                    p.centroid.x,
                    p.centroid.y]]).produto_inercia(eixo_coordenada_x, eixo_coordenada_y)
                produtos.append(resultado)
                    
            return sum(produtos)
        
        coords = list(self.completa.exterior.coords)
        soma_orient = 0
        for i in range(len(coords) - 1):
            soma_orient += (coords[i+1][0] - coords[i][0]) * (coords[i+1][1] + coords[i][1])
        if soma_orient > 0:  # sentido horário - inverter pq ele me retorna coordenadas de analise em sentido anti-horário, o que favoreceu em erro de sinal 
            coords = coords[::-1]

        x = np.array([c[0] for c in coords])
        y = np.array([c[1] for c in coords])

        #x, y = self.completa.exterior.coords.xy
        #x = np.array(x)
        #y = np.array(y)

        Ixy = 0
        for i in range(len(x) - 1):
            xi, yi = x[i], y[i]
            xi1, yi1 = x[i+1], y[i+1]
            det = xi * yi1 - xi1 * yi
            termo = (xi * yi1 + 2 * xi * yi + 2 * xi1 * yi1 + xi1 * yi) 
            Ixy +=  termo * det
        Ixy = Ixy * 1/24
        #Ixy = abs(Ixy * 1/24) #* (-1) Outro fator que foi influenciável


        c = self.completa.centroid
        A = self.completa.area
        if eixo_coordenada_x != 0 or eixo_coordenada_y !=0:
            dx = eixo_coordenada_x - c.x
            dy = eixo_coordenada_y - c.y
            Ixy = 0
            Ixy += A * dx * dy
        
        return Ixy
