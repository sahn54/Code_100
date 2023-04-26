from tkinter import Tk, Entry,  Label, Button

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
# padding
window.config(padx=20, pady=20)


# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# pack(side="left") or pack(expand=1)

# my_label.place(x=100, y=200)

my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
# input.pack()
# input.get() returns str

# New Button
new_button = Button(text="Click Me NOW", command=button_clicked)
new_button.grid(column=2, row=0)

# argument default values
# unlimited arguments
# *args
# def add(*args):
#   for n in args:
#       print(n)


# pack , Place, grid


window.mainloop()
