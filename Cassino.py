from tkinter import *
import tkinter as tk
from Player import Player
from Roulette import Roulette

class Cassino:
    def __init__(self, master):
        self.__players = []
        self.__budget = 1000
        self.__vez = 0
        self.__nroPassaVez = 0
        self.__tipoJogo = str()
        self.__nroSorteado = int()
        self.__nroJogadores = int()
        self.__roulette = Roulette()
        self.widgets()
        
    def widgets(self):
        # Tipo de jogo
        self.__root = root.geometry("800x600+200+200")
        self.__b1 = tk.Button(root, text="AMERICANO", width=8, height=2, command=lambda:self.setTipoJogo("AMERICANO"))
        self.__b1.place(x=100,y=200)
        self.__b2 = tk.Button(root, text="EUROPEU", width=8, height=2, command=lambda:self.setTipoJogo("EUROPEU"))
        self.__b2.place(x=100,y=250)
        self.__b3 = tk.Button(root, text="FRANCÊS", width=8, height=2, command=lambda:self.setTipoJogo("FRANCES"))
        self.__b3.place(x=100,y=300)
        self.__lb1 = tk.Label(root)

        self.__lb1.configure(text="{}".format(self.getTipoJogo()), width=13, height=1, font="Times 25 bold", fg="black", bg="red")
        self.__lb1.place(x=200,y=250)
        # Budget cassino (no método de pagamento colocar isso tbm pra atualizar)
        self.__lb2 = tk.Label(root)
        self.__lb2.configure(text="{}".format(self.__budget), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
        self.__lb2.place(x=630,y=5)
        # Iniciar o jogo, sair do hub principal e ir pro game
        self.__b4 = tk.Button(root, text="INICIAR", width=8, height=2,command=lambda: self.changeWindow())
        self.__b4.place(x=650,y=550)
        # Nro de jogadores
        self.__b5 = tk.Button(root, text="1", width=3, height=2,command=lambda: self.setNroJogadores(1))
        self.__b5.place(x=430,y=250)
        self.__b5 = tk.Button(root, text="2", width=3, height=2,command=lambda: self.setNroJogadores(2))
        self.__b5.place(x=430,y=300)

        self.__lb3 = tk.Label(root)
        self.__lb3.configure(text="{}".format(self.getNrojogadores()), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
        self.__lb3.place(x=530,y=250)
        
    def changeWindow(self):
        if self.__tipoJogo == 'EUROPEU':
            self.europeu()
        elif self.__tipoJogo == 'FRANCES':
            self.frances()
        elif self.__tipoJogo == 'AMERICANO':
            self.americano()
    
    def setTipoJogo(self,tipo):
        self.__tipoJogo = tipo
        self.__roulette.setType_Roulette(tipo)
        self.__lb1.configure(text="{}".format(self.getTipoJogo()), width=13, height=1, font="Times 25 bold", fg="black", bg="red")
        self.__lb1.place(x=200,y=250)

    def getTipoJogo(self):
        return self.__tipoJogo

    def setNroJogadores(self,nro):
        self.__nroJogadores = nro
        self.__lb3.configure(text="{}".format(self.getNrojogadores()), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
        self.__lb3.place(x=530,y=250)

    def getNrojogadores(self):
        return self.__nroJogadores
    
    def criarPlayers(self):
        a = self.__nroJogadores
        name_players = ["Leonardo","Carol"]
        for i in range(0, a):
            name_players[i] = Player(name_players[i])
            b = name_players[i]
            self.__players.append(b)

    def ignorar(self):
        pass

    def botoesAposta(self):
        lista1 = [3,6,9,12,15,18,21,24,27,30,33,36]
        lista2 = [2,5,8,11,14,17,20,23,26,29,32,35]
        lista3 = [1,4,7,10,13,16,19,22,25,28,31,34]
        if self.__tipoJogo == "AMERICANO":
            self.__b7 = tk.Button(root, text="00", width=1, height=1,command=lambda: self.apostarNro('00'))
            self.__b7.place(x=32,y=350)
            self.__b7 = tk.Button(root, text="00,0,1,2,3", width=6, height=1,command=lambda:self.apostaExterna(13))
            self.__b7.place(x=0,y=400)
        else:
            self.__b7 = tk.Button(root, text="00", width=1, height=1,command=lambda:self.ignorar())
            self.__b7.place(x=32,y=350)
            self.__b7 = tk.Button(root, text="00,0,1,2,3", width=6, height=1,command=lambda:self.ignorar())
            self.__b7.place(x=0,y=400)

        self.__b7 = tk.Button(root, text="LIMPAR", width=5, height=1,command=lambda:self.limparApostas())
        self.__b7.place(x=550,y=550)

        self.__b7 = tk.Button(root, text="0", width=1, height=1,command=lambda:self.apostarNro(0))
        self.__b7.place(x=32,y=452)
        self.__b7 = tk.Button(root, text="1", width=1, height=1,command=lambda:self.apostarNro(1))
        self.__b7.place(x=73,y=460)
        self.__b7 = tk.Button(root, text="2", width=1, height=1,command=lambda:self.apostarNro(2))
        self.__b7.place(x=73,y=400)
        self.__b7 = tk.Button(root, text="3", width=1, height=1,command=lambda:self.apostarNro(3))
        self.__b7.place(x=73,y=340)
        self.__b7 = tk.Button(root, text="4", width=1, height=1,command=lambda:self.apostarNro(4))
        self.__b7.place(x=112,y=460)
        self.__b7 = tk.Button(root, text="5", width=1, height=1,command=lambda:self.apostarNro(5))
        self.__b7.place(x=112,y=400)
        self.__b7 = tk.Button(root, text="6", width=1, height=1,command=lambda:self.apostarNro(6))
        self.__b7.place(x=112,y=340)
        self.__b7 = tk.Button(root, text="7", width=1, height=1,command=lambda:self.apostarNro(7))
        self.__b7.place(x=151,y=460)
        self.__b7 = tk.Button(root, text="8", width=1, height=1,command=lambda:self.apostarNro(8))
        self.__b7.place(x=151,y=400)
        self.__b7 = tk.Button(root, text="9", width=1, height=1,command=lambda:self.apostarNro(9))
        self.__b7.place(x=151,y=340)
        self.__b7 = tk.Button(root, text="10", width=1, height=1,command=lambda:self.apostarNro(10))
        self.__b7.place(x=190,y=460)
        self.__b7 = tk.Button(root, text="11", width=1, height=1,command=lambda:self.apostarNro(11))
        self.__b7.place(x=190,y=400)
        self.__b7 = tk.Button(root, text="12", width=1, height=1,command=lambda:self.apostarNro(12))
        self.__b7.place(x=190,y=340)
        self.__b7 = tk.Button(root, text="13", width=1, height=1,command=lambda:self.apostarNro(13))
        self.__b7.place(x=230,y=460)
        self.__b7 = tk.Button(root, text="14", width=1, height=1,command=lambda:self.apostarNro(14))
        self.__b7.place(x=230,y=400)
        self.__b7 = tk.Button(root, text="15", width=1, height=1,command=lambda:self.apostarNro(15))
        self.__b7.place(x=230,y=340)
        self.__b7 = tk.Button(root, text="16", width=1, height=1,command=lambda:self.apostarNro(16))
        self.__b7.place(x=270,y=460)
        self.__b7 = tk.Button(root, text="17", width=1, height=1,command=lambda:self.apostarNro(17))
        self.__b7.place(x=270,y=400)
        self.__b7 = tk.Button(root, text="18", width=1, height=1,command=lambda:self.apostarNro(18))
        self.__b7.place(x=270,y=340)
        self.__b7 = tk.Button(root, text="19", width=1, height=1,command=lambda:self.apostarNro(19))
        self.__b7.place(x=310,y=460)
        self.__b7 = tk.Button(root, text="20", width=1, height=1,command=lambda:self.apostarNro(20))
        self.__b7.place(x=310,y=400)
        self.__b7 = tk.Button(root, text="21", width=1, height=1,command=lambda:self.apostarNro(21))
        self.__b7.place(x=310,y=340)
        self.__b7 = tk.Button(root, text="22", width=1, height=1,command=lambda:self.apostarNro(22))
        self.__b7.place(x=350,y=460)
        self.__b7 = tk.Button(root, text="23", width=1, height=1,command=lambda:self.apostarNro(23))
        self.__b7.place(x=350,y=400)
        self.__b7 = tk.Button(root, text="24", width=1, height=1,command=lambda:self.apostarNro(24))
        self.__b7.place(x=350,y=340)
        self.__b7 = tk.Button(root, text="25", width=1, height=1,command=lambda:self.apostarNro(25))
        self.__b7.place(x=390,y=460)
        self.__b7 = tk.Button(root, text="26", width=1, height=1,command=lambda:self.apostarNro(26))
        self.__b7.place(x=390,y=400)
        self.__b7 = tk.Button(root, text="27", width=1, height=1,command=lambda:self.apostarNro(27))
        self.__b7.place(x=390,y=340)
        self.__b7 = tk.Button(root, text="28", width=1, height=1,command=lambda:self.apostarNro(28))
        self.__b7.place(x=430,y=460)
        self.__b7 = tk.Button(root, text="29", width=1, height=1,command=lambda:self.apostarNro(29))
        self.__b7.place(x=430,y=400)
        self.__b7 = tk.Button(root, text="30", width=1, height=1,command=lambda:self.apostarNro(30))
        self.__b7.place(x=430,y=340)
        self.__b7 = tk.Button(root, text="31", width=1, height=1,command=lambda:self.apostarNro(31))
        self.__b7.place(x=470,y=460)
        self.__b7 = tk.Button(root, text="32", width=1, height=1,command=lambda:self.apostarNro(32))
        self.__b7.place(x=470,y=400)
        self.__b7 = tk.Button(root, text="33", width=1, height=1,command=lambda:self.apostarNro(33))
        self.__b7.place(x=470,y=340)
        self.__b7 = tk.Button(root, text="34", width=1, height=1,command=lambda:self.apostarNro(34))
        self.__b7.place(x=510,y=460)
        self.__b7 = tk.Button(root, text="35", width=1, height=1,command=lambda:self.apostarNro(35))
        self.__b7.place(x=510,y=400)
        self.__b7 = tk.Button(root, text="36", width=1, height=1,command=lambda:self.apostarNro(36))
        self.__b7.place(x=510,y=340)
        # Aposta externa
        self.__b7 = tk.Button(root, text="2 for 1", width=5, height=1,command=lambda:self.apostaExterna(1))
        self.__b7.place(x=600,y=340)
        self.__b7 = tk.Button(root, text="2 for 1", width=5, height=1,command=lambda:self.apostaExterna(2))
        self.__b7.place(x=600,y=400)
        self.__b7 = tk.Button(root, text="2 for 1", width=5, height=1,command=lambda:self.apostaExterna(3))
        self.__b7.place(x=600,y=460)
        self.__b7 = tk.Button(root, text="1st to 12", width=15, height=1,command=lambda:self.apostaExterna(4))
        self.__b7.place(x=75,y=511)
        self.__b7 = tk.Button(root, text="2hd to 12", width=15, height=1,command=lambda:self.apostaExterna(5))
        self.__b7.place(x=233,y=511)
        self.__b7 = tk.Button(root, text="3rd to 12", width=15, height=1,command=lambda:self.apostaExterna(6))
        self.__b7.place(x=389,y=511)
        self.__b7 = tk.Button(root, text="1-18", width=5, height=1,command=lambda:self.apostaExterna(7))
        self.__b7.place(x=76,y=550)
        self.__b7 = tk.Button(root, text="19-36", width=5, height=1,command=lambda:self.apostaExterna(8))
        self.__b7.place(x=469,y=550)
        self.__b7 = tk.Button(root, text="EVEN", width=5, height=1,command=lambda:self.apostaExterna(9))
        self.__b7.place(x=156,y=550)
        self.__b7 = tk.Button(root, text="ODD", width=5, height=1,command=lambda:self.apostaExterna(10))
        self.__b7.place(x=389,y=550)
        self.__b7 = tk.Button(root, text="", width=5, height=1,bg="red",command=lambda:self.apostaExterna(11))
        self.__b7.place(x=234,y=550)
        self.__b7 = tk.Button(root, text="", width=5, height=1,bg="black",command=lambda:self.apostaExterna(12))
        self.__b7.place(x=314,y=550)


    def botoesValor(self):
        self.__b8 = tk.Button(root, text="1", width=2, height=1,command=lambda:self.apostarValor(1))
        self.__b8.place(x=32,y=200)
        self.__b8 = tk.Button(root, text="5", width=2, height=1,command=lambda:self.apostarValor(5))
        self.__b8.place(x=90,y=200)
        self.__b8 = tk.Button(root, text="10", width=2, height=1,command=lambda:self.apostarValor(10))
        self.__b8.place(x=148,y=200)
        self.__b8 = tk.Button(root, text="25", width=2, height=1,command=lambda:self.apostarValor(25))
        self.__b8.place(x=206,y=200)
        self.__b8 = tk.Button(root, text="100", width=2, height=1,command=lambda:self.apostarValor(100))
        self.__b8.place(x=264,y=200)

    def europeu(self):
        # atualizar o fundo para inserir novos botões
        if self.getNrojogadores() != 0:
            self.photo = PhotoImage(file="european3.gif")
            self.blacklabel = Label(root,image=self.photo).place(x=-1,y=-1)
        # carregar budget cassino
            self.__lb4 = tk.Label(root)
            self.__lb4.configure(text="{}".format(self.__budget), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
            self.__lb4.place(x=630,y=5)
        # label do numero sorteado
            self.__lb7 = tk.Label(root)
            self.__lb7.configure(text="AGUARDE", width=20, height=1, font="Times 12 bold", fg="black", bg="red")
            self.__lb7.place(x=320,y=50)
        # botões para fazer aposta dos números
            self.botoesAposta()
        # botões para fazer aposta do dinheiro
            self.botoesValor()
        # carregamento de funções
            self.criarPlayers()
            self.confirmarAposta()
            self.loadGetCarteiraPlayer()
            self.loadNomePlayers()

    def americano(self):
        # atualizar o fundo para inserir novos botões
        if self.getTipoJogo() == "AMERICANO" and self.getNrojogadores() != 0:
            self.photo = PhotoImage(file="european3.gif")
            self.blacklabel = Label(root,image=self.photo).place(x=-1,y=-1)
        # carregar budget cassino
            self.__lb4 = tk.Label(root)
            self.__lb4.configure(text="{}".format(self.__budget), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
            self.__lb4.place(x=630,y=5)
        # label do numero sorteado
            self.__lb7 = tk.Label(root)
            self.__lb7.configure(text="AGUARDE", width=20, height=1, font="Times 12 bold", fg="black", bg="red")
            self.__lb7.place(x=320,y=50)
        # botões para fazer aposta dos números
            self.botoesAposta()
        # botões para fazer aposta do dinheiro
            self.botoesValor()
        # carregamento de funções
            self.criarPlayers()
            self.confirmarAposta()
            self.loadGetCarteiraPlayer()
            self.loadNomePlayers()
        
    def frances(self):
        # atualizar o fundo para inserir novos botões
        if self.getTipoJogo() == "FRANCES" and self.getNrojogadores() != 0:
            self.photo = PhotoImage(file="european3.gif")
            self.blacklabel = Label(root,image=self.photo).place(x=-1,y=-1)
        # carregar budget cassino
            self.__lb4 = tk.Label(root)
            self.__lb4.configure(text="{}".format(self.__budget), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
            self.__lb4.place(x=630,y=5)
        # label do numero sorteado
            self.__lb7 = tk.Label(root)
            self.__lb7.configure(text="AGUARDE", width=20, height=1, font="Times 12 bold", fg="black", bg="red")
            self.__lb7.place(x=320,y=50)
        # botões para fazer aposta dos números
            self.botoesAposta()
        # botões para fazer aposta do dinheiro
            self.botoesValor()
        # carregamento de funções
            self.criarPlayers()
            self.confirmarAposta()
            self.loadGetCarteiraPlayer()
            self.loadNomePlayers()

    def apostarValor(self,x):
        self.__players[self.__vez].clearNroPassaVez()
        self.__b5.configure(state="normal")
        self.__players[self.__vez].setDinheiroCarteira(-x)
        self.__players[self.__vez].setValorAposta_Player(x) 
        # self.__players[self.__vez]
        carteira = (self.__players[self.__vez].getCarteira_Player())        
        self.__lb5.configure(text="{}".format(carteira), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
    
    def apostarNro(self,x):
        if x not in self.__players[self.__vez].getNumerosAposta():
            self.__players[self.__vez].setNumerosAposta(x)
        elif x in self.__players[self.__vez].getNumerosAposta():
            print("o número já foi apostado")
        print(self.__players[self.__vez].getNumerosAposta())

    def apostaExterna(self,x):
        if x == 1:
            self.__players[self.__vez].setNumerosAposta("2for1 1")
        
        if x == 2:
            self.__players[self.__vez].setNumerosAposta("2for1 2")

        if x == 3:
            self.__players[self.__vez].setNumerosAposta("2for1 3")

        if x == 4:
            self.__players[self.__vez].setNumerosAposta("1st12")

        if x == 5:
            self.__players[self.__vez].setNumerosAposta("2hd12")

        if x == 6:
            self.__players[self.__vez].setNumerosAposta("3rd12")

        if x == 7:
            self.__players[self.__vez].setNumerosAposta("1-18")

        if x == 8:
            self.__players[self.__vez].setNumerosAposta("19-36")

        if x == 9:
            self.__players[self.__vez].setNumerosAposta("even")

        if x == 10:
            self.__players[self.__vez].setNumerosAposta("odd")

        if x == 11:
            self.__players[self.__vez].setNumerosAposta("red")

        if x == 12:
            self.__players[self.__vez].setNumerosAposta("black")

        if x == 13:
            self.__players[self.__vez].setNumerosAposta("especial")
            
        print(self.__players[self.__vez].getNumerosAposta())

    def loadGetCarteiraPlayer(self):
        carteira = (self.__players[self.__vez].getCarteira_Player())
        self.__lb5 = tk.Label(root)
        self.__lb5.configure(text="{}".format(carteira), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
        self.__lb5.place(x=630,y=50)

    def loadNomePlayers(self):
        nome = (self.__players[self.__vez].getNome_Player())
        self.__lb6 = tk.Label(root)
        self.__lb6.configure(text="{}".format(nome), width=10, height=1, font="Times 25 bold", fg="black", bg="red")
        self.__lb6.place(x=50,y=50)
    
    def confirmarAposta(self):
        self.__b5 = tk.Button(root, text="APOSTAR", width=5, height=1,command=lambda: self.addVez())
        self.__b5.place(x=650,y=550)

    def addVez(self):
        self.__vez += 1
        if self.__vez == len(self.__players):
            self.__vez = 0
            self.__nroSorteado = self.__roulette.getResult_Roulette()
            self.payment()
            self.retiraPlayer()
            self.limparApostas()
            self.mostrarNroSorteadoAnterior()
        if self.__budget < 0 or len(self.__players) <= 0:
            self.endGame()
        self.passaVez()
        self.atualizarValores()

    def mostrarNroSorteadoAnterior(self):
        self.__lb7.configure(text="{}".format(self.__nroSorteado), width=20, height=1, font="Times 12 bold", fg="black", bg="red")
        
    def passaVez(self):
        # se eu não apertar nenhum botão de aposta, então passavez += 1
        self.__players[self.__vez].setNroPassaVez(1)
        if self.__players[self.__vez].getNroPassaVez() == 3:
            self.__b5.configure(state="disabled")

    def endGame(self):
        self.photo = PhotoImage(file="black.gif")
        self.blacklabel = Label(root,image=self.photo).place(x=-1,y=-1)

        self.__lb9 = tk.Label(root)
        self.__lb9.configure(text="FIM DE JOGO! FECHE PARA VOLTAR", width=50, height=2, font="Times 15 bold", fg="black", bg="red")
        self.__lb9.place(x=150,y=250)

    def girarRoleta(self):
        pass

    def payment(self):
        lista1 = [3,6,9,12,15,18,21,24,27,30,33,36]
        lista2 = [2,5,8,11,14,17,20,23,26,29,32,35]
        lista3 = [1,4,7,10,13,16,19,22,25,28,32,34]
        
        firstTwelve = [1,2,3,4,5,6,7,8,9,10,11,12]
        secondTwelve = [13,14,15,16,17,18,19,20,21,22,23,24]
        thirdTwelve = [25,26,27,28,29,30,31,32,33,34,35,36]

        oneToEighteen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        nineteenToThirdSix = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

        even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
        odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]

        red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

        especial = ['00',0,1,2,3]

        for player in self.__players:
            interna = []
            externa = []
            lenNrosAposta = len(player.getNumerosAposta())
            
            for n in player.getNumerosAposta():
                if type(n) == int:
                    interna.append(n)
                else:
                    externa.append(n)

            # apostas internas
            if self.__nroSorteado in interna and len(interna) == 1:
                player.setDinheiroCarteira(player.getValorAposta_Player() * 36)
                self.__budget -= (player.getValorAposta_Player() * 36)
            
            if self.__nroSorteado in interna and len(interna) == 2:
                player.setDinheiroCarteira(player.getValorAposta_Player() * 18)
                self.__budget -= (player.getValorAposta_Player() * 18)
            
            if self.__nroSorteado in interna and len(interna) == 3:
                player.setDinheiroCarteira(player.getValorAposta_Player() * 12)
                self.__budget -= (player.getValorAposta_Player() * 12)
            
            if self.__nroSorteado in interna and len(interna) == 4:
                player.setDinheiroCarteira(player.getValorAposta_Player() * 9)
                self.__budget -= (player.getValorAposta_Player() * 9)
            
            if self.__nroSorteado in interna and len(interna) == 5:
                player.setDinheiroCarteira(player.getValorAposta_Player() * 7)
                self.__budget -= (player.getValorAposta_Player() * 7)
            
            if self.__nroSorteado in interna and len(interna) == 6:
                player.setDinheiroCarteira(player.getValorAposta_Player() * 6)
                self.__budget -= (player.getValorAposta_Player() * 6)

            if self.__tipoJogo == "FRANCES" and self.__nroSorteado == 0 and 0 not in player.getNumerosAposta():
                self.__budget +=  (player.getValorAposta_Player() / 2)
                player.setDinheiroCarteira(player.getValorAposta_Player() / 2)

            # apostas externas:
            if (self.__nroSorteado in lista1 and "2for1 1" in player.getNumerosAposta()) or (self.__nroSorteado in lista2 and "2for1 2" in player.getNumerosAposta()) or (self.__nroSorteado in lista3 and "2for1 3" in player.getNumerosAposta()):
                player.setDinheiroCarteira(player.getValorAposta_Player() * 3)
                self.__budget -= (player.getValorAposta_Player() * 3)
            
            if (self.__nroSorteado in firstTwelve and "1st12" in player.getNumerosAposta()) or (self.__nroSorteado in secondTwelve and "2hd12" in player.getNumerosAposta()) or (self.__nroSorteado in thirdTwelve and "3rd12" in player.getNumerosAposta()):
                player.setDinheiroCarteira(player.getValorAposta_Player() * 3)
                self.__budget -= (player.getValorAposta_Player() * 3)
                
            if (self.__nroSorteado in oneToEighteen and "1-18" in player.getNumerosAposta()) or (self.__nroSorteado in nineteenToThirdSix and "19-36" in player.getNumerosAposta()):
                player.setDinheiroCarteira(player.getValorAposta_Player() * 2)
                self.__budget -= (player.getValorAposta_Player() * 2)

            if (self.__nroSorteado in even and "even" in player.getNumerosAposta()) or (self.__nroSorteado in odd and "odd" in player.getNumerosAposta()):
                player.setDinheiroCarteira(player.getValorAposta_Player() * 2)
                self.__budget -= (player.getValorAposta_Player() * 2)
            
            if (self.__nroSorteado in red and "red" in player.getNumerosAposta()) or (self.__nroSorteado in black and "black" in player.getNumerosAposta()):
                player.setDinheiroCarteira(player.getValorAposta_Player() * 2)
                self.__budget -= (player.getValorAposta_Player() * 2)
            
            if (self.__nroSorteado in especial and "especial" in player.getNumerosAposta()):
                player.setDinheiroCarteira(player.getValorAposta_Player() * 7)
                self.__budget -= (player.getValorAposta_Player() * 7)

            else:
                self.__budget += player.getValorAposta_Player()
 
    def retiraPlayer(self):
        for player in self.__players:
            if player.getCarteira_Player() <= 0:
                self.__players.remove(player)

    def limparApostas(self):
        for players in self.__players:
            players.limparApostas()

    def atualizarValores(self):
        # atualização do nome do jogador da vez
        self.__lb6.configure(text="{}".format(self.__players[self.__vez].getNome_Player()), width=7, height=1, font="Times 25 bold", fg="black", bg="red")        
        # atualização da carteira do jogador da vez
        self.__lb5.configure(text="{}".format(self.__players[self.__vez].getCarteira_Player()), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
        # atualização do budget do cassino após as apostas
        self.__lb4.configure(text="{}".format(self.__budget), width=7, height=1, font="Times 25 bold", fg="black", bg="red")
        # mostrar numero sorteado dps das apostas
        self.__lb7.configure(text="{}".format(self.__nroSorteado), width=20, height=1, font="Times 12 bold", fg="black", bg="red")

root = tk.Tk()
Cassino(root)
root.mainloop()