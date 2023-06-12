import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import tkinter.font as tkFont
import util.generic as utl

class FormLoginDesigner():
        
    def verificar(self):
        pass
    
    def userRegister(self):
        pass
    
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

        logo = utl.leer_imagen("./imagenes/logoChurrasqueria.png", (200, 200))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300,
                              relief=tk.SOLID, padx=10, pady=10, bg='#222831')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#222831')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=(
            'Impact', 30, "italic"), fg="#d46c91", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=(
            'Georgia', 14), fg="#d46c91", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14), textvariable="hola")
        self.usuario.insert(0, "agustin")
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=(
            'Georgia', 14), fg="#d46c91", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.insert(0, "1234")
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesion", font=(
            'Georgia', 15), bg='#d46c91', bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))
        
        
        inicio = tk.Button(frame_form_fill, text="Registrar usuario", font=(
            'Georgia', 15), bg='#d46c91', bd=0, fg="#fff", command=self.userRegister)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.userRegister()))
        
        # end frame_form_fill
        self.ventana.mainloop()
