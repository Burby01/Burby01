import os
import tkinter as tk
from tkinter import filedialog, Toplevel
class MiniApp:
    def __init__(self, username):
        self.username = username
        self.conversation = self.betoltes_uzenetek("message.txt")
        self.profile_path = f"profiles/{self.username}"

        if not os.path.exists(self.profile_path):
            os.makedirs(self.profile_path)

    def run(self):
        self.root = tk.Tk()
        self.root.title("Mini App")
        self.root.geometry("1000x600")
        self.root.config(bg="#008080")
        self.root.minsize(width=600, height=500)

        self.cim = tk.Label(self.root, text='Mini App', fg='black', bg='#008080', font=("Times New Roman", 14))
        self.cim.place(relx=0.5, rely=0.05, anchor="n")

        self.user_label = tk.Label(self.root, text=f"Bejelentkezve mint: {self.username}", fg='#404040', bg='#A0A0A0')
        self.user_label.place(relx=0, rely=0.05)

        self.conversation_textbox = tk.Text(self.root, height=20, width=80, bg='#C0C0C0')
        self.conversation_textbox.place(relx=0.5, rely=0.5, anchor="n")
        self.update_conversation()
        self.conversation_textbox.config(state="disabled")

        self.message_entry = tk.Entry(self.root, width=80, bg='#808080', fg='lime')
        self.message_entry.place(relx=0.5, rely=0.9, anchor="n")

        self.send_button = tk.Button(self.root, text="Küldés", command=self.send_message, bg="grey", fg="lime")
        self.send_button.place(relx=0.76, rely=0.9, anchor="n")

        self.new_conversation_button = tk.Button(self.root, text="Új beszélgetés", command=self.open_conversation_windows, bg="grey", fg="lime")
        self.new_conversation_button.place(relx=0.9, rely=0.05, anchor="n")

        self.profile_button = tk.Button(self.root, text="Profil szerkesztése", command=self.open_profile_window, bg="grey", fg="lime")
        self.profile_button.place(relx=0, rely=.085)

        self.root.mainloop()


    def update_conversation(self):
        self.conversation_textbox.config(state="normal")
        self.conversation_textbox.delete(1.0, "end")
        for msg in self.conversation:
            self.conversation_textbox.insert("end", msg + "\n")
        self.conversation_textbox.config(state="disabled")

    def open_profile_window(self):
        self.profile_window = Toplevel(self.root)
        self.profile_window.title(f"{self.username} Profilja")
        self.profile_window.geometry("400x400")
        self.profile_window.config(bg='#008080')

        self.profile_intro_label = tk.Label(self.profile_window, text="Könyvek lekérdezése:", bg='#008080')
        self.profile_intro_label.pack(pady=5)

        self.profile_intro_text = tk.Text(self.profile_window, height=5, width=40)
        self.profile_intro_text.pack(pady=5)
        self.load_profile_intro()

        self.upload_image_button = tk.Button(self.profile_window, text="Könyvek rögzítése", command=self.upload_image)
        self.upload_image_button.pack(pady=10)

        self.upload_image_button = tk.Button(self.profile_window, text="Könyvek módosítása", command=self.upload_image)
        self.upload_image_button.pack(pady=10)

        self.upload_image_button = tk.Button(self.profile_window, text="Könyvek törlése", command=self.upload_image)
        self.upload_image_button.pack(pady=10)

        self.save_profile_button = tk.Button(self.profile_window, text="Mentés", command=self.save_profile)
        self.save_profile_button.pack(pady=10)

        self.display_profile_image()

    def load_profile_intro(self):
        intro_path = os.path.join(self.profile_path, "intro.txt")
        if os.path.exists(intro_path):
            with open(intro_path, "r") as file:
                intro_text = file.read()
                self.profile_intro_text.insert("1.0", intro_text)

    def upload_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if image_path:
            dest_path = os.path.join(self.profile_path, "profile_image.png")
            img = Image.open(image_path)
            img.thumbnail((150, 150))  
            img.save(dest_path)
            self.display_profile_image()

    def display_profile_image(self):
        dest_path = os.path.join(self.profile_path, "profile_image.png")
        if os.path.exists(dest_path):
            img = Image.open(dest_path)
            img = ImageTk.PhotoImage(img)
            if hasattr(self, 'profile_image_label'):
                self.profile_image_label.config(image=img)
                self.profile_image_label.image = img
            else:
                self.profile_image_label = tk.Label(self.profile_window, image=img)
                self.profile_image_label.image = img
                self.profile_image_label.pack(pady=10)

    def save_profile(self):
        intro_text = self.profile_intro_text.get("1.0", "end").strip()
        intro_path = os.path.join(self.profile_path, "intro.txt")
        with open(intro_path, "w") as file:
            file.write(intro_text)
        tk.messagebox.showinfo("Mentés", "Profil mentve!")

    def open_conversation_windows(self):
        # Ember 1 ablaka
        self.user1_window = Toplevel(self.root)
        self.user1_window.title("Chat Ember 1")
        self.user1_window.geometry("300x350")
        self.user1_window.config(bg='#008080')

        self.user1_label = tk.Label(self.user1_window, text="Üzenetfal:", bg='#008080')
        self.user1_label.pack(pady=5)

        self.user1_message_entry = tk.Entry(self.user1_window, width=30, bg='#808080', fg='lime')
        self.user1_message_entry.pack(pady=5)

        self.user1_send_button = tk.Button(self.user1_window, text="Küldés", command=self.send_message_user1)
        self.user1_send_button.pack(pady=10)

        self.user1_textbox = tk.Text(self.user1_window, height=10, width=30, bg='#C0C0C0')
        self.user1_textbox.pack(pady=10)
        self.user1_textbox.config(state="disabled")

        self.user1_exit_button = tk.Button(self.user1_window, text="Kilépés", command=self.close_conversation_windows, bg="red", fg="white")
        self.user1_exit_button.pack(pady=10)

        # Ember 2 ablaka
        self.user_window = Toplevel(self.root)
        self.user_window.title("Chat Ember 2")
        self.user_window.geometry("300x350")
        self.user_window.config(bg='#008080')

        self.user_label = tk.Label(self.user_window, text="Üzenetfal:", bg='#008080')
        self.user_label.pack(pady=5)

        self.user_message_entry = tk.Entry(self.user_window, width=30, bg='#808080', fg='lime')
        self.user_message_entry.pack(pady=5)

        self.user_send_button = tk.Button(self.user_window, text="Küldés", command=self.send_message_user)
        self.user_send_button.pack(pady=10)

        self.user_textbox = tk.Text(self.user_window, height=10, width=30, bg='#C0C0C0')
        self.user_textbox.pack(pady=10)
        self.user_textbox.config(state="disabled")

        self.user_exit_button = tk.Button(self.user_window, text="Kilépés", command=self.close_conversation_windows, bg="red", fg="white")
        self.user_exit_button.pack(pady=10)

        # Üzenetek betöltése mindkét ablakba
        self.user1_conversation = self.betoltes_uzenetek("fomessage.txt")
        self.update_user1_conversation()

    def send_message_user1(self):
        message = self.user1_message_entry.get().strip()
        if message:
            formatted_message = f"Ember 1: {message}"
            self.user1_conversation.append(formatted_message)
            self.mentes_uzenetek("fomessage.txt", self.user1_conversation)
            self.update_user1_conversation()
            self.user1_message_entry.delete(0, "end")

    def send_message_user(self):
        message = self.user_message_entry.get().strip()
        if message:
            formatted_message = f"{self.username}: {message}"
            self.user1_conversation.append(formatted_message)
            self.mentes_uzenetek("fomessage.txt", self.user1_conversation)
            self.update_user1_conversation()
            self.user_message_entry.delete(0, "end")

    def update_user1_conversation(self):
        conversation_text = "\n".join(self.user1_conversation)
        self.user1_textbox.config(state="normal")
        self.user1_textbox.delete(1.0, "end")
        self.user1_textbox.insert("end", conversation_text)
        self.user1_textbox.config(state="disabled")

        self.user_textbox.config(state="normal")
        self.user_textbox.delete(1.0, "end")
        self.user_textbox.insert("end", conversation_text)
        self.user_textbox.config(state="disabled")

    def close_conversation_windows(self):
        # Csak az üzenetablakokat zárja be
        if self.user1_window:
            self.user1_window.destroy()
        if self.user_window:
            self.user_window.destroy()

    
    def mentes_uzenetek(self, filename, messages):
        with open(filename, "w") as file:
            for msg in messages:
                file.write(msg + "\n")

    def betoltes_uzenetek(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return [line.strip() for line in file.readlines()]
        return []


root = tk.Tk()
root.title("Bejelentkezés")
root.geometry("1000x600")
root.configure(bg="#008880")

valid_users = {
    "1": "1",
    "Fekhasznalo": "asd123"
}

felhasznalo_label = tk.Label(root, text="Felhasználónév", bg="grey", fg="lime")
felhasznalo_label.place(relx=0.5, rely=0.05, anchor="n")
felhasznalo = tk.Entry(root, width=50, bg="grey", fg="lime", borderwidth=8)
felhasznalo.place(relx=0.5, rely=0.1, anchor="n")

jelszo_label = tk.Label(root, text="Jelszó", bg="grey", fg="lime")
jelszo_label.place(relx=0.5, rely=0.2, anchor="n")
jelszo = tk.Entry(root, width=50, show="*", bg="grey", fg="lime", borderwidth=8)
jelszo.place(relx=0.5, rely=0.25, anchor="n")

siker_label = tk.Label(root, text="", bg="green", fg="lime")
nemsiker_label = tk.Label(root, text="", bg="red", fg="lime")

def bejelentkezes():
    username = felhasznalo.get()
    password = jelszo.get()
    if username in valid_users and valid_users[username] == password:
        siker_label.config
        siker_label.config(text="Sikeres bejelentkezés")
        siker_label.place(relx=0.5, rely=0.35, anchor="n")
        
        root.after(500, lambda: [root.destroy(), MiniApp(username).run()])
    else:
        nemsiker_label.config(text="Sikertelen bejelentkezés")
        nemsiker_label.place(relx=0.5, rely=0.35, anchor="n")

belepes = tk.Button(root, text="Bejelentkezés", padx=10, pady=10, command=bejelentkezes, fg="lime", bg="grey")
belepes.place(relx=0.5, rely=0.44, anchor="n")

kilepes = tk.Button(root, text="Kilépés", padx=10, pady=10, fg="lime", bg="red", command=root.destroy)
kilepes.place(relx=0.5, rely=0.6, anchor="n")

root.mainloop()