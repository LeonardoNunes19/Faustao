from random import randint,choice

class Roulette:
    def __init__(self):
        self.__tipoRoleta = str()

    def setType_Roulette(self,tipo):
        self.__tipoRoleta = tipo

    def getType_Roulette(self):
        return self.__tipoRoleta

    def getResult_Roulette(self):
        if self.__tipoRoleta == 'FRANCES' or self.__tipoRoleta == 'EUROPEU':
            self.__number = randint(0, 36)
            return self.__number
        elif self.__tipoRoleta == 'AMERICANO':
            lista = [00]
            lista.append(randint(0,36))
            self.__number = choice(lista)
            return self.__number
