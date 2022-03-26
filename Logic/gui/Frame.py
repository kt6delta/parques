import tkinter as tk
#import Logic.Singleton.Partida as p
#import gui.PanelControles as pc
import gui.PanelTablero as pt


class Frame():
  
  ancho="925"
  alto="648"

  def __init__(self):
    self.initTemplate()
  
  def initTemplate(self):
    ventana= tk.Tk()
    ventana.geometry(self.ancho+'x'+self.alto)
    ventana['background']='#ffe6e6'
    ventana.title('parchis')
    ventana.resizable(0,0)
    self.initComponents()
    ventana.mainloop()

  def initComponents(self):
    pt.PanelTablero()
    #pc.PanelControles(self)
    #p.Partida(self)