import re #funcao regular

class Termo:
    def __init__(self, dividendo, divisor=None):
        self.dividendo = self.__limpar_zeros(list(dividendo))
        self.divisor = self.__limpar_zeros(list(divisor)) if divisor else [1]

    def __repr__(self):
        div = self.__formatar_polinomio(self.dividendo)
        den = self.__formatar_polinomio(self.divisor)
        return f"({div})/({den})" if den != "1" else div

    def __formatar_polinomio(self, coeficientes):
        formula = ""
        grau = len(coeficientes) - 1
        for i, coef in enumerate(coeficientes):
            expoente = grau - i
            if coef == 0:
                continue
            if coef > 0 and i != 0:
                formula += "+"
            if expoente == 0:
                formula += f"{coef}"
            elif expoente == 1:
                formula += f"{coef}x"
            else:
                formula += f"{coef}x^{expoente}"
        return formula or "0"

    def __limpar_zeros(self, polinomio):
        while len(polinomio) > 1 and polinomio[0] == 0:
            polinomio.pop(0)
        return polinomio

    def avaliar(self, x):
        def calcular(p):
            return sum(coef * (x ** (len(p) - i - 1)) for i, coef in enumerate(p))
        num = calcular(self.dividendo)
        den = calcular(self.divisor)
        if den == 0:
            raise ZeroDivisionError(f"Divisão por zero ao avaliar {self}")
        return num / den

    def derivada(self):
        f = self.dividendo
        g = self.divisor
        f_linha = self.__derivar(f)
        g_linha = self.__derivar(g)
        numerador = self.__subtrair_polinomios(
            self.__multiplicar_polinomios(f_linha, g),
            self.__multiplicar_polinomios(f, g_linha)
        )
        denominador = self.__multiplicar_polinomios(g, g)
        return Termo(numerador, denominador)

    def __derivar(self, p):
        derivada = []
        grau = len(p) - 1
        for i, coef in enumerate(p):
            expoente = grau - i
            if expoente > 0:
                derivada.append(coef * expoente)
        return derivada or [0]

    def __multiplicar_polinomios(self, p1, p2):
        grau_res = len(p1) + len(p2) - 2
        resultado = [0] * (grau_res + 1)
        for i in range(len(p1)):
            for j in range(len(p2)):
                resultado[i + j] += p1[i] * p2[j]
        return resultado

    def __subtrair_polinomios(self, p1, p2):
        max_len = max(len(p1), len(p2))
        p1 = [0] * (max_len - len(p1)) + p1
        p2 = [0] * (max_len - len(p2)) + p2
        return [a - b for a, b in zip(p1, p2)]

    def __mul__(self, other):
        if isinstance(other, Termo):
            novo_num = self.__multiplicar_polinomios(self.dividendo, other.dividendo)
            novo_den = self.__multiplicar_polinomios(self.divisor, other.divisor)
            return Termo(novo_num, novo_den)
        raise TypeError("Multiplicação inválida entre Termo e outro tipo")

    def __truediv__(self, other):
        if isinstance(other, Termo):
            novo_num = self.__multiplicar_polinomios(self.dividendo, other.divisor)
            novo_den = self.__multiplicar_polinomios(self.divisor, other.dividendo)
            return Termo(novo_num, novo_den)
        raise TypeError("Divisão inválida entre Termo e outro tipo")


class Funcao:
    def __init__(self, *termos):
        self.__termos = []
        for termo in termos:
            if isinstance(termo, Termo):
                self.__termos.append(termo)
            elif isinstance(termo, tuple) and len(termo) == 2:
                self.__termos.append(Termo(termo[0], termo[1]))
            elif isinstance(termo, list):
                self.__termos.append(Termo(termo))
            else:
                raise ValueError("Formato inválido de termo.")

    def __repr__(self):
        result = ""
        for i, termo in enumerate(self.__termos):
            termo_str = repr(termo)
            if i > 0 and "-" not in termo_str:
                result += "+"
            result += termo_str
        return result

    def avaliar(self, x):
        return sum(t.avaliar(x) for t in self.__termos)

    def __add__(self, other):
        if not isinstance(other, Funcao):
            raise TypeError("Somente funções podem ser somadas.")
        return Funcao(*self.__termos, *other.__termos)

    def __sub__(self, other):
        if not isinstance(other, Funcao):
            raise TypeError("Somente funções podem ser subtraídas.")
        termos_neg = [Termo([-c for c in t.dividendo], t.divisor) for t in other.__termos]
        return Funcao(*self.__termos, *termos_neg)

    def __mul__(self, other):
        if not isinstance(other, Funcao):
            raise TypeError("Somente funções podem ser multiplicadas.")
        termos_result = []
        for t1 in self.__termos:
            for t2 in other.__termos:
                termos_result.append(t1 * t2)
        return Funcao(*termos_result)

    def __truediv__(self, other):
        if not isinstance(other, Funcao):
            raise TypeError("Somente funções podem ser divididas.")
        termos_result = []
        for t1 in self.__termos:
            for t2 in other.__termos:
                termos_result.append(t1 / t2)
        return Funcao(*termos_result)

    def derivada(self):
        return Funcao(*[t.derivada() for t in self.__termos])

    @staticmethod
    def from_string(expr):
        expr = expr.replace(" ", "")
        pattern = re.compile(r"([+-]?[^+-]+)")
        termos_raw = pattern.findall(expr)

        termos = []
        for raw in termos_raw:
            if "/" in raw:
                num, den = raw.split("/")
                num_coef = parse_polinomio(num)
                den_coef = parse_polinomio(den)
                termos.append(Termo(num_coef, den_coef))
            else:
                termos.append(Termo(parse_polinomio(raw)))
        return Funcao(*termos)


def parse_polinomio(expr): 
    if expr == "":
        return [0]
    if not re.search(r"x", expr):
        return [int(expr)]

    termos = re.findall(r"([+-]?\d*)(x(?:\^\d+)?)?", expr)
    grau_max = 0
    partes = []

    for coef, var in termos:
        if coef in ("", "+"): coef = 1
        elif coef == "-": coef = -1
        else: coef = int(coef)

        if var == "":
            exp = 0
        elif "^" in var:
            exp = int(var.split("^")[1])
        else:
            exp = 1

        grau_max = max(grau_max, exp)
        partes.append((exp, coef))

    coeficientes = [0] * (grau_max + 1)
    for exp, coef in partes:
        coeficientes[grau_max - exp] += coef

    return coeficientes

f = Funcao.from_string("x^3/3x - 2x - 6")
g = Funcao.from_string("4x + 2")

print("f(x):", f)
print("g(x):", g)
print("f * g:", f * g)
print("f / g:", f / g)
print("f derivada:", f.derivada())
