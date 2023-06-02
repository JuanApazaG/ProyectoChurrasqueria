#importamos
import tkinter as tk
from tkinter import ttk
import util.generic as utl

class FormRegisterDesigner  :
    def register():
        pass

    #constructor
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title('Inicio de sesion')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width =0, height =0)
        utl.centrar_ventana(self.ventana, 600, 480)

        #creamos nuestro logo 
        logo = utl.leer_imagen("./imagenes/twitch.png", (200, 200))
        #traemos nuestro panel
        #frame_logo
        frame_logo = tk.Frame(self.ventana, bd =0, width = 200 , relief=tk.SOLID, padx=10, pady=10, bg='#123a42')
        frame_logo.pack(side="left", expand=tk.NO, fill = tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg = "#123a42")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #generamos otro segundo panel
        #frame_form
        frame_form = tk.Frame(self.ventana, bd =0, relief=tk.SOLID, bg='red')
        frame_form.pack(side="right", expand=tk.YES,fill=tk.BOTH)

        #agregamos nuestro titulo
        frame_form_top = tk.Frame(frame_form, height = 50, bd =0 ,relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text = "Registro de usuario", font=('Times', 30), fg="#002fca", bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #fin frame_form_top

        #generamos el frame que esta hacia abajo
        frame_form_fill = tk.Frame(frame_form, height = 50, bd=0, relief = tk.SOLID, bg='red')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill = tk.BOTH)

        #usuario 
        etiqueta_usuario = tk.Label(frame_form_fill, text = "Usuario", font=('Times', 14), fg="#002fca", bg='black', anchor = "w")
        etiqueta_usuario.pack(fill = tk.X, padx = 20, pady = 5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx = 20, pady = 10)

        #para la contraseña
        etiqueta_password = tk.Label(frame_form_fill, text = "Contraseña", font=('Times', 14), fg="#002fca", bg='black', anchor = "w")
        etiqueta_password.pack(fill = tk.X, padx = 20, pady = 5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx = 20, pady = 10)
        self.password.config(show="*")

        etiqueta_confirmation= tk.Label(frame_form_fill, text = "Confirmacion", font=('Times', 14), fg="#666a88", bg='black', anchor = "w")
        etiqueta_confirmation.pack(fill = tk.X, padx = 20, pady = 5)
        self.confirmation = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.confirmation.pack(fill=tk.X, padx = 20, pady = 10)
        self.confirmation.config(show="*")
        
        #creamos otro boton
        register = tk.Button(frame_form_fill, text="Registrar", font=('Times', 15),bg='#983508', bd=0, fg="#fff", command=self.register)
        register.pack(fill = tk.X, padx =20, pady= 20)
        #el bind es para cachar un evento si le damos click verificamos con un lambda se llama a la funcion 
        register.bind("<Return>", (lambda event: self.register()))

        self.ventana.mainloop()


