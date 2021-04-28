''' trump quotes generator using tkinter - for the true patriot only '''

import requests
import random
from tkinter import *


def get_quote():

    # call on the trump api

    response = requests.get(url='https://api.whatdoestrumpthink.com/api/v1/quotes')
    response.raise_for_status()
    data = response.json()

    # choose (almost) random quote from list 

    choice = random.randint(0, len(data['messages']['personalized']))
    quote = data['messages']['personalized'][choice]
    canvas.itemconfig(quote_text, text=f'Trump says Biden: {quote}')

window = Tk()
window.title("Trump Quotes Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(130, 207, text='Trump 4 President', width=250, font=("Arial", 20, "bold"), fill="red")
canvas.grid(row=0, column=0)

trump_img = PhotoImage(file="trump.png")
trump_button = Button(image=trump_img, highlightthickness=0, command=get_quote, height=198, width=200)
trump_button.grid(row=1, column=0)

window.mainloop()