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
        self.ventana.config(bg='#222831', menu=self.barraMenu)
        #self.ventana.resizable(width=0, height=0)            
        
        self.barraMenu.add_cascade(label="Menu",)
        self.barraMenu.add_cascade(label="Nosotros", command=self.nosotros) 
        self.barraMenu.add_cascade(label="Carta") 
        self.barraMenu.add_cascade(label="Contacto") 

        logo =utl.leer_imagen("./imagenes/logoChurrasqueria.png", (200, 200))
        label = tk.Label( self.ventana, image=logo,bg='#222831' )
        label.place(x=300,y=0)
        
        logo1 =utl.leer_imagen("./imagenes/pokemon.png", (200, 200))
        label = tk.Label( self.ventana, image=logo1,bg='#222831' )
        label.place(x=0,y=0)

        self.ventana.mainloop()