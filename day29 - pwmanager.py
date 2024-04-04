from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
from pyperclip import copy
FONT = ("sans-serif", 10, "normal")
BGCOLOR = "#2c343a"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():
    password_letters = [choice(LETTERS) for char in range(randint(8, 10))]
    password_numbers = [choice(NUMBERS) for char in range(randint(2, 4))]
    password_symbols = [choice(SYMBOLS) for char in range(randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    pw = "".join(password_list)
    password_field.delete(0, END)
    password_field.insert(0, pw)
    copy(pw)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_field.get()
    username = email_field.get()
    password = password_field.get()
    password_line = f"{website} | {username} | {password}"

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
    else:
        isok = messagebox.askokcancel(title=website, message=f"Save {username} as username \n" 
                            f"and {password} as password?")
        if isok:
            with open("file.txt", "a") as file:
                file.write(password_line)
                file.write("\n")
            website_field.delete(0, END)
            email_field.delete(0, END)
            password_field.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg=BGCOLOR, padx=20, pady=20)

logo = Canvas(width=200, height=200, bg=BGCOLOR, highlightthickness=0)
logo_img = PhotoImage(file="supportfiles/logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT, fg="white", bg=BGCOLOR)
website_label.grid(row=1, column=0, sticky="e", ipady=3)

website_field = Entry(width=50)
website_field.grid(row=1, column=1, columnspan=2, sticky="w")
website_field.focus()

email_label = Label(text="Email/Username:", font=FONT, fg="white", bg=BGCOLOR)
email_label.grid(row=2, column=0, sticky="e", ipady=3)

email_field = Entry(width=50)
email_field.grid(row=2, column=1, columnspan=2, sticky="w")
email_field.insert(0, "sample@email.com")

password_label = Label(text="Password:", font=FONT, fg="white", bg=BGCOLOR)
password_label.grid(row=3, column=0, sticky="e", pady=3)

password_field = Entry(width=30)
password_field.grid(row=3, column=1, sticky="w")

password_gen = Button(text="Generate Password", command=gen_password)
password_gen.grid(row=3, column=2, sticky="w")

add_button = Button(width=42, text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=3)

window.mainloop()
