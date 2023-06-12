import tkinter as tk
from tkinter import ttk
from tkinter import*
from tkinter import filedialog
from tkinter.font import BOLD
from tkinter import ttk,messagebox
import util.generic as utl
import forms.master.form_master as mas

class nosotros:

    def Menu(self):
        self.ventana.destroy()
        mas.MasterPanel()

    def __init__(self):        
     

        self.ventana = tk.Tk()                             
        self.ventana.title('Nosotros')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.barraMenu = tk.Menu(self.ventana)
        self.ventana.config(bg='#fcfcfc', menu=self.barraMenu)

        self.barraMenu.add_cascade(label="menu",command=self.Menu)        
        self.barraMenu.add_cascade(label="nosotros") 
        self.barraMenu.add_cascade(label="empleados") 
        self.barraMenu.add_cascade(label="informe") 

       
       
        #aqui creamos la barra scroll para bajar y subir una lisbox
        listbox = tk.Listbox()
        listbox.insert(tk.END, *(f"Elemento {i}" for i in range(100)))
        scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)
        listbox.pack(expand=tk.YES, fill=tk.BOTH)
        scrollbar.place(x=1500,y=10,height=725)


        self.ventana.mainloop()