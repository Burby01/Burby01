import tkinter as tk
from tkinter import ttk
from konyveklista import konyvek_adatok

root = tk.Tk()
root.title("Könyv Lista")
root.geometry("500x500")

elotte = tk.Label(root, text="Válassza ki a könyvet:")
elotte.pack(padx=10, pady=10)

konyv_cimek = [konyv["cim"] for konyv in konyvek_adatok]
combo_box = ttk.Combobox(root, values=konyv_cimek, state="readonly")
combo_box.pack(padx=10, pady=10)

def konyv_info():
    kivalasztott_cim = combo_box.get()
    kivalasztott_konyv = next((konyv for konyv in konyvek_adatok if konyv["cim"] == kivalasztott_cim), None)

    if kivalasztott_konyv:
        valaszt_text = f"Cím: {kivalasztott_konyv['cim']}\n"
        valaszt_text += f"Szerző: {kivalasztott_konyv['szerzo']}\n"
        valaszt_text += f"Kiadás éve: {kivalasztott_konyv['megjelenes']}\n"
        valaszt_text += f"Kiadó: {kivalasztott_konyv['kiado']}\n"
        valaszt_text += f"Oldalszám: {kivalasztott_konyv['oldalszam']}\n"
        valaszt_text += f"ISBN: {kivalasztott_konyv['isbn']}"
    else:
        valaszt_text = "Nincs könyv kiválasztva."

    valaszt_label.config(text=valaszt_text)

def kolcsonzes():
    kivalasztott_cim = combo_box.get()
    kivalasztott_konyv = next((konyv for konyv in konyvek_adatok if konyv["cim"] == kivalasztott_cim), None)
    
    if kivalasztott_konyv:
        with open("kikolcsonzott_konyvek.txt", "r") as file:
            kikolcsonzott = file.readlines()

        if f"{kivalasztott_konyv['cim']}\n" in kikolcsonzott:
            valaszt_label.config(text=f"A(z) {kivalasztott_konyv['cim']} könyvet már kikölcsönözték.")
        else:
            with open("kikolcsonzott_konyvek.txt", "a") as file:
                file.write(f"{kivalasztott_konyv['cim']}\n")
            valaszt_label.config(text=f"A(z) {kivalasztott_konyv['cim']} könyvet sikeresen kikölcsönözted!")
    else:
        valaszt_label.config(text="Nincs könyv kiválasztva.")

def kolcsonzes_lekerese():
    kivalasztott_cim = combo_box.get()
    kivalasztott_konyv = next((konyv for konyv in konyvek_adatok if konyv["cim"] == kivalasztott_cim), None)
    if kivalasztott_konyv:
        with open("kikolcsonzott_konyvek.txt", "r") as file:
            kikolcsonzott = file.readlines()
        lekert_konyvek = "".join(kikolcsonzott)
        valaszt_label.config(text=f"Kikölcsönzött könyvek:\n{lekert_konyvek}")
    else:
        valaszt_label.config(text="Még nincs kikölcsönzött könyv.")

def torles():
    kivalasztott_cim = combo_box.get()
    kivalasztott_konyv = next((konyv for konyv in konyvek_adatok if konyv["cim"] == kivalasztott_cim), None)

    if kivalasztott_konyv:
        with open("kikolcsonzott_konyvek.txt", "r") as file:
            kikolcsonzott = file.readlines()
        with open("kikolcsonzott_konyvek.txt", "w") as file:
            for konyv in kikolcsonzott:
                if konyv.strip() != kivalasztott_cim:
                    file.write(konyv)
        valaszt_label.config(text=f"A(z) {kivalasztott_cim} könyv vissza lett adva.")
    else:
        valaszt_label.config(text="Még nincs kikölcsönzött könyv.")

adat_button = tk.Button(root, text="A könyv adatai", command=konyv_info)
adat_button.pack(padx=10, pady=10)

kolcsonzes_button = tk.Button(root, text="Kikölcsönzés", command=kolcsonzes)
kolcsonzes_button.pack(padx=10, pady=10)

kolcsonzes_lekerese_button = tk.Button(root, text="Kikölcsönzött könyvek", command=kolcsonzes_lekerese)
kolcsonzes_lekerese_button.pack(padx=10, pady=10)

torles_button = tk.Button(root, text="Kikölcsönzött könyv visszaadása", command=torles)
torles_button.pack(padx=10, pady=10)

valaszt_label = tk.Label(root, text="Még nem választott ki könyvet , kérem válasszon ki.", justify=tk.LEFT)
valaszt_label.pack(padx=10, pady=10)

root.mainloop()