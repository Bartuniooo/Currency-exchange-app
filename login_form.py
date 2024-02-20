import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("system")

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Tutaj można dodać logikę weryfikacji danych logowania
    
    if username == "admin" and password == "admin":
        ctk.CTkMessageBox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        ctk.CTkMessageBox.showerror("Login Failed", "Invalid username or password")

app = ctk.CTk()

app.title("Login Form")
app.geometry("850x550")

label_username = ctk.CTkLabel(app, text="Username:")
label_username.pack()

entry_username = ctk.CTkEntry(app)
entry_username.pack()

label_password = ctk.CTkLabel(app, text="Password:")
label_password.pack()

entry_password = ctk.CTkEntry(app, show="*")  # Show "*" to hide password
entry_password.pack()

button_login = ctk.CTkButton(app, text="Login", command=login)
button_login.pack()

app.mainloop()
