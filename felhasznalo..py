import tkinter as tk
from tkinter import ttk
from konyveklista import konyvek_adatok

root = tk.Tk()
root.title("Könyv Lista")
root.geometry("500x500")

elotte = tk.Label(root, text="Válassza ki a könyvet:")
elotte.pack(padx=10, pady=10)


konyv_cimek = [konyv["cim"] for konyv in konyvek_adatok]
combo_box = ttk.Combobox(root, values=konyv_cimek)
combo_box.pack(padx=10, pady=10)


def konyv_info():
    kivalasztott_cim = combo_box.get()
    kivalasztott_konyv = next((konyv for konyv in konyvek_adatok if konyv["cim"] == kivalasztott_cim), None)

    if kivalasztott_konyv:
        info_text = f"Cím: {kivalasztott_konyv['cim']}\n"
        info_text += f"Szerző: {kivalasztott_konyv['szerzo']}\n"
        info_text += f"Kiadás éve: {kivalasztott_konyv['megjelenes']}\n"
        info_text += f"Kiadó: {kivalasztott_konyv['kiado']}\n"
        info_text += f"Oldalszám: {kivalasztott_konyv['oldalszam']}\n"
        info_text += f"ISBN: {kivalasztott_konyv['isbn']}"
    else:
        info_text = "Nincs könyv kiválasztva."

    info_label.config(text=info_text)

adat_button = tk.Button(root, text="A könyv adatai", command=konyv_info)
adat_button.pack(padx=10, pady=10)

kolcsonzes_button = tk.Button(root,text="Kikölcsönzés",command=konyv_info)
kolcsonzes_button.pack(padx=10,pady=10)

info_label = tk.Label(root, text="Válassz ki egy könyvet.", justify=tk.LEFT)
info_label.pack(padx=10, pady=10)

root.mainloop()
