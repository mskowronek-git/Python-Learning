from tkinter import *
from tkinter import messagebox
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if (len(website) or len(email) or len(password)) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as passwords:

                #new_password = f"{website} | {email} | {password}\n"
                #passwords.write(new_password)
                data = json.load(passwords)
                data.update(new_data)

            with open("data.json", "w") as passwords:

                json.dump(data, passwords, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

        except FileNotFoundError:
            with open("data.json", "a") as passwords:
                json.dump(new_data, passwords, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as passwords:
            data = json.load(passwords)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
        if website in data:
                email = list(data[website].values())[0]
                password= list(data[website].values())[1]
                messagebox.showinfo(title=website, message=f"Email: {email}\n "
                                                    f"Password: {password}")
        else:
            messagebox.showinfo(message="No details for the website exists")
# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()

website_button = Button(text="Search", bg="white", command=find_password)
website_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:    ", bg="white")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "michal.skowronek@gmail.com")

password_label = Label(text="Password:    ", bg="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", bg="white", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", bg="white", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()