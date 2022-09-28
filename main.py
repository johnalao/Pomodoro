import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks.config(text="")
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
        count_down(long_break_sec)
        title_label.config(text="break", fg=PINK)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="break", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


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
        marks = ""
        work_time = math.floor(REPS / 2)
        for i in range(work_time):
            marks += "✔"

        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=RED, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# logic to add the tomato picture and the text to the screen
canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create the button

start_button = Button(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

# Checkmarks

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)
window.mainloop()  # allow the screen to show up just like exit onscreen
