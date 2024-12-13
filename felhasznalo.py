import tkinter as tk
from tkinter import ttk
from konyveklista import konyvek_adatok

def fel():

    root = tk.Tk()
    root.title("Felhasználó")
    root.geometry("1000x600")
    root.configure(bg="#9A7E6F")

    elotte = tk.Label(root, text="Válassza ki a könyvet:", bg="#B59F81", fg="yellow")
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
            try:
                with open("kikolcsonzott_konyvek.txt", "r") as file:
                    kikolcsonzott = file.readlines()

                if f"{kivalasztott_konyv['cim']}\n" in kikolcsonzott:
                    valaszt_label.config(text=f"A(z) {kivalasztott_konyv['cim']} könyvet már kikölcsönözték.")
                else:
                    with open("kikolcsonzott_konyvek.txt", "a") as file:
                        file.write(f"{kivalasztott_konyv['cim']}\n")
                    valaszt_label.config(text=f"A(z) {kivalasztott_konyv['cim']} könyvet sikeresen kikölcsönözted!")
            except FileNotFoundError:
                with open("kikolcsonzott_konyvek.txt", "w") as file:
                    file.write(f"{kivalasztott_konyv['cim']}\n")
                valaszt_label.config(text=f"A(z) {kivalasztott_konyv['cim']} könyvet sikeresen kikölcsönözted!")
        else:
            valaszt_label.config(text="Nincs könyv kiválasztva.")

    def kikolcsonzött_konyvek_megjelenitese():
        try:
            with open("kikolcsonzott_konyvek.txt", "r") as file:
                kikolcsonzott = file.readlines()

            if kikolcsonzott:
                lekert_konyvek = "".join(kikolcsonzott)
                valaszt_label.config(text=f"Kikölcsönzött könyvek:\n{lekert_konyvek}")
            else:
                valaszt_label.config(text="Nincs kikölcsönzött könyv.")
        except FileNotFoundError:
            valaszt_label.config(text="Még nincs kikölcsönzött könyv.")

    def torles():
        kivalasztott_cim = combo_box.get()
        kivalasztott_konyv = next((konyv for konyv in konyvek_adatok if konyv["cim"] == kivalasztott_cim), None)

        if kivalasztott_konyv:
            try:
                with open("kikolcsonzott_konyvek.txt", "r") as file:
                    kikolcsonzott = file.readlines()

                if f"{kivalasztott_cim}\n" not in kikolcsonzott:
                    valaszt_label.config(text=f"A(z) {kivalasztott_cim} könyv nincs kikölcsönözve, nem törölhető.")
                else:
                    with open("kikolcsonzott_konyvek.txt", "w") as file:
                        for konyv in kikolcsonzott:
                            if konyv.strip() != kivalasztott_cim:
                                file.write(konyv)
                    valaszt_label.config(text=f"A(z) {kivalasztott_cim} könyv vissza lett adva.")
            except FileNotFoundError:
                valaszt_label.config(text="Még nincs kikölcsönzött könyv.")
        else:
            valaszt_label.config(text="Még nincs kikölcsönzött könyv.")

    adat_button = tk.Button(root, text="A könyv adatai", command=konyv_info, bg="grey", fg="#4CCD99")
    adat_button.pack(padx=10, pady=10)

    kolcsonzes_button = tk.Button(root, text="Kikölcsönzés", command=kolcsonzes, bg="grey", fg="#4CCD99")
    kolcsonzes_button.pack(padx=10, pady=10)

    kolcsonzes_lekerese_button = tk.Button(root, text="Kikölcsönzött könyvek", command=kikolcsonzött_konyvek_megjelenitese, bg="grey", fg="#4CCD99")
    kolcsonzes_lekerese_button.pack(padx=10, pady=10)

    torles_button = tk.Button(root, text="Kikölcsönzött könyv visszaadása", command=torles, bg="grey", fg="#4CCD99")
    torles_button.pack(padx=10, pady=10)

    valaszt_label = tk.Label(root, text="Még nem választott ki könyvet , kérem válasszon ki.", justify=tk.LEFT, bg="#B59F81", fg="#8B0000")
    valaszt_label.pack(padx=10, pady=10)

    kilépés = tk.Button(root, text="Kilépés", padx=10, pady=10, fg="yellow", bg="red", command=root.destroy)
    kilépés.pack(padx=10, pady=10, anchor=None)

    root.mainloop()
