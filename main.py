import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from forex_python.converter import CurrencyRates
from PIL import ImageTk, Image

# Create the window and set the width and height
window = tk.Tk()
window.title("Real-time Currency Converter")
window.geometry("600x500")

# Define fonts
FONT = tkfont.Font(family="Comic Sans MS", size=9, weight="bold")
HEADER_FONT = tkfont.Font(family="Comic Sans MS", size=12, weight="bold")

# Create the background canvas
canvas = tk.Canvas(window, height=500, width=600)
canvas.pack()

# Load and place the background image
background_image = ImageTk.PhotoImage(Image.open("Image/cur1.jpeg").resize((600, 500)))
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Function to clear the input and output fields
def clear():
    entry.delete(0, tk.END)
    label_down["text"] = ""

# Function to perform the conversion
def convert(c1, c2, amount):
    try:
        if not amount:
            messagebox.showerror("Error", "Please enter an amount.")
        elif c1 == "Select" or c2 == "Select":
            messagebox.showerror("Error", "Please select currencies.")
        else:
            try:
                amount = float(amount)
                c = CurrencyRates()
                result = c.convert(c1, c2, amount)

                label_down["text"] = f"Conversion Result: {amount} {c2}\n{amount} {c1} = {result} {c2}"
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
                clear()
    except Exception:
        messagebox.showerror("Error", "Something went wrong. Please try again.")

# Create the upper frame for input and labels
upper_frame = tk.Frame(window, bd=10)
upper_frame.place(relx=0.5, rely=0.12, relwidth=0.8, relheight=0.3, anchor="n")

# Create the label for the input fields
label1 = tk.Label(upper_frame, text="FROM", font=FONT, fg="black")
label1.pack(side="left")

label2 = tk.Label(upper_frame, text="TO", font=FONT, fg="black")
label2.pack(side="right")

# Create the OptionMenus for currency selection
options = [
    "USD",
    "EUR",
    "JPY",
    "GBP",
    "AUD",
    "CAD",
    "CHF",
    "INR",
    "RUB",
    "CNY",
]

clicked1 = tk.StringVar(window)
clicked1.set("Select")
listbox1 = tk.OptionMenu(upper_frame, clicked1, *options)
listbox1.config(font=FONT)
listbox1.pack(side="left")

clicked2 = tk.StringVar(window)
clicked2.set("Select")
listbox2 = tk.OptionMenu(upper_frame, clicked2, *options)
listbox2.config(font=FONT)
listbox2.pack(side="right")

# Create the amount label and entry field
label3 = tk.Label(window, text="AMOUNT", font=FONT, fg="black")
label3.place(relx=0.26, rely=0.32, relwidth=0.15, relheight=0.05)

entry = tk.Entry(window, font=FONT)
entry.place(relx=0.42, rely=0.32, relwidth=0.2, relheight=0.05)

# Create the convert button
button = tk.Button(window, text="CONVERT", font=FONT, bg="green", fg="black", command=lambda: convert(clicked1.get(), clicked2.get(), entry.get()))
button.place(relx=0.42, rely=0.42, relwidth=0.2, relheight=0.07)

# Create the output label
label_down = tk.Label(window, text="", font=HEADER_FONT)
label_down.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.3)

# Create the clear button
clear_button = tk.Button(window, text="CLEAR", font=FONT, bg="red", fg="black", command=clear)
clear_button.place(relx=0.42, rely=0.75, relwidth=0.2, relheight=0.07)

# Run the application
window.mainloop()
