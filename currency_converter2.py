import tkinter as tk
from tkinter import messagebox

rates = {
    'USD' : 1.0,
    'INR' : 83.2,
    'EUR' : 0.93,
    'GBP' : 0.80,
    'JPY' : 155.5,
    'CAD' : 1.36,
    'AUD' : 1.52,
    'CNY' : 7.22,
    'CHF' : 0.91,
    'NZD' : 1.63,
    'MXN' : 18.18,
    'BRL' : 5.31
}

def currency_converter(amount , source , target):
    source = source.upper()
    target = target.upper()
    if source not in rates or target not in rates:
        messagebox.showerror("Error","We are not able to provide that currency . ")
        return None
    else:
        source_amount = amount / rates[source]
        converted_amount = source_amount * rates[target]
        return converted_amount

def final_res():
    try:
        amount = float(amount_entry.get())
        source = from_currency_entry.get().strip().upper()
        target = to_currency_entry.get().strip().upper()
        result = currency_converter(amount , source , target)

        if result is not None:
            result_label.config(text=f"{amount} {source} = {result:.2f} {target}")

    except ValueError:
        messagebox.showerror("Error","Invalid. Please enter a valid currency . ")


window = tk.Tk()
window.title("Currency Converter")
window.attributes("-fullscreen",True)
window.configure(bg = "beige")

initial = tk.Label(window,text = "Enter Amount :",font = ("Times New Roman",24),bg = "beige")
initial.pack(pady = 20)

amount_entry = tk.Entry(window,font = ("Times New Roman",20),width =20)
amount_entry.pack(pady = 20)

from_label = tk.Label(window,text = "Enter Source Currency : ",font = ("Times New Roman",20),bg = "beige")
from_label.pack(pady = 20)

from_currency_entry = tk.Entry(window,font = ("Times New Roman",20),width = 20)
from_currency_entry.pack(pady = 20)

to_label = tk.Label(window,text = "Enter Target Currency : ",font = ("Times New Roman ",20), bg = "beige")
to_label.pack(pady = 20)

to_currency_entry = tk.Entry(window,font = ("Times New Roman",20),width = 20)
to_currency_entry.pack(pady = 20)

button = tk.Button(window , text = "Convert" , font = ("Courier New",24) , command = final_res , bg = "green" , fg = "white")
button.pack(pady = 20)

result_label = tk.Label(window , text = "",font = ("Times New Roman",48),bg = "beige" , fg = "black")
result_label.pack(pady = 40)

window.mainloop()
        
