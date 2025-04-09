class Funcao:
    def __init__(self, *args):
        self.__polinomios = list(args)  

    def __repr__(self):
        formula = ""
        grau = len(self.__polinomios) - 1
        for i, coef in enumerate(self.__polinomios):
            expoente = grau - i

            if coef >= 0 and i != 0:
                formula += "+"

            formula += f"{coef}"
            if expoente > 0:
                formula += f"x"
                if expoente > 1:
                    formula += f"^{expoente}"
        return formula

    @property
    def polinomios(self):
        return self.__polinomios


f1 = Funcao(3, -2, 5, 4)
print(f1)