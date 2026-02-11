import customtkinter as ctk

class MyScrollableCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.last_checked_checkbox = None
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value, command=lambda text=value: self.on_checkbox_click(text))
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)
    
    def on_checkbox_click(self, text):
        for checkbox in self.checkboxes:
            if checkbox.cget("text") != text:
                checkbox.deselect()
            else:
                self.last_checked_checkbox = checkbox if checkbox != self.last_checked_checkbox else None

    def get_checked_values(self):
        checked_values = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_values.append(checkbox.cget("text"))
        return checked_values

def show_scrollbar_frame():
    frame.pack(pady=40)
    button_2.pack()

def check_and_destory(frame, app):
    checked_values = frame.get_checked_values()
    print("Checked values:", checked_values)

    for checkbox in frame.checkboxes:
        checkbox.deselect()
        
    checked_values = None
    frame.pack_forget()
    button_2.forget()

app = ctk.CTk()
app.title("Currency App")
app.iconbitmap('./images/dollar.ico')
app.geometry("750x450")

values = ["USD", "EUR", "GBP", "PLN", "CHF", "NOK", "SEK", "CZK", "CNY", "JPY", "AUD", "CAD"]

frame = MyScrollableCheckboxFrame(app, "waluty", values)

button = ctk.CTkButton(app, text="Pokaż ramkę", command=show_scrollbar_frame)
button.pack(pady=20)
button_2 = ctk.CTkButton(app, text="Zatwierdź", command=lambda: check_and_destory(frame, app))

app.mainloop()
