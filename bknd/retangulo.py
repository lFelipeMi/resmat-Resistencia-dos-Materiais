from shapely.geometry import box
from shapely.ops import unary_union
from shapely.geometry import Polygon
import numpy as np

def criar_retangulo(b, h, cx, cy):
    return box(cx - b/2, cy - h/2, cx + b/2, cy + h/2)

class Figura():
    def __init__(self, retangulos):        
        self.naoSeiDoQueChamar = retangulos

    @property
    def naoSeiDoQueChamar(self):
        return self.__naoSeiDoQueChamar
    
    @naoSeiDoQueChamar.setter
    def naoSeiDoQueChamar(self, retangulos):
        if isinstance(retangulos, Polygon):
            self.__naoSeiDoQueChamar = retangulos
        else:
            formas_da_figura = [criar_retangulo(b, h, cx, cy) for (b, h, cx, cy) in retangulos]
            self.__naoSeiDoQueChamar = unary_union(formas_da_figura)

    @property
    def area(self):
        return self.naoSeiDoQueChamar.area if self.naoSeiDoQueChamar else 0

    def momento_inercia(self, eixo='x', eixo_coordenada=0.0):
        if not isinstance(self.naoSeiDoQueChamar, Polygon):
            momentos = [p.momento_inercia(eixo, eixo_coordenada) for p in self.naoSeiDoQueChamar.geoms]
            return sum(momentos)

        x, y = self.naoSeiDoQueChamar.exterior.coords.xy
        x = np.array(x)
        y = np.array(y)
        I = 0
        for i in range(len(x) - 1):
            xi, yi = x[i], y[i]
            xi1, yi1 = x[i+1], y[i+1]
            common = xi * yi1 - xi1 * yi
            if eixo == 'x':
                I += (yi**2 + yi*yi1 + yi1**2) * common
            elif eixo == 'y':
                I += (xi**2 + xi*xi1 + xi1**2) * common
        I *= 1/12
        I = abs(I)

        # Teorema dos Eixos Paralelos para eixo arbitrário
        c = self.naoSeiDoQueChamar.centroid
        A = self.naoSeiDoQueChamar.area
        d = abs((c.y - eixo_coordenada) if eixo == 'x' else (c.x - eixo_coordenada))
        I += A * d**2

        return I
    
    def momento_polar(self, eixo_coordenada=0.0):
        Ip = self.momento_inercia('x', eixo_coordenada) + self.momento_inercia('y', eixo_coordenada)