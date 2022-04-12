from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    website = website.lower()

    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
                    "email": email,
                    "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("password_vault.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # creating a new json file to write user entries to
            with open("password_vault.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("password_vault.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #


def search():
    website = website_entry.get()
    website = website.lower()

    with open("password_vault.json", "r") as data_file:
        # reading old data
        data = json.load(data_file)
        for site in data:
            if website == site:
                messagebox.showinfo(title=site, message=f"Email: {data[site]['email']}\n"
                                                        f"Password: {data[site]['password']}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(bg="white")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0, "dkmiamib@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

#Buttons
password_button = Button(text="Generate", command=generate_pass, bg="white")
password_button.grid(row=3, column=2, columnspan=1)
add_button = Button(text="Add", command=save, width=38, bg="white")
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search, bg="white")
search_button.grid(row=1, column=2, columnspan=1)




window.mainloop()
