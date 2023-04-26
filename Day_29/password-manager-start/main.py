from tkinter import Tk, Canvas, PhotoImage,  Label, Button, Entry, END, messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]

    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    password = "".join(password_list)
    if len(password_input.get()) != 0:
        password_input.delete(0, END)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    is_ok = messagebox.askokcancel(
        title=website, message=f"These are the details entered: \nEmail:{email} \nPassword{password} \nIs it okay to save?")
    if is_ok:
        with open("Code_100/Day_29/password-manager-start/data.txt", mode="a") as data:
            data.write(
                f"{website} | {email} | {password}\n")
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)


def check_input():
    if len(website_input.get()) == 0 or len(password_input.get()) == 0 or len(email_input.get()) == 0:
        messagebox.showerror(
            title="Error", message=f"Please don't leave any fields empty!")
    else:
        save_password()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# image
my_password = PhotoImage(
    file="Code_100/Day_29/password-manager-start/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=my_password)
canvas.grid(column=1, row=0)


# website label
website_label = Label(text="Website:", font=(
    "Courier", 20), highlightthickness=0)
website_label.grid(column=0, row=1)
# Email label
email_label = Label(text="Email/Username:",
                    font=("Courier", 20), highlightthickness=0)
email_label.grid(column=0, row=2)
# password label
password_label = Label(text="Password:", font=(
    "Courier", 20), highlightthickness=0)
password_label.grid(column=0, row=3)

# website input
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
# email input
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "@gmail.com")
# password input
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# calls generate_password() when pressed
generate_button = Button(text="Generate Password",
                         highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)
# calls save_password() when pressed
save_button = Button(text="Add", width=36,
                     highlightthickness=0, command=check_input)
save_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
