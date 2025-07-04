from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches
import numpy as np

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon

from bknd import criar_retangulo, Figura

root = Tk()

class Application:
    def __init__(self, master=None):
        root.title("Calculadora de Momentos e Produto de Inércia")
        root.attributes('-fullscreen', True)
        root.configure(background='#1e3743')

        self.centroide = None
        self.retangulosADD = []
        self.retangulosREM = []

    # ---------------- Título ----------------
        self.topoFrame = Frame(master, pady=10)
        self.topoFrame.pack(fill=X)
        self.titulo = Label(self.topoFrame, text="Calculadora de Momentos e Produto de Inércia", font=("Arial", 14, "bold"))
        self.titulo.pack()
    
    # ---------------- Painel lateral esquerdo ----------------
        self.painelControles = Frame(master, width=500, height=800, bg="#cccccc")
        self.painelControles.pack_propagate(0)
        self.painelControles.pack(side=LEFT, padx=40, pady=40, anchor=N)

    # ---------------- Saída ----------------
        self.sair = Button(self.painelControles, text="Sair", font=("Arial", "12"), fg="white", bg="red", width=8, command=root.quit)
        self.sair.pack(side=BOTTOM, anchor=SW, padx=10, pady=10)

    # ---------------- SubPainel ----------------
        self.subpainel = Frame(self.painelControles, bg="#cccccc")
        self.subpainel.pack(anchor=NW, expand=TRUE, fill=BOTH)

    # ---------------- Origem ----------------
        self.origemFrame = Frame(self.subpainel, bg="#cccccc")
        self.origemFrame.grid(row=0, column=0, columnspan=4, padx=(5,0), pady=(10, 10))

        self.origemMsg = Label(self.origemFrame, text="Defina as coordenadas para a origem do sistema:", font=("Arial", 12), bg="#cccccc", fg="black")
        self.origemMsg.grid(row=0, column=0, columnspan=3, pady=(5, 10))

    # ---------------- Entradas Coordenadas ----------------
        self.origemXLabel = Label(self.origemFrame, text="X:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.origemXLabel.grid(row=1, column=0)
        self.origemX = Entry(self.origemFrame, width=10, font=("Arial", "12"))
        self.origemX.grid(row=1, column=1, padx=3, pady=5)

        self.origemYLabel = Label(self.origemFrame, text="Y:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.origemYLabel.grid(row=2, column=0)
        self.origemY = Entry(self.origemFrame, width=10, font=("Arial", "12"))
        self.origemY.grid(row=2, column=1, padx=3, pady=5)

        self.definirBtn = Button(self.origemFrame, text="Definir Origem", font=("Arial", "12"), command=self.DefinirOrigem)
        self.definirBtn.grid(row=3, column=1, padx=3, pady=5)

    # ---------------- Unidade de medida ----------------  
        self.unidadeLabel = Label(self.origemFrame, text="Unidade:", font=("Arial", "12"), bg="#cccccc")
        self.unidadeLabel.grid(row=1, column=2)
        self.opcao = StringVar()
        self.unidade = OptionMenu(self.origemFrame, self.opcao, "Metros", "Centímetros", "Milímetros")
        self.unidade.config(width=10)
        self.unidade.grid(row=1, column=3, columnspan=2)

    # ---------------- Limpar plano ----------------  
        self.limparPlano = Button(self.subpainel, text="Limpar plano", font=("Arial", "12"), fg=("red"), command=self.LimparPlano)
        self.limparPlano.grid(row=7, column=0,padx=15, pady=10, sticky=W)

    # ---------------- Subáreas ----------------
        self.subareaMsg = Label(self.subpainel, text="Adicione ou remova uma subárea da área final:", font=("Arial", 12), bg="#cccccc", fg="black")
        self.subareaMsg.grid(row=2, column=0, columnspan=4, padx=(5,0), pady=(0, 10), sticky="w")

        self.baseLabel = Label(self.subpainel, text="Base:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.baseLabel.grid(row=3, column=0)
        self.base = Entry(self.subpainel, width=10, font=("Arial", "12"))
        self.base.grid(row=3, column=1, padx=5, pady=10)

        self.alturaLabel = Label(self.subpainel, text="Altura:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.alturaLabel.grid(row=4, column=0)
        self.altura = Entry(self.subpainel, width=10, font=("Arial", "12"))
        self.altura.grid(row=4, column=1, padx=5, pady=10)

        self.CXLabel = Label(self.subpainel, text="X do Centróide:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.CXLabel.grid(row=5, column=0)
        self.CX = Entry(self.subpainel, width=10, font=("Arial", "12"))
        self.CX.grid(row=5, column=1, padx=5, pady=10)

        self.CYLabel = Label(self.subpainel, text="Y do Centróide:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.CYLabel.grid(row=6, column=0)
        self.CY = Entry(self.subpainel, width=10, font=("Arial", "12"))
        self.CY.grid(row=6, column=1, padx=5, pady=10)

        self.add = Button(self.subpainel, text="Adicionar", font=("Arial", "12"), width=10, command=self.Adicionar)
        self.add.grid(row=7, column=1,padx=15, pady=10, sticky=W)

        self.remover = Button(self.subpainel, text="Remover", font=("Arial", "12"), width=10, command=self.Remover)
        self.remover.grid(row=7, column=2,padx=15, pady=10, sticky=W)

    # ---------------- SubPainel2 ----------------
        self.subpainel2 = Frame(self.painelControles, bg="#cccccc")
        self.subpainel2.pack(anchor=NW, expand=TRUE, fill=BOTH)

        self.calc = Button(self.subpainel2, text="Calcular Momentos e Produto de Inércia", font=("Arial", "12"), fg="green", width=40, pady=10, command=self.Calcular)
        self.calc.grid(row=6, column=0, columnspan=4, padx=(45,0), pady=(5, 20))

        self.resultado = Label(self.subpainel2, font=("Arial", "12", "bold"),  bg="#cccccc", fg="black")
        self.resultado.grid(row=10, column=2, padx=10, sticky=W)

    # ---------------- Plano ----------------
        self.plano = Frame(master, bg="#1e3743")
        self.plano.pack(fill=BOTH, expand=True, padx=20, pady=20)
        self.fig = None
        self.ax = None
        self.canvas = None

    # ----------------  Criando o Plano ----------------
    def DefinirOrigem(self):
        try:
            self.x_origem = float(self.origemX.get())
            self.y_origem = float(self.origemY.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
            return

        if self.fig is None:
            self.fig = Figure(figsize=(15, 6), dpi=100)
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.plano)
            self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        self.ax.clear()

        self.ax.set_xlim(self.x_origem - 50, self.x_origem + 50)
        self.ax.set_ylim(self.y_origem - 50, self.y_origem + 50)

        self.ax.set_xticks(np.arange(self.x_origem - 50, self.x_origem + 51, 5))
        self.ax.set_yticks(np.arange(self.y_origem - 50, self.y_origem + 51, 5))

        self.ax.grid(True)

        self.ax.axhline(y=self.y_origem, color='black', linewidth=1)
        self.ax.axvline(x=self.x_origem, color='black', linewidth=1)

        self.ax.set_xlabel("Eixo X")
        self.ax.set_ylabel("Eixo Y")

        self.ax.plot(self.x_origem, self.y_origem, marker='o', color='black', markersize=10, label='Origem')

        self.canvas.draw()
    
    # ---------------- Adicionando subáreas ----------------
    def Adicionar(self):
        try:
            base = float(self.base.get())
            altura = float(self.altura.get())
            cx = float(self.CX.get())
            cy = float(self.CY.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
            return

        if base <= 0 or altura <= 0:
            messagebox.showerror("Erro", "A área do retângulo deve ser positiva.")
            return

        canto_x = cx - base / 2
        canto_y = cy - altura / 2

        if self.ax:
            retangulo = patches.Rectangle((canto_x, canto_y), base, altura, linewidth=2, edgecolor='lightblue', facecolor='lightblue')
            self.retangulosADD.append((base, altura, cx, cy))
            self.ax.add_patch(retangulo)
            self.AjustarPlano()
            self.ExibirCentroide()
            self.canvas.draw()
        
        self.CX.delete(0, END)
        self.CY.delete(0, END)
        self.base.delete(0, END)
        self.altura.delete(0, END)              #isso limpa a entry após apertar o botão

    # ---------------- Removendo subáreas ----------------
    def Remover(self):
        try:
            base = float(self.base.get())
            altura = float(self.altura.get())
            cx = float(self.CX.get())
            cy = float(self.CY.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
            return

        if base <= 0 or altura <= 0:
            messagebox.showerror("Erro", "A área do retângulo deve ser positiva.")
            return
        
        canto_x1 = cx - base / 2
        canto_y1 = cy - altura / 2
        canto_x2 = cx + base / 2
        canto_y2 = cy + altura / 2

        interseccao = False

        for base_add, altura_add, cx_add, cy_add in self.retangulosADD:

            add_x1 = cx_add - base_add / 2
            add_y1 = cy_add - altura_add / 2
            add_x2 = cx_add + base_add / 2
            add_y2 = cy_add + altura_add / 2

            inter_x1 = max(canto_x1, add_x1)
            inter_y1 = max(canto_y1, add_y1)
            inter_x2 = min(canto_x2, add_x2)
            inter_y2 = min(canto_y2, add_y2)

            if inter_x2 > inter_x1 and inter_y2 > inter_y1:
                interseccao = True
                largura_inter = inter_x2 - inter_x1
                altura_inter = inter_y2 - inter_y1

                remocao = patches.Rectangle((inter_x1, inter_y1), largura_inter, altura_inter, linewidth=1, edgecolor='gray', facecolor='lightgray', hatch='////', alpha=0.7)
                self.ax.add_patch(remocao)
                self.retangulosREM.append((largura_inter, altura_inter, inter_x1 + largura_inter/2, inter_y1 + altura_inter/2))

        self.CX.delete(0, END)
        self.CY.delete(0, END)
        self.base.delete(0, END)
        self.altura.delete(0, END)

        if not interseccao:
            return
        else:
            self.ExibirCentroide()
            self.canvas.draw()

    # ---------------- Removendo tudo ----------------
    def LimparPlano(self):
        if self.ax:

            self.ax.clear()

            try:
                x_origem = float(self.origemX.get())
                y_origem = float(self.origemY.get())
            except ValueError:
                messagebox.showerror("Erro", "Por favor, defina a origem corretamente antes de limpar.")
                return

        self.ax.set_xlim(x_origem - 50, x_origem + 50)
        self.ax.set_ylim(y_origem - 50, y_origem + 50)

        self.ax.set_xticks(np.arange(x_origem - 50, x_origem + 51, 5))
        self.ax.set_yticks(np.arange(y_origem - 50, y_origem + 51, 5))

        self.ax.grid(True)
        self.ax.axhline(y=y_origem, color='black', linewidth=1)
        self.ax.axvline(x=x_origem, color='black', linewidth=1)
        self.ax.set_xlabel("Eixo X")
        self.ax.set_ylabel("Eixo Y")
        self.ax.plot(x_origem, y_origem, marker='o', color='black', markersize=10, label='Origem')

        self.canvas.draw()

        self.retangulosADD.clear()
        self.retangulosREM.clear()
        self.resultado["text"] = ""

    # ---------------- Plano dinâmico ----------------
    def AjustarPlano(self):

        maior = 0
        for el in self.retangulosADD:          #percorre a tupla maior

            i = 0
            while i < 4:                       #percorre os elementos da tupla menor
                if abs(el[i]) >= maior:
                    maior = int(el[i] * 2)
                i+=1
            
        ticks = abs(maior*0.2)
        maior = abs(maior)

        self.ax.set_xlim(self.x_origem - maior, self.x_origem + maior)
        self.ax.set_ylim(self.y_origem - maior, self.y_origem + maior)

        self.ax.set_xticks(np.arange(self.x_origem - maior, self.x_origem + (maior+1), ticks))
        self.ax.set_yticks(np.arange(self.y_origem - maior, self.y_origem + (maior+1), ticks))

    # ---------------- Exibição centróide ----------------
    def ExibirCentroide(self):

        areas = []
        centroides_x = []
        centroides_y = []
        addFiltrado = []
        lados = [] 

        for base, altura, cx, cy in self.retangulosADD:
            xmin, xmax = cx - base/2, cx + base/2
            ymin, ymax = cy - altura/2, cy + altura/2

            dentro = False
            for xb_min, xb_max, yb_min, yb_max in lados:
                if xmin >= xb_min and xmax <= xb_max and ymin >= yb_min and ymax <= yb_max:
                    dentro = True
                    break

            if not dentro:
                addFiltrado.append((base, altura, cx, cy))
                lados.append((xmin, xmax, ymin, ymax))

        for base, altura, cx, cy in addFiltrado:
            areas.append(base * altura)
            centroides_x.append(cx)
            centroides_y.append(cy)

        for base, altura, cx, cy in self.retangulosREM:
            areas.append(-base * altura)
            centroides_x.append(cx)
            centroides_y.append(cy)

        area_total = sum(areas)

        if area_total == 0:
            return

        numerador_x = sum(cx * a for cx, a in zip(centroides_x, areas))
        numerador_y = sum(cy * a for cy, a in zip(centroides_y, areas))
        centroide_x = numerador_x / area_total
        centroide_y = numerador_y / area_total

        if self.centroide is not None:
            try:
                self.centroide.remove()
            except NotImplementedError:
                self.centroide.set_visible(False)

        self.centroide = self.ax.scatter(centroide_x, centroide_y, c='red')

    # ---------------- Cálculos -----------------
    def Calcular(self):

        unidade = self.opcao.get()

        match unidade:
            case 'Centímetros':
                unidade = "cm⁴"
            case 'Milímetros':
                unidade = "mm⁴"
            case 'Metros':
                unidade = "m⁴"        

        self.figuraADD = Figura(self.retangulosADD)
        self.figuraREM = Figura(self.retangulosREM)

        try:
            self.x_origem = float(self.origemX.get())
            self.y_origem = float(self.origemY.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
            return

        if (isinstance(self.figuraADD.completa, MultiPolygon) and isinstance(self.figuraREM.completa, MultiPolygon)):
            # Divide os polígonos em partes
            self.figurasADD = [Figura([(0, 0, 0, 0)]) for _ in self.figuraADD.completa.geoms]
            for f, geom in zip(self.figurasADD, self.figuraADD.completa.geoms):
                f.completa = geom

            self.figurasREM = [Figura([(0, 0, 0, 0)]) for _ in self.figuraREM.completa.geoms]
            for f, geom in zip(self.figurasREM, self.figuraREM.completa.geoms):
                f.completa = geom

            # Cálculo de momentos
            self.momento_xADD = sum(f.momento_inercia('x', self.x_origem) for f in self.figurasADD)
            self.momento_xREM = sum(f.momento_inercia('x', self.x_origem) for f in self.figurasREM)
            self.momento_x = self.momento_xADD - self.momento_xREM

            self.momento_yADD = sum(f.momento_inercia('y', self.y_origem) for f in self.figurasADD)
            self.momento_yREM = sum(f.momento_inercia('y', self.y_origem) for f in self.figurasREM)
            self.momento_y = self.momento_yADD - self.momento_yREM

            self.produtoADD = sum(f.produto_inercia(self.x_origem, self.y_origem) for f in self.figurasADD)
            self.produtoREM = sum(f.produto_inercia(self.x_origem, self.y_origem) for f in self.figurasREM)
            self.produto_inercia = self.produtoADD - self.produtoREM
        else:

            self.intersecao = self.figuraADD.completa.intersection(self.figuraREM.completa)

            self.intersecao_figura = Figura([])
            self.intersecao_figura.completa = self.intersecao

            self.momento_x = self.figuraADD.momento_inercia('x', self.x_origem) - self.intersecao_figura.momento_inercia('x', self.x_origem)
            self.momento_y = self.figuraADD.momento_inercia('y', self.y_origem) - self.intersecao_figura.momento_inercia('y', self.y_origem)

            self.produto_inercia = self.figuraADD.produto_inercia(self.x_origem, self.y_origem) - self.intersecao_figura.produto_inercia(self.x_origem, self.y_origem)

        self.momento_o = self.momento_x + self.momento_y

        self.resultado["text"] = (
            f"Ix = {self.momento_x:,.2f} {unidade}\n"
            f"Iy = {self.momento_y:,.2f} {unidade}\n"
            f"Jo = {self.momento_o:,.2f} {unidade}\n"
            f"Ixy = {self.produto_inercia:,.2f} {unidade}").replace(",", "X").replace(".", ",").replace("X", ".")

Application(root)
root.mainloop()
