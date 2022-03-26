#import Logic.Utilities.Coordenadas as c
#import Logic.Singleton.Partida as p
import gui.Frame as F

class P_tablero():
  def __init__(self):
    #c.Coordenadas.llenarCoordenadas()
    self.initComponents

  def initComponents(self):
    imagen = F.ventana.PhotoImage(file = "Resources/Tablero.png")
    tablero=F.ventana.Label(F.ventana, borderwidth = 6,idth = 40,relief="ridge",image=imagen, bd=0)
    tablero.grid(column=0, row=0, padx=10, pady=10)
