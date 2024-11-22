import tkinter as tk
from tkinter import ttk
from konyveklista import konyvek_adatok

root = tk.Tk()
root.title("Könyv Lista")
root.geometry("500x500")
root.configure(bg="#964B00")

elotte = tk.Label(root, text="Válassza ki a könyvet:", bg="grey", fg="yellow")
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

adat_button = tk.Button(root, text="A könyv adatai", command=konyv_info, bg="grey", fg="yellow")
adat_button.pack(padx=10, pady=10)
    
valaszt_label = tk.Label(root, text="Még nem választott ki könyvet , kérem válasszon ki.", justify=tk.LEFT, bg="grey", fg="#8B0000")
valaszt_label.pack(padx=10, pady=10)

root.mainloop()