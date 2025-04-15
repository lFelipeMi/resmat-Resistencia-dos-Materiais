from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

from bknd import  FormaGeometrica, Retangulo, Figura, analisar, analisar_forma

root = Tk()

class Application:
    def __init__(self, master=None):
        root.title("Calculadora de Momentos e Produto de Inércia")
        root.attributes('-fullscreen', True)
        root.configure(background='#1e3743')

        self.retangulos = Figura()

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
        self.CXLabel = Label(self.origemFrame, text="X:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.CXLabel.grid(row=1, column=0)
        self.CX = Entry(self.origemFrame, width=10, font=("Arial", "12"))
        self.CX.grid(row=1, column=1, padx=3, pady=5)

        self.CYLabel = Label(self.origemFrame, text="Y:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.CYLabel.grid(row=2, column=0)
        self.CY = Entry(self.origemFrame, width=10, font=("Arial", "12"))
        self.CY.grid(row=2, column=1, padx=3, pady=5)

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
        self.limparPlano.grid(row=7, column=0, pady=10)

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

        self.XLabel = Label(self.subpainel, text="X do Centróide:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.XLabel.grid(row=5, column=0)
        self.X = Entry(self.subpainel, width=10, font=("Arial", "12"))
        self.X.grid(row=5, column=1, padx=5, pady=10)

        self.YLabel = Label(self.subpainel, text="Y do Centróide:", font=("Arial", "12"), bg="#cccccc", fg="black")
        self.YLabel.grid(row=6, column=0)
        self.Y = Entry(self.subpainel, width=10, font=("Arial", "12"))
        self.Y.grid(row=6, column=1, padx=5, pady=10)

        self.add = Button(self.subpainel, text="Adicionar", font=("Arial", "12"), width=10, command=self.Adicionar)
        self.add.grid(row=7, column=1, pady=10, sticky=W)

        self.remover = Button(self.subpainel, text="Remover", font=("Arial", "12"), width=10, command=self.Remover)
        self.remover.grid(row=7, column=2, pady=10, sticky=W)

    # ---------------- SubPainel2 ----------------
        self.subpainel2 = Frame(self.painelControles, bg="#cccccc")
        self.subpainel2.pack(anchor=NW, expand=TRUE, fill=BOTH)

        self.calc = Button(self.subpainel2, text="Calcular Momentos e Produto de Inércia", font=("Arial", "12"), fg="green", width=40, pady=10, command=self.Calcular)
        self.calc.grid(row=6, column=0, columnspan=4, padx=(45,0), pady=(5, 20))

        self.resultado = Label(self.subpainel2, font=("Arial", "12", "bold"),  bg="#cccccc", fg="black")
        self.resultado.grid(row=10, column=2, padx=(20,0), pady=10, sticky=W)

    # ---------------- Plano ----------------
        self.plano = Frame(master, bg="#1e3743")
        self.plano.pack(fill=BOTH, expand=True, padx=20, pady=20)
        self.fig = None
        self.ax = None
        self.canvas = None

    # ----------------  Criando o Plano ----------------
    def DefinirOrigem(self):
        try:
            self.x_origem = float(self.CX.get())
            self.y_origem = float(self.CY.get())
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
            cx = float(self.X.get())
            cy = float(self.Y.get())
            x_origem = float(self.CX.get())
            y_origem = float(self.CY.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
            return

        canto_x = cx - base / 2
        canto_y = cy - altura / 2

        if self.ax:
            retangulo = patches.Rectangle((canto_x, canto_y), base, altura, linewidth=2, edgecolor='lightblue', facecolor='lightblue')
            self.retangulos.adicionar_forma(Retangulo(base, altura, cx, cy))
            self.ax.add_patch(retangulo)
            self.canvas.draw()
        
        self.X.delete(0, END)
        self.Y.delete(0, END)
        self.base.delete(0, END)
        self.altura.delete(0, END) #isso limpa a entry após apertar o botão

    # ---------------- Removendo subáreas ----------------
    def Remover(self):
        try:
            base = float(self.base.get())
            altura = float(self.altura.get())
            cx = float(self.X.get())
            cy = float(self.Y.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
            return

        canto_x = cx - base / 2
        canto_y = cy - altura / 2

        if self.ax:
            remover = patches.Rectangle((canto_x, canto_y), base, altura, linewidth=1, edgecolor='gray', facecolor='lightgray', hatch='////', alpha=0.7)
            self.ax.add_patch(remover)
            self.retangulos.adicionar_forma(Retangulo(base, -1 * altura, cx, cy))
            self.canvas.draw()

        self.X.delete(0, END)
        self.Y.delete(0, END)
        self.base.delete(0, END)
        self.altura.delete(0, END)
    
    def LimparPlano(self):
        if self.ax:

            self.ax.clear()

            try:
                x_origem = float(self.CX.get())
                y_origem = float(self.CY.get())
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

        self.retangulos.formas.clear()
        self.resultado["text"] = ""

    def Calcular(self):

        unidade = self.opcao.get()

        match unidade:
            case 'Centímetros':
                unidade = "cm⁴"
            case 'Milímetros':
                unidade = "mm⁴"
            case 'Metros':
                unidade = "m⁴"        

        self.retangulos.verificar_sobreposicoes()

        self.resultado["text"] = (
            f"Ix = {self.retangulos.momento_em('x'):.2f} {unidade}\n"
            f"Iy = {self.retangulos.momento_em('y'):.2f} {unidade}\n"
            f"Jo = {self.retangulos.momento_total():.2f} {unidade}\n"
            f"Produto de Inércia = Resultado {unidade}")


Application(root)
root.mainloop()