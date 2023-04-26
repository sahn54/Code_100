import time
import math
from tkinter import Tk, Canvas, PhotoImage,  Label, Button
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFF3E2"
FONT_NAME = "Courier"
WORK_MIN = 45  # 45
SHORT_BREAK_MIN = 5  # 5
LONG_BREAK_MIN = 20  # 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)  # type: ignore
    canvas.itemconfig(timer_text, text=f"00:00")
    check_label.config(text="")
    title_label.config(text="Timer")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        title_label.config(text=f"Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text=f"Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        check_marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            check_marks += "✔"
        check_label.config(text=f"{check_marks}", font=(FONT_NAME, 20),
                           fg=GREEN, bg=YELLOW, highlightthickness=0)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Code_100/Day_28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# title label
title_label = Label(text="Timer", font=(FONT_NAME, 60),
                    fg=GREEN, bg=YELLOW, highlightthickness=0)
title_label.grid(column=1, row=0)


# calls start_timer() when pressed
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# calls reset_timer() when pressed
button = Button(text="Reset", highlightthickness=0, command=reset_timer)
button.grid(column=2, row=2)

# check_mark
check_label = Label(font=(FONT_NAME, 20),
                    fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=3)


window.mainloop()
