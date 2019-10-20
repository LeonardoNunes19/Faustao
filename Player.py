class Player:
    def __init__(self,nome):
        self.__carteira = 100
        self.__valor = int()
        self.__nome = nome
        self.__numerosAposta = []
        self.__nroPassaVez = 0
    
    def setDinheiroCarteira(self,x):
        if self.__carteira + x < 0:
            pass
        else:
            self.__carteira += x
    
    def setNroPassaVez(self,x):
        self.__nroPassaVez += x

    def getNroPassaVez(self):
        return self.__nroPassaVez

    def clearNroPassaVez(self):
        self.__nroPassaVez = 0

    def setNumerosAposta(self,x):
        self.__numerosAposta.append(x)

    def getNumerosAposta(self):
        return self.__numerosAposta
    
    def setValorAposta_Player(self,valor):
        self.__valor += valor

    def getValorAposta_Player(self):
        return self.__valor

    def getNome_Player(self):
        return self.__nome

    def limparApostas(self):
        self.__numerosAposta = []

    def getCarteira_Player(self):
        return self.__carteira