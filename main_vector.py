import tkinter as tk
import customtkinter as ctk
import re
import requests
import socket
from CTkScrollableDropdown import *


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
ctk.deactivate_automatic_dpi_awareness()

app = ctk.CTk()
app.title("Currency App")
app.iconbitmap('images/dollar.ico')
app.geometry("750x450")

mode = 'dark'

class CustomEntry(ctk.CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(validate="key")
        self.configure(validatecommand=(self.register(self.validate_input), '%P'))
        
    def validate_input(self, new_text):
        # Dozwolone są cyfry i kropki w Entryboxie input_entry_1
        return re.match(r'^[0-9.]*$', new_text) is not None
    

    
 # Internet connection information
def internet_connection_label(frame_name):
    def internet_connection():
        try:
            socket.create_connection(("Google.com", 80))
            return "Online"       
        except OSError:
            return "Offline"
        
    # Internet connection caption    
    status = ctk.CTkLabel(master=frame, text = "Status połączenia: ")
    status.place(relx=0.85, rely=0.9, anchor=tk.CENTER)

    online_status_text = internet_connection()
    online_status = ctk.CTkLabel(master=frame, text = online_status_text)
    online_status.place(relx=0.96, rely=0.9, anchor=tk.CENTER)

    # set the color
    if online_status_text == "Online":
       online_status.configure(text_color="green")
    else:
        online_status.configure(text_color="red")
        
    

    
def convert_with_API(base_currency, converted_currency, amount):
    # Where base_currency is the  currency you want to use, converted_currency is the currency that you want to convert to
    url = f"https/{base_currency}/{converted_currency}"

    # Making  request
    response = requests.get(url)

    # Convert data
    data = response.json() # converts JSON content into Python-readable content

    # Extract keys from data
    conversion_rate = float(data.get("conversion_rate")) # Gets value of key 'conversion_rate' from data
    last_time_update = data.get("time_last_update_utc") # Gets value of key 'time_last_update_utc' from data

    # Converts amount to another currency
    new_amount = amount * conversion_rate

    return new_amount

def currency_convert():
    base_currency = currency_combobox_1.get()
    convert_currency = currency_combobox_2.get()
    amount = input_entry_1.get().strip()  # Usuń białe znaki z przodu i z tyłu
    if not amount:  # Jeśli amount jest puste po usunięciu białych znaków
        my_label = ctk.CTkLabel(frame, font=("Arial", 18), text_color="red")
        my_label.configure(text="NIE podano kwoty!")
        my_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        app.after(2000, lambda: my_label.destroy()) 
    else:
        float_amount = float(amount)
        if float_amount < 0:
            my_label = ctk.CTkLabel(frame, font=("Arial", 18))
            my_label.configure(text="Kwota NIE może być mniejsza od 0!")
            my_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            app.after(2000, lambda: my_label.destroy()) 
        else:
            my_label = ctk.CTkLabel(frame, font=("Arial", 18))
            my_label.configure(text="Przeliczono")
            my_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            app.after(2000, lambda: my_label.destroy()) 
            result = convert_with_API(base_currency, convert_currency, float_amount)
            entry_variable.set(result)

    # # sprawdzenie
    # print(base_currency)
    # print(convert_currency)
    # print(amount)

entry_variable = ctk.StringVar()

def clearFunction():
    entry_variable.set("")
    input_entry_1.delete(0, ctk.END)
    input_entry_2.delete(0, ctk.END)
    
def change_color_mode():
    global mode
    if mode == 'dark':
        ctk.set_appearance_mode("light")
        mode = 'light'
    else:
        ctk.set_appearance_mode("dark")
        mode = 'dark'


currency_options = [
    "USD", "EUR", "GBP", "PLN", "CHF", "NOK", "SEK", "CZK", "CNY", "JPY", 
    "AUD", "CAD", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", 
    "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", 
    "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CDF", "CLP", "COP", "CRC",
    "CUP", "CVE", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR",
    "FJD", "FKP", "FOK", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ",
    "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", 
    "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "KES", "KGS", "KHR", "KID", 
    "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", 
    "MAD", "KMF", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", 
    "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NPR", "NZD", 
    "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PYG", "QAR", "RON", "RSD", 
    "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SGD", "SHP", "SLE", "SOS", 
    "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", 
    "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "AED", "UYU", "UZS", 
    "VES", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", 
    "ZAR", "ZMW", "ZWL"
]

frame = ctk.CTkFrame(master=app, width=700, height=450)
frame.pack(pady=25)

main_label = ctk.CTkLabel(master=frame, text="Przelicznik walut", font=("Arial", 26), text_color="red")
main_label.place(relx=0.5, rely=0.08, anchor=tk.CENTER)

internet_connection_label(frame)

button = ctk.CTkButton(master=frame, text="Przelicz waluty", command=currency_convert, corner_radius=50)
button.place(relx=0.85, rely=0.25, anchor=tk.CENTER)

output_label = ctk.CTkLabel(master=frame, text="Przelicz z:", height=5, width=5)
output_label.place(relx=0.2, rely=0.18, anchor=tk.CENTER)
input_entry_1 = CustomEntry(master=frame, placeholder_text="Podaj kwote do wymiany", width=170, height=40)
input_entry_1.place(relx=0.44, rely=0.26, anchor=tk.CENTER)
currency_combobox_1 = ctk.CTkComboBox(frame, values=currency_options, width=100, height=40, dropdown_hover_color='red',button_hover_color="red", dropdown_fg_color="black", dropdown_text_color="white")                      
currency_combobox_1.place(relx=0.2, rely=0.26, anchor=tk.CENTER)
CTkScrollableDropdown(attach=currency_combobox_1, values=currency_options)

output_label = ctk.CTkLabel(master=frame, text="Wynik: ")
output_label.place(relx=0.37, rely=0.38, anchor=tk.CENTER)

output_label = ctk.CTkLabel(master=frame, text="Przelicz na:")
output_label.place(relx=0.2, rely=0.38, anchor=tk.CENTER)
input_entry_2 = ctk.CTkEntry(master=frame, width=170, state='disable',textvariable=entry_variable, height=40)
input_entry_2.place(relx=0.44, rely=0.46, anchor=tk.CENTER)
currency_combobox_2 = ctk.CTkComboBox(frame, values=currency_options, width=100, height=40, dropdown_hover_color='red',button_hover_color="red", dropdown_fg_color="black", dropdown_text_color="white")
currency_combobox_2.place(relx=0.2, rely=0.46, anchor=tk.CENTER)
CTkScrollableDropdown(attach=currency_combobox_2, values=currency_options)

clear_button = ctk.CTkButton(frame, text="Wyczyść", command=clearFunction, corner_radius=50, fg_color='red', hover_color='orange')
clear_button.place(relx=0.85, rely=0.5, anchor=tk.CENTER)


switch_button = ctk.CTkSwitch(frame, text='Color Mode', command=change_color_mode)
switch_button.place(relx=0.2, rely = 0.9, anchor=tk.CENTER)

app.mainloop()