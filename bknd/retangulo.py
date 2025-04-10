from .forma_geometrica import FormaGeometrica

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura, cx, cy):
        #centroide é uma lista [x, y]
        self.cx = cx
        self.cy = cy
        self.base = base
        self.altura = altura
        self.area = self.base * self.altura

    def momento_total(self, lista_formas):
        Itotal = 0
        for forma in lista_formas:
            Itotal += self.momento(forma)

    def momento(self, forma:'Retangulo'):
        return forma.momento_em('x') + forma.momento_em('y')
    
    def momento_em(self, eixo):
        if(eixo == 'x'):
            return (self.base * (self.altura ** 3)/12) + self.area * self.cy ** 2 #Distancia do eixo Y
        return (self.altura * (self.base ** 3)/12) + self.area * self.cx ** 2 #Distancia do eixo X
    
