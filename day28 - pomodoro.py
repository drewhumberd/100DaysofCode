from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 24
SHORT_BREAK_MIN = 4
LONG_BREAK_MIN = 19
reps = 0
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global checks
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    checks = ""
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(WORK_MIN, 59)
        title.config(text="Work", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(SHORT_BREAK_MIN, 59)
        title.config(text="Short Break", fg=PINK)
    elif reps == 8:
        count_down(LONG_BREAK_MIN, 59)
        title.config(text="Long Break", fg=RED)
        reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(minutes, seconds):
    canvas.itemconfig(timer_text, text=f"{minutes}:{str(seconds).zfill(2)}")
    if minutes > 0:
        if seconds > 0:
            global timer
            timer = window.after(1000, count_down, minutes, seconds - 1)
        else:
            minutes -= 1
            seconds = 59
            timer = window.after(1000, count_down, minutes, seconds)
    else:
        if seconds > 0:
            timer = window.after(1000, count_down, minutes, seconds - 1)
        else:
            if reps % 2:
                global checks
                checks += "✔"
            start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=0, columnspan=3, sticky="")

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
start_button.grid_anchor("ne")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="supportfiles/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)
reset_button.grid_anchor("nw")

checkmarks = Label(text=checks, font=(FONT_NAME, 18, "bold"), bg=YELLOW, fg=GREEN)
checkmarks.grid(row=3, column=1)

window.mainloop()