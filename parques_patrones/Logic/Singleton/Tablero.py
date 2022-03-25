import Tablero

class Tablero:
    __tablero:Tablero

    def getInstance(self):
        if(self.__tablero is None):
            self.__tablero=Tablero()
        return self.__tablero