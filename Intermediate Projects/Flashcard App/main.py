from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- Generate a word, flip card, keep track of progress------------------------------- #
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(quiz_word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(quiz_word_label, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #

# window and timing for flipping card
window = Tk()
window.title("Flashcard App")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=75)
# After 3 seconds, card flips
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
language_label = canvas.create_text(400, 150, text="", font=("arial", 30, "italic"))
quiz_word_label = canvas.create_text(400, 255, text="", font=("arial", 70, "bold"))
language_label_english = canvas.create_text(400, 150, text="", font=("arial", 30, "italic"))
quiz_word_label_english = canvas.create_text(400, 255, text="", font=("arial", 70, "bold"))

# Buttons
wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


right_button_image = PhotoImage(file="right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# Start with next word card upon launching app
next_card()

window.mainloop()
