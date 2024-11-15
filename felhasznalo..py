import tkinter as tk
from tkinter import ttk
from konyveklista import konyvek_adatok


root = tk.Tk()
root.title("Könyv Lista")
root.geometry("500x500")

konyv_cimek = [konyv["cim"] for konyv in konyvek_adatok]  
combo_box = ttk.Combobox(root, values=konyv_cimek)
combo_box.pack(padx=10, pady=10)


def show_book_info(event):
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


combo_box.bind("<<ComboboxSelected>>", show_book_info)


info_label = tk.Label(root, text="Válassz ki egy könyvet.", justify=tk.LEFT)
info_label.pack(padx=10, pady=10)

root.mainloop()