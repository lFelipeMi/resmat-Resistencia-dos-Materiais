from tkinter import * #sudo apt-get install python3-tk


root = Tk()

class application:
    def __init__(self, master=None):

        root.title("Calculadora de Momento de Inércia")
        root.attributes('-fullscreen', True)
        root.configure(background='#1e3743')

        #-------------------------------------------------CRIAÇÃO DE CONTAINERS--------------------------------------------------#

        self.widget1 = Frame(master)   #frame titulo
        self.widget1["pady"] = 10    
        self.widget1.pack(fill=X)

        self.widget2 = Frame(master, width=450, height=800, bg="#1e3743")   #frame entradas
        self.widget2["padx"] = 10
        self.widget2["pady"] = 10
        self.widget2.columnconfigure(0, weight=1)
        self.widget2.pack_propagate(0)       
        self.widget2.pack(side=LEFT)

        self.widget3 = Frame(master)   #frame visual
        self.widget3["padx"] = 20   
        self.widget3["pady"] = 20
        self.widget3.pack()

        self.widget4 = Frame(self.widget2)       #frame entrada parte superior
        self.widget4["pady"] = 40
        self.widget4.pack(anchor=NW, expand=TRUE, fill=BOTH)

        #---------------------------------------------------TEXTOS-----------------------------------------------------------#

        self.titulo = Label(self.widget1, text="Calculadora de Momento de Inércia") #criação de uma msg nesse container
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()

        self.resultado = Label(self.widget4)
        self.resultado["font"] = ("Arial", "10", "bold")
        self.resultado.grid(row=7, column=1, columnspan=2)

        #---------------------------------------------------ENTRADAS-----------------------------------------------------------#

        self.Y = Entry(self.widget4)
        self.Y["width"] = 10
        self.Y["font"] = ("Arial", "12")
        self.Y.grid(row=1, column=3, padx=5, pady=10)

        self.CXLabel = Label(self.widget4, text="X Inicial", font=("Arial", "12"))
        self.CXLabel.grid(row=0, column=0)

        self.CX = Entry(self.widget4)
        self.CX["width"] = 10
        self.CX["font"] = ("Arial", "12")
        self.CX.grid(row=1, column=0, padx=5, pady=10)

        self.CYLabel = Label(self.widget4, text="Y Inicial", font=("Arial", "12"))
        self.CYLabel.grid(row=0, column=1)

        self.XLabel = Label(self.widget4, text="Centróide X", font=("Arial", "12"))
        self.XLabel.grid(row=0, column=2)

        self.X = Entry(self.widget4)
        self.X["width"] = 10
        self.X["font"] = ("Arial", "12")
        self.X.grid(row=1, column=2, padx=5, pady=10)

        self.YLabel = Label(self.widget4, text="Centróide Y", font=("Arial", "12"))
        self.YLabel.grid(row=0, column=3)

        self.CY = Entry(self.widget4)
        self.CY["width"] = 10
        self.CY["font"] = ("Arial", "12")
        self.CY.grid(row=1, column=1, padx=5, pady=10)

        self.baseLabel = Label(self.widget4, text="Base (m)", font=("Arial", "12"))
        self.baseLabel.grid(row=2, column=0)

        self.base = Entry(self.widget4)
        self.base["width"] = 10
        self.base["font"] = ("Arial", "12")
        self.base.grid(row=3, column=0, padx=5, pady=10)

        self.alturaLabel = Label(self.widget4, text="Altura (m)", font=("Arial", "12"))
        self.alturaLabel.grid(row=2, column=1)

        self.altura = Entry(self.widget4)
        self.altura["width"] = 10
        self.altura["font"] = ("Arial", "12")
        self.altura.grid(row=3, column=1, padx=5, pady=10)

        #---------------------------------------------------BOTÕES-------------------------------------------------------------#

        self.contar = Button(self.widget4)
        self.contar["text"] = "Calcular"
        self.contar["font"] = ("Arial", "12")
        self.contar["fg"] = ("Blue")
        self.contar["width"] = 10
        self.contar["pady"] = 5
        self.contar["command"] = self.Calcular #atrela botão a função
        self.contar.grid(row=4, column=1, columnspan=2)

        self.sair = Button(self.widget4)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Arial", "12")
        self.sair["fg"] = ("Red")
        self.sair["width"] = 5
        self.sair["command"] = self.widget4.quit  #atribuição de uma função "quit" para o botão
        self.sair.grid(sticky=S, column=1, columnspan=2)

        self.add = Button(self.widget4)
        self.add["text"] = "Adicionar"
        self.add["font"] = ("Arial", "12")
        self.add["width"] = 7
        self.add.grid(row=3, column=2)

        self.sub = Button(self.widget4)
        self.sub["text"] = "Subtrair"
        self.sub["font"] = ("Arial", "12")
        self.sub["width"] = 7
        self.sub.grid(row=3, column=3)

        #----------------------------------------------------------------------------------------------------------------------#

    def Calcular(self):   #EVENT HANDLER --> botão chama a função
        base = float(self.base.get())
        altura = float(self.altura.get())

        if base > 0 and altura > 0:
            area = base*altura
            self.resultado["text"] = f"Ix = RESULTADO\nIy = RESULTADO\nÁrea = {area} m²"
        else:
            self.resultado["text"] = "Dados inválidos"



application(root)
root.mainloop()              #necessario para rodar a GUI