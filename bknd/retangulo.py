from shapely.geometry import box

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
