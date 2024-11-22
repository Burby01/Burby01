from tkinter import*
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from functools import partial
from felhasznalo import fel
from admin import ad
 

root=tk.Tk()
root.title("Könyvár")
root.geometry("1000x600")
root.minsize(width=600, height=500)
root.configure(bg="#9A7E6F")

felhasznalo_label = tk.Label(root, text="Felhasználónév", bg="#B59F81", fg="yellow")
felhasznalo_label.place(relx=0.5, rely=0.053, anchor=N)
felhasznalo = Entry(root, width=50, bg="#B59F81", fg="#2A3663", borderwidth=8)
felhasznalo.insert(0, "")
felhasznalo.place(relx=0.5,rely=0.1,anchor=N)

jelszo_label = tk.Label(root, text="Jelszó", bg="#B59F81", fg="yellow")
jelszo_label.place(relx=0.5,rely=0.20,  anchor=N)
jelszo= Entry(root, width=50, bg="#B59F81",fg="#2A3663", borderwidth=8,show="*")
jelszo.insert(0, "")
jelszo.place(relx=0.5,rely=0.25,anchor=N)

siker_label = Label(root, text="", bg="green", fg="yellow")
nemsiker_label = Label(root, text="", bg="red", fg="yellow")


def bejelentkezes():
    global siker_label
    global nemsiker_label
    jszo = jelszo.get()
    felnev = felhasznalo.get()
    print(jszo, felnev)
    if felnev == "Admin" and jszo == "asd0":
        siker_label.config(text="Sikeres bejelentkezés")
        siker_label.place(relx=0.5, rely=0.35, anchor=N)
        ad()

    elif felnev == "Felhasznalo" and jszo == "asd123":
        siker_label.config(text="Sikeres bejelentkezés")
        siker_label.place(relx=0.5, rely=0.35, anchor=N)
        fel()
        
    else:
         nemsiker_label.config(text="Sikertelen bejelentkezés")
         nemsiker_label.place(relx=0.5, rely=0.35, anchor=N)


belepes = Button(root, text="Bejelentkezés", padx=10, pady=10, command=bejelentkezes, fg="yellow", bg="#B59F81")
belepes.place(relx=0.5, rely=0.44, anchor=N)
kilépés = Button(root, text="Kilépés",padx=10,pady=10,fg="yellow",bg="red" ,command=root.destroy)
kilépés.place(relx=0.5,rely=0.6, anchor=N)


root.mainloop()