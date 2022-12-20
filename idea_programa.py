import tkinter as tk

ventana = tk.Tk()
ventana.geometry("800x600")

lista_entries = []
def escribir():
    curso = tk.Entry(ventana,)
    curso.grid(row=len(lista_entries)+1, column=0)
    horas = tk.Entry(ventana)
    horas.grid(row=len(lista_entries)+1, column=1)
    lista_entries.append((curso,horas))
    if lista_entries:
        boton2.grid(row=0, column=3)

    for elem in lista_entries:
        print(elem[0].get(), elem[1].get())


def eliminar():
    lista_entries[-1][0].destroy()
    lista_entries[-1][1].destroy()
    lista_entries.pop()

label1 = tk.Label(ventana, text="Curso", width=30)
label1.grid(row=0, column=0)
label1 = tk.Label(ventana, text="Cantidad de horas", width=30)
label1.grid(row=0, column=1)


boton1 = tk.Button(ventana, text="+", command=escribir)
boton1.grid(row=0, column=2)
boton2 = tk.Button(ventana, text="-", command=eliminar)

ventana.mainloop()