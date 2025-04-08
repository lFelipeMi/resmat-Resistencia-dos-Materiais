from tkinter import * #sudo apt-get install python3-tk

class application:
    def __init__(self, master=None):

        #-------------------------------------------------CRIAÇÃO DE CONTAINERS--------------------------------------------------#

        self.widget1 = Frame(master)
        self.widget1["pady"] = 10
        self.widget1.pack()

        self.widget2 = Frame(master)
        self.widget2["padx"] = 20
        self.widget2.pack()

        self.widget3 = Frame(master)
        self.widget3["padx"] = 20
        self.widget3.pack()

        self.widget4 = Frame(master)
        self.widget4["pady"] = 20
        self.widget4.pack()

        #---------------------------------------------------TEXTOS-----------------------------------------------------------#

        self.titulo = Label(self.widget1, text="Calculadora de Momento de Inércia") #criação de uma msg nesse container
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()

        self.resultado = Label(self.widget4, text="")
        self.resultado["font"] = ("Arial", "10", "bold")
        self.resultado.pack()

        #---------------------------------------------------ENTRADAS-----------------------------------------------------------#

        self.baseLabel = Label(self.widget2, text="Base (m)", font=("Arial", "12"))
        self.baseLabel.pack(side=LEFT)

        self.base = Entry(self.widget2)
        self.base["width"] = 10
        self.base["font"] = ("Arial", "12")
        self.base.pack(side=LEFT)           #não estou conseguindo mudar a posição dos textos nem das entradas :(

        self.alturaLabel = Label(self.widget3, text="Altura (m)", font=("Arial", "12"))
        self.alturaLabel.pack(side=LEFT)

        self.altura = Entry(self.widget3)
        self.altura["width"] = 10
        self.altura["font"] = ("Arial", "12")
        self.altura.pack(side=LEFT)

        #---------------------------------------------------BOTÕES-------------------------------------------------------------#

        self.contar = Button(self.widget4)
        self.contar["text"] = "Calcular"
        self.contar["font"] = ("Calibri", "10")
        self.contar["fg"] = ("Blue")
        self.contar["width"] = 10
        self.contar["command"] = self.Calcular #atrela botão a função
        self.contar.pack()

        self.sair = Button(self.widget4)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["fg"] = ("Red")
        self.sair["width"] = 5
        self.sair["command"] = self.widget4.quit  #atribuição de uma função "quit" para o botão
        self.sair.pack()

        #----------------------------------------------------------------------------------------------------------------------#

    def Calcular(self):   #EVENT HANDLER --> botão chama a função
        base = float(self.base.get())
        altura = float(self.altura.get())

        if base > 0 and altura > 0:
            area = base*altura
            self.resultado["text"] = f"Ix = RESULTADO\nIy = RESULTADO\nÁrea = {area} m²"
        else:
            self.resultado["text"] = "Dados inválidos"



root = Tk()
application(root)
root.mainloop()              #necessario para rodar a GUI