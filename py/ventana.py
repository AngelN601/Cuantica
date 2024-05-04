from tkinter import *
from tkinter import messagebox
from ventana_2 import Sin_Eva
from ventana_3 import Con_Eva


class Bienvenida:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Proyecto')
        self.ventana.geometry('650x750+700+100')
        self.ventana.configure(bg='black')
        self.ventana.iconbitmap(r'C:\Users\Ninja\Desktop\UNAM\7mo Semestre\Cuantica\Proyecto\py\imgs\qubit.ico')

        #Imagen
        self.fondo = PhotoImage(file = r'C:\Users\Ninja\Desktop\UNAM\7mo Semestre\Cuantica\Proyecto\py\imgs\fondo.png')
        Label(self.ventana, image=self.fondo, bg='black').pack()
        #Imagen 2
        self.fondoqubit = PhotoImage(file = r'C:\Users\Ninja\Desktop\UNAM\7mo Semestre\Cuantica\Proyecto\py\imgs\qubit.png')
        self.label4 = Label(self.ventana, image=self.fondoqubit, bg='black')
        self.label4.place(x=230,y=390)


        #Protocolo BB84
        self.label1 = Label(self.ventana, text='Protocolo BB84')
        self.label1.config(fg='White', bg='black', font=('Adale Mono Regular', 18, 'italic'))
        self.label1.place(x=260,y=140)

        #Pregunta
        self.label2 = Label(self.ventana, text='Desea la intervención de Eva?')
        self.label2.config(fg='White', bg='black', font=('Adale Mono Regular', 12, 'bold'))
        self.label2.place(x=230,y=200)

        self.label2 = Label(self.ventana, text='No=1  Si=2')
        self.label2.config(fg='White', bg='black', font=('Adale Mono Regular', 12, 'bold'))
        self.label2.place(x=300,y=220)

        #Autor
        self.label3 = Label(self.ventana, text='Creado por: Angel Brayan Gonzalez Mireles')
        self.label3.config(fg='White', bg='black', font=('Adale Mono Regular', 8, 'bold'))
        self.label3.place(x=230,y=710)        

        #Entry
        self.dato1 = IntVar()
        self.entry1 = Entry(self.ventana, bd = 2, bg = '#eee8e8', fg='black', textvariable=self.dato1)
        self.entry1.config(font=('Adale Mono Regular', 12, 'bold'), width=27)
        self.entry1.place(x=220,y=260)

        #boton
        self.boton1 = Button(self.ventana, text='Aceptar', bd = 2, bg= 'White', fg= 'black')
        self.boton1.config(font=('Adale Mono Regular', 14), width=12, command=self.acceso)
        self.boton1.place(x=270,y=310)

        self.ventana.mainloop()


    def acceso(self):
        self.largo = self.dato1.get()
        if not self.dato1.get():
            messagebox.showerror('Atencion!','Debe escoger una opcion disponible')
        elif self.largo == 1:
             self.ventana.destroy()
             Sin_Eva()
        elif self.largo == 2:
             self.ventana.destroy()
             Con_Eva()
        else:
             messagebox.showerror('Atencion!','Opcion no valida')

if __name__ == '__main__':
    ejecutar = Bienvenida()