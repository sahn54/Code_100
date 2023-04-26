from tkinter import Tk, Canvas, PhotoImage,  Label, Button, Entry, END
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
new_data = {}
try:
    data = pandas.read_csv(
        "Code_100/Day_31/flash-card-project-start/data/words_to_learn.csv")
except FileExistsError:
    original_data = pandas.read_csv(
        "Code_100/Day_31/flash-card-project-start/data/french_words.csv")
    new_data = original_data.to_dict(orient="records")
else:
    new_data = data.to_dict(orient="records")

# ------------------------------------Next Word ------------------------------------


def new_random_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(new_data)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(main_title, text="French", fill="black")
    canvas.itemconfig(main_word, text=current_card["French"], fill="black")
    window.after(3000, func=flip_card)
# ------------------------------------Flip card ------------------------------------


def flip_card():
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(main_title, text="English", fill="white")
    canvas.itemconfig(main_word, text=current_card["English"], fill="white")

# ------------------------------------learned------------------------------------


def is_known():
    new_data.remove(current_card)
    save_data = pandas.DataFrame(new_data)
    save_data.to_csv(
        "Code_100/Day_31/flash-card-project-start/data/word_to_learn.csv", index=False)
    new_random_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
front_card = PhotoImage(
    file="Code_100/Day_31/flash-card-project-start/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
main_title = canvas.create_text(400, 150, text="Title", font=(
    "Ariel", 40, "italic"), fill="black")
main_word = canvas.create_text(400, 263, text="Word", font=(
    "Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

back_card = PhotoImage(
    file="Code_100/Day_31/flash-card-project-start/images/card_back.png")

# canvas.create_image(400, 263, image=back_card)
# canvas.create_text(400, 150, text="Title", font=(
#     "Ariel", 40, "italic"), fill="white")
# canvas.grid(row=0, column=0)


right_logo = PhotoImage(
    file="Code_100/Day_31/flash-card-project-start/images/right.png")
right_button = Button(
    image=right_logo, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_logo = PhotoImage(
    file="Code_100/Day_31/flash-card-project-start/images/wrong.png")
wrong_button = Button(
    image=wrong_logo, highlightthickness=0, command=new_random_word)
wrong_button.grid(row=1, column=0)

new_random_word()
# Labels
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
window.mainloop()
