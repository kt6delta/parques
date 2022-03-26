import Logic.Models.Casilla as c

class Ficha:
    __id:int
    __casilla:c.Casilla
    def __init__(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id

    def getCasilla(self):
        return self.__casilla

    def setCasilla(self,casilla:c.Casilla):
        self.__casilla = casilla