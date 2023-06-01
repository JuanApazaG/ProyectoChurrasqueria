#importamos
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel

class App:

    #creamos un metodo para hacer la verificacion de la contraseña
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu == "root" and password == "1234") :
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message= "La contraseña no es correcta", title="Mensaje")

    #constructor
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width =0, height =0)
        utl.centrar_ventana(self.ventana, 800, 500)

        #creamos nuestro logo 
        logo = utl.leer_imagen("./imagenes/twitch.png", (200, 200))
        #traemos nuestro panel
        #frame_logo
        frame_logo = tk.Frame(self.ventana, bd =0, width = 300 , relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side="left", expand=tk.NO, fill = tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg = "#3a7ff6")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #generamos otro segundo panel
        #frame_form
        frame_form = tk.Frame(self.ventana, bd =0, relief=tk.SOLID, bg='red')
        frame_form.pack(side="right", expand=tk.YES,fill=tk.BOTH)

        #agregamos nuestro titulo
        frame_form_top = tk.Frame(frame_form, height = 50, bd =0 ,relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text = "Inicio de sesion", font=('Times', 30), fg="#002fca", bg='#fcfcfc',pady=50)
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

        #creamos el boton iniciar sesion
        inicio = tk.Button(frame_form_fill, text="Iniciar sesion", font=('Times', 15, BOLD),bg='#3a7ff6', bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill = tk.X, padx =20, pady= 5)
        #el bind es para cachar un evento si le damos click verificamos con un lambda se llama a la funcion 
        inicio.bind("<Return>", (lambda event: self.verificar()))

        self.ventana.mainloop()


