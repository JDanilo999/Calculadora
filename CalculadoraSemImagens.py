#versão para copiar e colar sem a necessidade de baixar imagem.
from tkinter import *
from sympy import sympify, SympifyError
class CalculadoraApp:

    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('420x470')
        self.janela.resizable(False,False)
        self.janela.title('Calculadora.JD')
        self.janela.config(background='white')
        self.lista = list()
        self.resulta = 0
        self.botoes = list()
        # visor com label
        self.visor = Label(text='0', width=0, height=2, font=('monospace', 30, 'bold'),anchor='e',fg='black',background='white')
        self.visor.pack()
        x = 4
        y = 2
        self.botao0 = Button(text='0',font=('monospace',20,'bold'),width=x,height=y,command=lambda:self.num('0'),bd=0)
        self.botao0.place(x=130, y=370)

        self.botao1 = Button(text='1',font=('monospace',20,'bold'), width=x, height=y,command=lambda:self.num('1'),bd=0)
        self.botao1.place(x=40, y=280)

        self.botao2 = Button(text='2', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('2'),bd=0)
        self.botao2.place(x=130, y=280)

        self.botao3 = Button(text='3', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('3'),bd=0)
        self.botao3.place(x=220, y=280)

        self.botao4 = Button(text='4', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('4'),bd=0)
        self.botao4.place(x=40, y=190)

        self.botao5 = Button(text='5', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('5'),bd=0)
        self.botao5.place(x=130, y=190)

        self.botao6 = Button(text='6', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('6'),bd=0)
        self.botao6.place(x=220, y=190)

        self.botao7 = Button(text='7', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('7'),bd=0)
        self.botao7.place(x=40, y=100)

        self.botao8 = Button(text='8',font=('monospace',20,'bold'), width=x, height=y,command=lambda:self.num('8'),bd=0)
        self.botao8.place(x=130, y=100)

        self.botao9 = Button(text='9', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('9'),bd=0)
        self.botao9.place(x=220, y=100)

        self.botaoce = Button(text='CE',font=('monospace',20,'bold'), width=x, height=y,command=self.apagar,bd=0)
        self.botaoce.place(x=40, y=370)

        self.botaomenos = Button(text='-', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('-'),bd=0)
        self.botaomenos.place(x=310, y=280)

        self.botaomais = Button(text='+',font=('monospace',20,'bold'), width=x, height=y,command=lambda:self.num('+'),bd=0)
        self.botaomais.place(x=310, y=370)

        self.botaodividir = Button(text='÷', font=('monospace',20,'bold'),width=x, height=y,command=lambda:self.num('/'),bd=0)
        self.botaodividir.place(x=310, y=100)

        self.botaomultiplicar = Button(text='x',font=('monospace',20,'bold'), width=x, height=y,command=lambda:self.num('*'),bd=0)
        self.botaomultiplicar.place(x=310, y=190)

        self.botaoigual = Button(text='=',font=('monospace',20,'bold'), width=x, height=y,command=self.result,bd=0)
        self.botaoigual.place(x=220, y=370)
        #estilo
        self.botaoescuro = Button(text='🌙',command=self.est,width=0, height=0,bd=0)
        self.botaoescuro.place(x=198, y=0)

    def num(self, numero):
        if len(self.lista) < 12:
            self.lista.append(numero)
            textolista = ' '.join(self.lista)
            visorfiltro = textolista.replace('*','x').replace('/','÷')
            self.visor.config(text=visorfiltro)

    def result(self):
        try:
            expre = ''.join(self.lista)
            self.resulta = sympify(expre)
            self.visor.config(text=self.resulta)
            converter = str(self.resulta)
            verificar = '/' in converter
            if verificar:
                resulta = float(self.resulta.evalf())
                self.visor.config(text=resulta)
        except SympifyError:
            print('expressão matematica errada')

    def apagar(self):
        self.visor.config(text=0)
        self.lista = []
        self.resulta = 0

    def est(self):#função exclusiva dessa calculadora sem imagens, faz a funçao de mudar de tema
        self.botoes = [
            self.botao0, self.botao1, self.botao2, self.botao3,
            self.botao4, self.botao5, self.botao6, self.botao7,
            self.botao8, self.botao9, self.botaoce, self.botaomenos,
            self.botaomais, self.botaodividir, self.botaomultiplicar,
            self.botaoigual,self.botaoescuro
        ]
        cor = root.cget('background')
        if cor == 'white':
            root.config(background='black')
            for botao in self.botoes:
                botao.config(fg='white',bd=0)
                botao.config(bg='#1e1e1e',bd=0)
                self.visor.config(bg='black')
                self.visor.config(fg='white')
            print(cor)
        else:
            root.config(background='white')
            for botao in self.botoes:
                botao.config(fg='black',bd=0)
                botao.config(bg='#f0f0f0', bd=0)
                self.visor.config(bg='white')
                self.visor.config(fg='black')

root = Tk()
CalculadoraApp(root)
root.mainloop()
