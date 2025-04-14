class FormaGeometrica():
    def __init__(self):
        pass

    def momento(self): 
        pass

    def momento_em(self):
        pass

    def centroide_figura(self, formas):
        area_total = 0
        for forma in formas:
            area_total += forma.area

        return [self.centroide_figura_em(formas, 'x', area_total), self.centroide_figura_em(formas, 'y', area_total)]


    # uma lista de formas geométricas  
    def centroide_figura_em(formas, eixo, area_total):
        somatorio_Distancia_Area = 0
        eixo_int = 0 if eixo == 'x' else 1
        for forma in formas:
            somatorio_Distancia_Area += forma.centroide[eixo_int] * forma.area

        return somatorio_Distancia_Area/area_total