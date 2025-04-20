from overrides.typing_utils import unknown

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
#----------------------------------------------------------------------------------------------------
to_learn= {}
try:
   data= pandas.read_csv("data/words_to_learns.csv")
except FileNotFoundError:
    og_data= pandas.read_csv("data/french_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient = "records")
def next_card():
    global choice ,flip_timer
    window.after_cancel(flip_timer)
    choice = random.choice(to_learn)
    canvas.itemconfig(card_title,text= "French",fill = "black")
    canvas.itemconfig(card_word, text=f"{choice["French"]}" ,fill = "black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000,func= flip_card)

def is_known():
    to_learn.remove(choice)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learns.csv",index= False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title,text ="English",fill = "white")
    canvas.itemconfig(card_word,text = choice["English"],fill = "white")
    canvas.itemconfig(card_bg,image = card_back)
#----------------------------UI Interfrace-----------------------------------------------------------#
window = Tk()
window.title("Flash Card France")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR )
flip_timer = window.after(3000,func= flip_card)

canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file= "images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
card_bg= canvas.create_image(400,263,image = card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column= 0, row=0,columnspan = 2)


card_title= canvas.create_text(400,150,text = "Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text = f"Word",font=("Ariel",60,"bold"))
known_image = PhotoImage(file="images/right.png")
known_button = Button(height =50, width=50 ,image=known_image, highlightthickness=0, command=is_known)
known_button.grid(column=1,row=3 )
unknown_image = PhotoImage(file ="images/wrong.png")
unknown_button = Button(height =50, width=50 ,image=unknown_image, highlightthickness=0 ,command=next_card)
unknown_button.grid(column=0,row=3)
next_card()

#------------------------------------------------------------------------------------------------------------#

#







window.mainloop()
