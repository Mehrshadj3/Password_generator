from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = ["".join(random.choice(letters)) for _ in range(nr_letters)]
    symbols_list = ["".join(random.choice(symbols)) for _ in range(nr_symbols)]
    numbers_list = ["".join(random.choice(numbers)) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)
    password =  "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {'email': email, 'password': password}}
    if len(website) < 3 or len(email) < 5 or len(password) < 5:
        messagebox.showinfo(title="ERROR", message="The length of your email or password is not appropriate!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No data found")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="Details", message=f"Website: {website}\n Password: {password}")
            else:
                messagebox.showinfo(title="ERROR", message="No details for the website exists.")






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
canvas = Canvas(width=190, height=180, highlightthickness=0)
window.minsize(width=400, height=400)
window.config(pady=20, padx=80)

logo_file = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=logo_file)
canvas.grid(column=2, row=1)


website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
website_label.config(pady=10)

email_label = Label(text="Email/Username:")
email_label.config(pady=10)
email_label.grid(column=1, row=3)
email_label.config(pady=10)

password_label = Label(text="Password:")

password_label.grid(column=1, row=4)
password_label.config(pady=10)

website_entry = Entry()
website_entry.grid(column=2, row=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(column=2, row=3, columnspan=2)
password_entry = Entry()
password_entry.grid(column=2, row=4)

password_button = Button(text="Generate Password", width=11, command=password_generator)
password_button.grid(column=3, row=4)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=2, row=5, columnspan=2)

search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=3, row=2)

window.mainloop()



