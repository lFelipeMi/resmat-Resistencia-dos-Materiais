canto_Superior_Esquerdo = 1
canto_Superior_Medio = 2
canto_Superior_Direito = 3
meio_Esquerdo = 4
centro = 5 # Maior relevancia
meio_Direito = 6
canto_Inferior_Esquerdo = 7
canto_Inferior_Medio = 8
canto_Inferior_Direito = 9

quinas = [canto_Superior_Direito, canto_Superior_Esquerdo, canto_Inferior_Direito, canto_Inferior_Esquerdo] # Menor relevancia
meios = [canto_Superior_Medio, canto_Inferior_Medio, meio_Esquerdo, meio_Direito] # Relevancia media

'''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
'''

def analisar(lista_retangulos):
    posicao = -1
    for retangulo in lista_retangulos:
        posicao_atual = analisar_forma(retangulo.base, retangulo.altura, retangulo.cx, retangulo.cy)
        posicao = posicao_atual if posicao == -1 else posicao
        if(posicao_atual == centro):
            return centro
        if(posicao_atual in meios):
            if(posicao_atual != posicao and posicao in meios):
                return centro
            if(posicao_atual != posicao and (posicao + posicao_atual == 7 or posicao + posicao_atual == 11 or posicao + posicao_atual == 9 or posicao + posicao_atual == 13)):
                return centro
        if(posicao_atual != posicao and posicao in meios and (posicao + posicao_atual == 7 or posicao + posicao_atual == 11 or posicao + posicao_atual == 9 or posicao + posicao_atual == 13)):
            return centro
        if(posicao_atual != posicao):
            posicao = (posicao + posicao_atual) / 2
    
    return posicao


def analisar_forma(base, altura, cx, cy):
    if(cx >= 0 and cy >= 0): 
        if(altura / 2 <= cy and base / 2 <= cx):
            return canto_Inferior_Esquerdo
        elif(altura / 2 > cy and base / 2 <= cx):
            return meio_Esquerdo
        elif(altura / 2 <= cy and base / 2 > cx):
            return canto_Inferior_Medio
        elif(altura / 2 > cy and base / 2 > cx):
            return centro
        
    if(cx <= 0 and cy >= 0):
        cx_aux = cx * -1

        if(altura / 2 <= cy and base / 2 <= cx_aux):
            return canto_Inferior_Direito
        elif(altura / 2 > cy and base / 2 <= cx_aux):
            return meio_Direito
        elif(altura / 2 <= cy and base / 2 > cx_aux):
            return canto_Inferior_Medio
        elif(altura / 2 > cy and base / 2 > cx_aux):
            return centro

    if(cx >= 0 and cy <= 0):
        cy_aux = cy * -1

        if(altura / 2 <= cy_aux and base / 2 <= cx):
            return canto_Superior_Esquerdo
        elif(altura / 2 > cy_aux and base / 2 <= cx):
            return meio_Esquerdo
        elif(altura / 2 <= cy_aux and base / 2 > cx):
            return canto_Superior_Medio
        elif(altura / 2 > cy_aux and base / 2 > cx):
            return centro

    if(cx <= 0 and cy <= 0):
        cx_aux = cx * -1
        cy_aux = cy * -1

        if(altura / 2 <= cy and base / 2 <= cx):
            return canto_Superior_Direito
        elif(altura / 2 > cy and base / 2 <= cx):
            return meio_Direito
        elif(altura / 2 <= cy and base / 2 > cx):
            return canto_Superior_Medio
        elif(altura / 2 > cy and base / 2 > cx):
            return centro
        

# teste
class Retangulo:
    def __init__(self, base, altura, cx, cy):
        self.base = base
        self.altura = altura
        self.cx = cx
        self.cy = cy

retangulos = [
    Retangulo(2, 5, 1, 3),
    Retangulo(4, 3, -1, 4)
]


print(analisar(retangulos)) #naooooo foiii aaaaa