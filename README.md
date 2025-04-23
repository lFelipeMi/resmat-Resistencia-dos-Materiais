Autores:
Leonardo Araujo Armelin, RA: 49577
Cleiton, RA:
Stefany, RA:
Luiz Felipe Miranda, RA: 49581

Línguagem:
Python 3.12.3

Bibliotecas:
Tkinter
Matplotlib
Shapely
Numpy
ABC

IDE:
Visual Studio Code


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

        self.figura_final = Figura(self.figuraADD.completa.difference(self.figuraREM.completa)) 

        if isinstance(self.figura_final, MultiPolygon):
            # Divide os polígonos em partes
            self.figuras_finais = [Figura([(0, 0, 0, 0)]) for _ in self.figura_final.completa.geoms]
            for f, geom in zip(self.figura_final, self.figura_final.completa.geoms):
                f.completa = geom

            self.momento_x = sum(f.momento_inercia('x', self.x_origem) for f in self.figuras_finais)
            self.momento_y = sum(f.momento_inercia('y', self.y_origem) for f in self.figuras_finais)

            self.produto_xy = sum(f.produto_inercia() for f in self.figuras_finais)
        else:
            self.momento_x = self.figura_final.momento_inercia('x', self.x_origem)
            self.momento_y = self.figura_final.momento_inercia('y', self.y_origem)

            self.produto_xy = self.figura_final.produto_inercia()

        self.momento_o = self.momento_x + self.momento_y 

        self.resultado["text"] = (
            f"Ix = {self.momento_x:.2f} {unidade}\n"
            f"Iy = {self.momento_y:.2f} {unidade}\n"
            f"Jo = {self.momento_o:.2f} {unidade}\n"
            f"Produto de Inércia = Resultado {unidade}")

Application(root)
root.mainloop()
