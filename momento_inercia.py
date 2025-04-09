class FormaGeometrica():
    def __init__(self):
        pass

    def momento(self): 
        pass

    def momento_em(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, centroide, base, altura):
        #centroide é uma lista [x, y]
        self.centroide = centroide
        self.base = base
        self.altura = altura
        self.area = self.base * self.altura

    def momento(self):
        return self.momento_em('x') + self.momento_em('y')
    
    def momento_em(self, eixo):
        if(eixo == 'x'):
            return (self.base * (self.altura ** 3)/12) * self.area * self.centroide[1] ** 2 #Distancia do eixo Y
        return (self.altura * (self.base ** 3)/12) * self.area * self.centroide[0] ** 2 #Distancia do eixo X
    
def centroide_figura(formas):
    area_total = 0
    for forma in formas:
        area_total += forma.area

    return [centroide_figura_em(formas, 'x', area_total), centroide_figura_em(formas, 'y', area_total)]

# uma lista de formas geométricas  
def centroide_figura_em(formas, eixo, area_total):
    somatorio_Distancia_Area = 0
    eixo_int = 0 if eixo == 'x' else 1
    for forma in formas:
        somatorio_Distancia_Area += forma.centroide[eixo_int] * forma.area

    return somatorio_Distancia_Area/area_total