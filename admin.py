import tkinter as tk
from tkinter import ttk
from konyveklista import konyvek_adatok

def ad():
    root = tk.Tk()
    root.title("Admin")
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

    rogzites_container = tk.Frame(root, bg="#9A7E6F")

    def rogzites():
        if not hasattr(rogzites, 'is_created') or not rogzites.is_created:
            labelek = ["Cím:", "Szerző:", "Megjelenés éve:", "Kiadó:", "Oldalszám:", "ISBN:"]
            entryk = []
            for i, label_text in enumerate(labelek):
                label = tk.Label(rogzites_container, text=label_text, bg="#B59F81", fg="yellow")
                label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
                entry = tk.Entry(rogzites_container, width=40, bg="#F5E6C8")
                entry.grid(row=i, column=1, padx=5, pady=5)
                entryk.append(entry)

            def mentes():
                adatok = {label: entry.get() for label, entry in zip(labelek, entryk)}

                uj_konyv = {
                    "cim": adatok["Cím:"],
                    "szerzo": adatok["Szerző:"],
                    "megjelenes": int(adatok["Megjelenés éve:"]),
                    "kiado": adatok["Kiadó:"],
                    "oldalszam": int(adatok["Oldalszám:"]),
                    "isbn": adatok["ISBN:"]
                }
                konyvek_adatok.append(uj_konyv)

                konyv_cimek.append(uj_konyv["cim"])
                combo_box['values'] = konyv_cimek

                for entry in entryk:
                    entry.delete(0, tk.END)

            mentes_button = tk.Button(rogzites_container, text="Rögzítés", command=mentes, bg="green", fg="white")
            mentes_button.grid(row=len(labelek), column=0, columnspan=2, pady=10)

            rogzites_container.pack(padx=10, pady=10)
            rogzites.is_created = True

    def torles():
        kivalasztott_cim = combo_box.get()
        if kivalasztott_cim:
            konyv_torles = next((konyv for konyv in konyvek_adatok if konyv["cim"] == kivalasztott_cim), None)
            if konyv_torles:
                konyvek_adatok.remove(konyv_torles)
                konyv_cimek.remove(kivalasztott_cim)
                combo_box['values'] = konyv_cimek 

                valaszt_label.config(text=f"A '{kivalasztott_cim}' című könyv törölve lett.")
            else:
                valaszt_label.config(text="Ezt a könyvet már kitörölted.")
        else:
            valaszt_label.config(text="Nincs kiválasztott könyv.")

    def modositas():
        kivalasztott_cim = combo_box.get()
        kivalasztott_konyv = next((konyv for konyv in konyvek_adatok if konyv["cim"] == kivalasztott_cim), None)

        if kivalasztott_konyv:
            if not hasattr(modositas, 'is_created') or not modositas.is_created:
                rogzites_container.pack(padx=10, pady=10)
                labelek = ["Cím:", "Szerző:", "Megjelenés éve:", "Kiadó:", "Oldalszám:", "ISBN:"]
                entryk = []

                for i, (label_text, key) in enumerate(zip(labelek, kivalasztott_konyv.keys())):
                    label = tk.Label(rogzites_container, text=label_text, bg="#B59F81", fg="yellow")
                    label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
                    entry = tk.Entry(rogzites_container, width=40, bg="#F5E6C8")
                    entry.insert(0, str(kivalasztott_konyv[key])) 
                    entry.grid(row=i, column=1, padx=5, pady=5)
                    entryk.append(entry)

                def ment_modositas():
                    uj_adatok = {label: entry.get() for label, entry in zip(labelek, entryk)}

                    kivalasztott_konyv["cim"] = uj_adatok["Cím:"]
                    kivalasztott_konyv["szerzo"] = uj_adatok["Szerző:"]
                    kivalasztott_konyv["megjelenes"] = int(uj_adatok["Megjelenés éve:"])
                    kivalasztott_konyv["kiado"] = uj_adatok["Kiadó:"]
                    kivalasztott_konyv["oldalszam"] = int(uj_adatok["Oldalszám:"])
                    kivalasztott_konyv["isbn"] = uj_adatok["ISBN:"]

                    combo_box['values'] = [k["cim"] for k in konyvek_adatok]

                    valaszt_label.config(text=f"A '{kivalasztott_cim}' című könyv módosítva lett.")
                    rogzites_container.pack_forget()
                    modositas.is_created = False

                ment_button = tk.Button(rogzites_container, text="Módosítás mentése", command=ment_modositas, bg="blue", fg="white")
                ment_button.grid(row=len(labelek), column=0, columnspan=2, pady=10)

                modositas.is_created = True
        else:
            valaszt_label.config(text="Válasszon ki egy könyvet a módosításhoz!")

    adat_button = tk.Button(root, text="A könyv adatai", command=konyv_info, bg="grey", fg="#4CCD99")
    adat_button.pack(padx=10, pady=10)

    hozzadas_button = tk.Button(root, text="Könyv rögzítése", command=rogzites, bg="grey", fg="#4CCD99")
    hozzadas_button.pack(padx=10, pady=10)

    torles_button = tk.Button(root, text="Könyv törlése", command=torles, bg="grey", fg="#4CCD99")
    torles_button.pack(padx=10, pady=10)

    modositas_button = tk.Button(root, text="Könyv módosítása", command=modositas, bg="grey", fg="#4CCD99")
    modositas_button.pack(padx=10, pady=10)

    valaszt_label = tk.Label(root, text="Még nem választott ki könyvet.", justify=tk.LEFT, bg="#B59F81", fg="#8B0000")
    valaszt_label.pack(padx=10, pady=10)

    kilepes_button = tk.Button(root, text="Kilépés", padx=10, pady=10, fg="yellow", bg="red", command=root.destroy)
    kilepes_button.pack(padx=10, pady=10)

    root.mainloop()
