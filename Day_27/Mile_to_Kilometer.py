from tkinter import Tk, Entry, Label, Button

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(input.get())
    kilometers = round(miles * 1.609)
    convert_km_label.config(text=f"{kilometers}")


input = Entry(width=10)
input.grid(column=2, row=0)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=3, row=0)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=3, row=1)

is_equal_label = Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=1, row=1)

convert_km_label = Label(text="0", font=("Arial", 12))
convert_km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=2)

window.mainloop()
