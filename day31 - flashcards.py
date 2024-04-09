from tkinter import Tk, Canvas, Button, PhotoImage
from random import choice
from pandas import DataFrame, read_csv

BACKGROUND_COLOR = "#B1DDC6"

try:
    read_csv("words_to_learn.csv")
except FileNotFoundError:
    words_data = read_csv("supportfiles/gaelic_words.csv")
else:
    words_data = read_csv("words_to_learn.csv")
finally:
    words_df = words_data.to_dict(orient="records")

def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_df)
    flash_card.itemconfig(language_text, text="Gaelic", fill="black")
    flash_card.itemconfig(word_text, text=current_card["Gaelic"], fill="black")
    flash_card.itemconfig(canvas_image, image=flash_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    flash_card.itemconfig(language_text, text="English", fill="white")
    flash_card.itemconfig(word_text, text=current_card["English"], fill="white")
    flash_card.itemconfig(canvas_image, image=back_img)

def learned_word():
    words_df.remove(current_card)
    to_learn = DataFrame.from_dict(words_df)
    to_learn.to_csv("words_to_learn.csv", index=False)
    new_card()

window = Tk()
flash_img = PhotoImage(file="supportfiles/card_front.png")
back_img = PhotoImage(file="supportfiles/card_back.png")
wrong_img = PhotoImage(file="supportfiles/wrong.png")
right_img = PhotoImage(file="supportfiles/right.png")
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)
current_card = {}

flash_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = flash_card.create_image(400, 263, image=flash_img)
language_text = flash_card.create_text(400, 150, text="Gaelic", 
                                    font=("Arial", 40, "italic"), justify="center")
word_text = flash_card.create_text(400, 263, text="word", font=("Arial", 60, "bold"), 
                                    justify="center")
flash_card.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, command=learned_word, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

window.mainloop()