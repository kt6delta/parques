import Logic.Utilities.Posicion as p
import Logic.Bridge.Color as c

class Casilla:
    __safe:bool
    __posicion:p.Posicion
    __fichas = []
    __color:c.Color
    def __init__(self, posicion, nameColor, safe):
        self.__safe = safe
        self.__posicion = posicion
        self.__color = nameColor

    def getPosicion(self):
        return self.__posicion

    def getFichas(self):
        return self.__fichas

    def isSafe(self):
        return self.__safe

    def toString(self):
        retorno = ""
        for i in range (len(self.__fichas)):
            retorno += "Ficha #" + i + ": " + self.__fichas[i].getiD() + " y su color es: " + self.__fichas[i].getColor().getClass() + "\n";
            return retorno;