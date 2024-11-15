import tkinter as tk
from tkinter import ttk
from konyveklista import books



# Tkinter ablak létrehozása
root = tk.Tk()
root.title("Könyv Lista")
root.geometry("500x500")

# Legördülő menü létrehozása
konyv_cimek = [konyv["cim"] for konyv in books]  # Kiválasztjuk a címeket a könyvek listájából
combo_box = ttk.Combobox(root, values=konyv_cimek)
combo_box.pack(padx=10, pady=10)

# Kiválasztott könyv információinak megjelenítése
def show_book_info(event):
    selected_title = combo_box.get()  # A kiválasztott könyv címe
    kivalasztott_konyv = next((konyv for konyv in books if konyv["cim"] == selected_title), None)
    
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

# Kiválasztás figyelése
combo_box.bind("<<ComboboxSelected>>", show_book_info)

# Információs szöveg megjelenítése
info_label = tk.Label(root, text="Select a book to see more details.", justify=tk.LEFT)
info_label.pack(padx=10, pady=10)

# Alkalmazás futtatása
root.mainloop()