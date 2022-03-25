import Logic.Models.Ficha as f
import Logic.Models.Jugador as j
import Partida

class Partida:
    __turnoActual:f.Jugador
    __jugadores:list
    __instance:Partida
    def __init__(self, jugadores:list):
        self.__jugadores = jugadores
        self.__turnoActual:self.__jugadores[0]

    @staticmethod
    def getInstance():
        if(__instance == null):
            pass

    def setTurnoActual(self, turnoActual:j.Jugador):
        self.__turnoActual = turnoActual

    def getTurnoActual(self):
        return self.__turnoActual

    def getJugadores(self):
        return self.__jugadores

    def setSiguienteJugador(self):
        pos = self.__jugadores.index(self.__turnoActual)
        if((pos) == 3):
            self.__turnoActual = self.__jugadores[0];
        else:
            self.__turnoActual = self.__jugadores[pos+1];
        