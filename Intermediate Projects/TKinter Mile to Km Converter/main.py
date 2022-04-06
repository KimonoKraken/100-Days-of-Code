from tkinter import *

# Create window
window = Tk()
window.title("Mile to Km Converter")
window.config(bg="white")
window.minsize(width=290, height=120)
window.config(padx=45, pady=30)

# Entry
input = Entry(width=10)
input.insert(END, "0")
print(input.get())
input.grid(column=1, row=0)

# Conversion button
def button_clicked():
    my_label_4.config(text=(round((int(input.get()) * 1.60934), 2)))


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Create labels (text)
my_label_1 = Label(text="is equal to", font=("Arial", 12, "bold"))
# my_label.config(text="New Text")
my_label_1.grid(column=0, row=1)
my_label_1.config(bg="white")


my_label_2 = Label(text="miles", font=("Arial", 12, "bold"))
my_label_2.grid(column=2, row=0)
my_label_2.config(bg="white")


my_label_3 = Label(text="Km", font=("Arial", 12, "bold"))
my_label_3.grid(column=2, row=1)
my_label_3.config(bg="white")

# This label/text spot is where the converted value appears
my_label_4 = Label(text="0", font=("Arial", 12))
my_label_4.grid(column=1, row=1)
my_label_4.config(bg="white")


window.mainloop()
