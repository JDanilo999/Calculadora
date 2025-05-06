#calculadora versão antiga. obs: estava no começo de tudo, por isso está cheio de erro. coloquei ela aqui, para mostrar minha evolução em relação a versao Oficial(nova).
from tkinter import *
class calculadoraApp:
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('420x470')
        self.janela.resizable(False,False)
        self.janela.title('Calculadora.JD')
        self.janela.config(background='white')
        self.prinum = 0
        self.segnum = 0
        self.mate = ''
        self.lista = list()
        self.lista2 = list()
        self.resulta = ''
        # visor com label
        self.visor = Label(text='0', width=0, height=2, font=('monospace', 30, 'bold'),anchor='e',fg='black',background='white')
        self.visor.pack()
        #imagens
        self.numero0 = PhotoImage(file='zero_8891020.png')
        self.numero1 = PhotoImage(file='um.png')
        self.numero2 = PhotoImage(file='dois.png')
        self.numero3 = PhotoImage(file='numero-3.png')
        self.numero4 = PhotoImage(file='numero-4.png')
        self.numero5 = PhotoImage(file='numero-5.png')
        self.numero6 = PhotoImage(file='numero-6.png')
        self.numero7 = PhotoImage(file='numero-7.png')
        self.numero8 = PhotoImage(file='numero-8.png')
        self.numero9 = PhotoImage(file='numero-9.png')
        self.button_ce = PhotoImage(file='ce.png')
        self.button_menos = PhotoImage(file='minus-button_4315581.png')
        self.button_mais = PhotoImage(file='add.png')
        self.button_mult = PhotoImage(file='circle.png')
        self.button_div = PhotoImage(file='division_17386076.png')
        self.button_igual = PhotoImage(file='round_11697205.png')
        #botoes
        x = 67
        y = 70
        self.botao0 = Button(image=self.numero0,width=x,height=y,command=lambda:self.num(0),bd=0)
        self.botao0.place(x=130, y=370)

        self.botao1 = Button(image=self.numero1, width=x, height=y,command=lambda:self.num(1),bd=0)
        self.botao1.place(x=40, y=280)

        self.botao2 = Button(image= self.numero2, width=x, height=y,command=lambda:self.num(2),bd=0)
        self.botao2.place(x=130, y=280)

        self.botao3 = Button(image=self.numero3, width=x, height=y,command=lambda:self.num(3),bd=0)
        self.botao3.place(x=220, y=280)

        self.botao4 = Button(image=self.numero4, width=x, height=y,command=lambda:self.num(4),bd=0)
        self.botao4.place(x=40, y=190)

        self.botao5 = Button(image=self.numero5, width=x, height=y,command=lambda:self.num(5),bd=0)
        self.botao5.place(x=130, y=190)

        self.botao6 = Button(image=self.numero6, width=x, height=y,command=lambda:self.num(6),bd=0)
        self.botao6.place(x=220, y=190)

        self.botao7 = Button(image=self.numero7, width=x, height=y,command=lambda:self.num(7),bd=0)
        self.botao7.place(x=40, y=100)

        self.botao8 = Button(image=self.numero8, width=x, height=y,command=lambda:self.num(8),bd=0)
        self.botao8.place(x=130, y=100)

        self.botao9 = Button(image=self.numero9, width=x, height=y,command=lambda:self.num(9),bd=0)
        self.botao9.place(x=220, y=100)

        self.botaoce = Button(image= self.button_ce, width=x, height=y,command=self.apagar,bd=0)
        self.botaoce.place(x=40, y=370)

        self.botaomenos = Button(image=self.button_menos, width=x, height=y,command=self.menos,bd=0)
        self.botaomenos.place(x=310, y=280)

        self.botaomais = Button(image=self.button_mais, width=x, height=y,command=self.soma,bd=0)
        self.botaomais.place(x=310, y=370)

        self.botaodividir = Button(image=self.button_div, width=x, height=y,command=self.div,bd=0)
        self.botaodividir.place(x=310, y=100)

        self.botaomultiplicar = Button(image=self.button_mult, width=x, height=y,command=self.mult,bd=0)
        self.botaomultiplicar.place(x=310, y=190)

        self.botaoigual = Button(image=self.button_igual, width=x, height=y,command=self.result,bd=0)
        self.botaoigual.place(x=220, y=370)

    def num(self, numero):
        if self.mate == '':
            if len(self.lista) < 12:
                self.lista.append(numero)
                textolista = ' '.join(map(str, self.lista))
                self.visor.config(text=textolista)
            print(self.prinum)
        else:
            if len(self.lista2) < 12:
                self.lista2.append(numero)
                textolista2 = ' '.join(map(str, self.lista2))
                self.visor.config(text=textolista2)
        print(f'Lista 1 {self.lista}')
        print(f'Lista 2 {self.lista2}')

    def soma(self):
        self.mate = 'soma'
        self.visor.config(text= '+')

    def div(self):
        self.mate = 'div'
        self.visor.config(text='/')

    def mult(self):
        self.mate = 'mult'
        self.visor.config(text='x')

    def menos(self):
        self.mate = 'menos'
        self.visor.config(text='-')

    def result(self):
        print('igual')
        try:
            self.prinum = int(''.join(map(str,self.lista)))  # os numeros são transformados em strings para funcionar o join e depois, são transformadas em int denovo
            self.segnum = int(''.join(map(str, self.lista2)))  # o join junta as strings
        except ValueError:
            print('Error: A digitação está errada!')
        print(self.prinum)
        print(self.segnum)

        if self.mate == 'soma':
            resultado = self.prinum + self.segnum
            self.visor.config(text=resultado)
            print('soma')

        if self.mate == 'div':
            resultado = self.prinum / self.segnum
            self.visor.config(text=resultado)
            print('div')

        if self.mate == 'menos':
            resultado = self.prinum - self.segnum
            self.visor.config(text=resultado)
            print('menos')

        if self.mate == 'mult':
            resultado = self.prinum * self.segnum
            self.visor.config(text=resultado)
            print('mult')
        self.mate = ''

    def apagar(self):
            self.visor.config(text=0)
            self.mate = ''
            self.lista = []
            self.lista2 = []

janela = Tk()
calculadoraApp(janela)
janela.mainloop()

#problema, a calculadora só consegue fazer 1 conta de cada vez. EX: se o usuario fazer 100 + 100 +100, vai da erro, pq ela so consegue fazer 100 + 100.