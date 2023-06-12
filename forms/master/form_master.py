import tkinter as tk
from tkinter import*
from tkinter.font import BOLD
import util.generic as utl
from forms.master.ventana_nosotros import nosotros

class MasterPanel:

    def nosotros(self):
        self.ventana.destroy()
        nosotros()

    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.barraMenu = tk.Menu(self.ventana)
        self.ventana.config(bg='#fcfcfc', menu=self.barraMenu)
        #self.ventana.resizable(width=0, height=0)            
        
        self.barraMenu.add_cascade(label="menu",)
        self.barraMenu.add_cascade(label="nosotros", command=self.nosotros) 
        self.barraMenu.add_cascade(label="Empleados") 
        self.barraMenu.add_cascade(label="informe") 
        
        logo =utl.leer_imagen("./imagenes/pokemon.png", (200, 200))
        

        label = tk.Label( self.ventana, image=logo,bg='#3a7ff6' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        


        self.ventana.mainloop()