#Obs: Essa calculadora segue a ordem de calculo aritimético da matematica.(versão nova)
from tkinter import *
from sympy import sympify, SympifyError
class calculadoraApp:
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('420x470')
        self.janela.resizable(False,False)
        self.janela.title('Calculadora.JD')
        self.janela.config(background='white')
        self.lista = list()
        self.resulta = 0
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
        self.botao0 = Button(image=self.numero0,width=x,height=y,command=lambda:self.num('0'),bd=0)
        self.botao0.place(x=130, y=370)

        self.botao1 = Button(image=self.numero1, width=x, height=y,command=lambda:self.num('1'),bd=0)
        self.botao1.place(x=40, y=280)

        self.botao2 = Button(image= self.numero2, width=x, height=y,command=lambda:self.num('2'),bd=0)
        self.botao2.place(x=130, y=280)

        self.botao3 = Button(image=self.numero3, width=x, height=y,command=lambda:self.num('3'),bd=0)
        self.botao3.place(x=220, y=280)

        self.botao4 = Button(image=self.numero4, width=x, height=y,command=lambda:self.num('4'),bd=0)
        self.botao4.place(x=40, y=190)

        self.botao5 = Button(image=self.numero5, width=x, height=y,command=lambda:self.num('5'),bd=0)
        self.botao5.place(x=130, y=190)

        self.botao6 = Button(image=self.numero6, width=x, height=y,command=lambda:self.num('6'),bd=0)
        self.botao6.place(x=220, y=190)

        self.botao7 = Button(image=self.numero7, width=x, height=y,command=lambda:self.num('7'),bd=0)
        self.botao7.place(x=40, y=100)

        self.botao8 = Button(image=self.numero8, width=x, height=y,command=lambda:self.num('8'),bd=0)
        self.botao8.place(x=130, y=100)

        self.botao9 = Button(image=self.numero9, width=x, height=y,command=lambda:self.num('9'),bd=0)
        self.botao9.place(x=220, y=100)

        self.botaoce = Button(image= self.button_ce, width=x, height=y,command=self.apagar,bd=0)
        self.botaoce.place(x=40, y=370)

        self.botaomenos = Button(image=self.button_menos, width=x, height=y,command=lambda:self.num('-'),bd=0)
        self.botaomenos.place(x=310, y=280)

        self.botaomais = Button(image=self.button_mais, width=x, height=y,command=lambda:self.num('+'),bd=0)
        self.botaomais.place(x=310, y=370)

        self.botaodividir = Button(image=self.button_div, width=x, height=y,command=lambda:self.num('/'),bd=0)
        self.botaodividir.place(x=310, y=100)

        self.botaomultiplicar = Button(image=self.button_mult, width=x, height=y,command=lambda:self.num('*'),bd=0)
        self.botaomultiplicar.place(x=310, y=190)

        self.botaoigual = Button(image=self.button_igual, width=x, height=y,command=self.result,bd=0)
        self.botaoigual.place(x=220, y=370)
        #estilo
        '''
        self.botaoescuro = Button(text='Black',command=self.est)
        self.botaoescuro.place(x=325, y=0)
        '''

    def num(self, numero): #nessa função, foi implementado a captação dos numeros clicados nos respectivos botoes, que foram executados dentro de uma lambda.
        if len(self.lista) < 12: #fiz essa estrutura de condição, para limitar o numero de caracteres que seram exibido no visor(evitando contas gigantes que não cabem no visor)
            self.nume = numero#aqui capta o numero que foi executado ao clicar o respectivo botão
            self.lista.append(numero)#armazena em uma lista
            textolista = ' '.join(self.lista)#aqui junta todos os espaços que existem dentro da lista transformando em uma frase.
            self.visor.config(text=textolista)#aqui exibi os numeros que foram captados no visor.

    def result(self):#da o resultado com o auxilio de uma biblioteca sympy capaz de realizar operações seguindo a ordem aritmetica(obs: essa biblioteca consegue interpretar numeros com o tipo primitivo string)
        try:#evita que o codigo pare com erros
            expre = ''.join(self.lista)#tirei todos os espaços, para ficar igual a uma expressão.
            self.resulta = sympify(expre)#ultilizei essa expreção dentro da função simpify que interpreta a expressão e da o resultado
            self.visor.config(text=self.resulta)#mostro o resultado no visor
            #obs: resultados de divisão que apresentava resto, o simpify dava o resultado em forma de fração. por isso tive que corrigir em baixo, para que obtenha o valor total.
            converter = str(self.resulta)#aqui é um conversor que fiz, para converter a variavel self.resulta para string(A função sympify muda o tipo primitivo da variavel self.resulta, por isso fiz isso)
            verificar = '/' in converter#fiz isso para verificar se existe um '/'
            if verificar:#se retorna True, é porque existe um '/'
                resulta = float(self.resulta.evalf())#transformei o resultado em um tipo primitivo float, onde com a função poderosa evalf, transformei o resultado da fração no valor total da divisão.
                self.visor.config(text=resulta)#novamente exibi o resultado na tela
        except SympifyError:#evita que o codigo pare com erros
            print('expressão matematica errada')

    def apagar(self):#faz a funçao de apagar
        self.visor.config(text=0)
        self.lista = []
        self.resulta = 0
'''
    def est(self):
        self.botoes = [
            self.botao0, self.botao1, self.botao2, self.botao3,
            self.botao4, self.botao5, self.botao6, self.botao7,
            self.botao8, self.botao9, self.botaoce, self.botaomenos,
            self.botaomais, self.botaodividir, self.botaomultiplicar,
            self.botaoigual
        ]
        cor = janela.cget('background')
        if cor == 'white':
            janela.config(background='black')
            for botao in self.botoes:
                botao.config(bg='black',bd=0)
            print(cor)
        else:
            janela.config(background='white')
            for botao in self.botoes:
                botao.config(bg='white',bd=0)
'''
janela = Tk()
calculadoraApp(janela)
janela.mainloop()
