from tkinter import *
import random
from tkinter import scrolledtext

class Sin_Eva:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Protocolo BB84 sin Eva')
        self.ventana.geometry('650x750+700+100')
        self.ventana.configure(bg='black')
        self.ventana.iconbitmap(r'C:\Users\Ninja\Desktop\UNAM\7mo Semestre\Cuantica\Proyecto\py\imgs\qubit.ico')

        # Imagen
        self.fondo = PhotoImage(file=r'C:\Users\Ninja\Desktop\UNAM\7mo Semestre\Cuantica\Proyecto\py\imgs\fondo.png')
        Label(self.ventana, image=self.fondo, bg='black').pack()

        # Protocolo BB84 sin Eva
        self.label1 = Label(self.ventana, text='Protocolo BB84 sin Eva')
        self.label1.config(fg='White', bg='black', font=('Adale Mono Regular', 18, 'italic'))
        self.label1.place(x=200, y=140)

        # Pregunta
        self.label2 = Label(self.ventana, text='Cuantos Qubits desea?')
        self.label2.config(fg='White', bg='black', font=('Adale Mono Regular', 12, 'bold'))
        self.label2.place(x=250, y=250)

        # Alice - Bob
        self.label3 = Label(self.ventana, text='Alice                                                                                     Bob')
        self.label3.config(fg='White', bg='black', font=('Adale Mono Regular', 12, 'bold'))
        self.label3.place(x=100, y=380)

        # Entry
        self.dato1 = IntVar()
        self.entry1 = Entry(self.ventana, bd=2, bg='#eee8e8', fg='black', textvariable=self.dato1)
        self.entry1.config(font=('Adale Mono Regular', 12, 'bold'), width=27)
        self.entry1.place(x=220, y=280)

        # Boton
        self.boton3 = Button(self.ventana, text='Aceptar', bd=2, bg='White', fg='black', command=self.generar_llave)
        self.boton3.config(font=('Adale Mono Regular', 14), width=12)
        self.boton3.place(x=270, y=310)

        # Boton return
        self.boton2 = Button(self.ventana, text='Regresar', bd=2, bg='White', fg='black', command=self.acceso)
        self.boton2.config(font=('Adale Mono Regular', 14), width=12)
        self.boton2.place(x=270, y=350)

        # Área de texto desplazable para mostrar el protocolo
        self.protocolo_text = scrolledtext.ScrolledText(self.ventana, width=69, height=19, fg='White', bg='black')
        self.protocolo_text.config(font=('Adale Mono Regular', 12))
        self.protocolo_text.place(x=10, y=400)

        self.ventana.mainloop()

    def acceso(self):
        import ventana
        self.ventana.destroy()
        ventana.Bienvenida()

    def generar_bit(self):
        return random.randint(0, 1)

    def generar_base(self):
        return random.randint(0, 1)

    def generar_qubit(self, bit, base):
        bc = "C" if base == 0 else "D"
        qubit = "ketcero" if bit == 0 else "ketmenos"

        if bit == 0 and base == 1:
            qubit = "ketmas"
        elif bit == 1 and base == 0:
            qubit = "ketuno"

        return bc, qubit

    def generar_llave_qubits(self, n):
        llave_privada = []
        qubitAlice = []
        qubitBob = self.protocolo_text

        for _ in range(n):
            bit = self.generar_bit()
            baseA = self.generar_base()
            baseB = self.generar_base()

            bcA, qubit = self.generar_qubit(bit, baseA)
            bcB, qubitB = self.generar_qubit(bit, baseB)

            if bcA == bcB:
                llave_privada.append(bit)
                qubitAlice.append(qubit)
                qubitBob.insert(END, f"-Bit: {bit} Base: {bcA} Qubit: {qubit} ___________________ Base: {bcB} Qubit: {qubitB}\n")
            else:
                qubitAlice.append(qubit)
                qubitBob.insert(END, f"-Bit: {bit} Base: {bcA} Qubit: {qubit} _______________ Base: {bcB} Qubit: {qubitB} SE CANCELA\n")

        qubitBob.insert(END, "La llave privada es: " + ''.join(map(str, llave_privada)))

    def generar_llave(self):
        n = self.dato1.get()
        self.protocolo_text.delete(1.0, END)
        self.generar_llave_qubits(n)


