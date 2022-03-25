import Ficha
import Dado

class Jugador:
    __nombre:str
    __nroIntentos:int
    __fichas = []
    __carcel = []
    __won = []
    def __init__(self, nombre:str):
        self.__nombre = nombre
        for i in range (1,4):
            newFicha = Ficha(i)
            self.__fichas.append(newFicha)
            self.__carcel.append(newFicha)

    def tirarDados(self):
        retorno = []
        retorno[0] = Dado.tirar()
        retorno[1] = Dado.tirar()
        return retorno