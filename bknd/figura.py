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

    def verificar_sobreposicoes(self):
        i = 0
        tam = len(self.formas)
        while(i < tam - 1):

            j = i + 1
            while(j < tam):
                self.verificar_sobreposicao(self.formas[i], self.formas[j])
                j += 1
        
            i += 1
    
    def verificar_sobreposicao(self, retangulo1, retangulo2):
        cx1max, cx1min = retangulo1.cx + retangulo1.base/2, retangulo1.cx - retangulo1.base/2
        cy1max, cy1min = retangulo1.cy + retangulo1.altura/2, retangulo1.cy - retangulo1.altura/2
        cx2max, cx2min = retangulo2.cx + retangulo2.base/2, retangulo2.cx - retangulo2.base/2
        cy2max, cy2min = retangulo2.cy + retangulo2.altura/2, retangulo2.cy - retangulo2.altura/2

        cyCorrecao, cxCorrecao = 0, 0

        base_sobreposta = 0

        if(cx1max <= cx2max and cx1min >= cx2min):
            base_sobreposta = retangulo1.base
            cxCorrecao = retangulo1.cx

        if(cx1max >= cx2max and cx1min <= cx2min):
            base_sobreposta = retangulo2.base
            cxCorrecao = retangulo2.cx

        if(cx1max > cx2max and cx1min >= cx2min):
            base_sobreposta = cx2max - cx1min
            cxCorrecao = cx1min + base_sobreposta / 2

        if(cx1max < cx2max and cx1min <= cx2min):
            base_sobreposta = cx1max - cx2min
            cxCorrecao = cx2min + base_sobreposta / 2
        
        altura_sobreposta = 0

        if(cy1max <= cy2max and cy1min >= cy2min):
            altura_sobreposta = retangulo1.altura
            cyCorrecao = retangulo1.cy

        if(cy1max >= cy2max and cy1min <= cy2min):
            altura_sobreposta = retangulo2.altura
            cyCorrecao = retangulo2.cy

        if(cy1max > cy2max and cy1min >= cy2min):
            altura_sobreposta = cy2max - cy1min
            cyCorrecao = cy1min + altura_sobreposta / 2

        if(cy1max < cy2max and cy1min <= cy2min):
            altura_sobreposta = cy1max - cy2min
            cyCorrecao = cy2min + altura_sobreposta / 2
        

        print(f'Base sopreposta: {base_sobreposta}\nAltura sobreposta: {altura_sobreposta}')
        if(base_sobreposta * altura_sobreposta != 0):
            print('Houve uma sobreposição')
            self.adicionar_forma(Retangulo(base_sobreposta, altura_sobreposta * -1, cxCorrecao, cyCorrecao))