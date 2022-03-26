from _typeshed import Self
import Logic.Models.Ficha

class Movimiento:
    strategyC=MovimientoStrategy()

    def getStrategy(self):
        return strategyC

    def setStrategy(self,strategy): 
        Self.strategyC=strategy
    
    def moverFicha(self,fichas,valor1,valor2):
        strategyC.moverFichas(fichas,valor1,valor2)

