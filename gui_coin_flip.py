#This is a game of Flip the Coin. The first to 5 wins.
from tkinter import *
from tkinter import ttk
import random
import time
root = Tk()
root.title('Coin Flip')
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text='FLIP THE COIN').grid(column=2, row=1)
computer_score = 0
player_score = 0
ttk.Label(mainframe, text='Player').grid(column=1, row=4)
ttk.Label(mainframe, text='Computer').grid(column=3, row=4)
ttk.Label(mainframe, text=player_score).grid(column=1, row=5)
ttk.Label(mainframe, text=computer_score).grid(column=3, row=5)
ttk.Label(mainframe, text="5 points wins.\nChoose: Heads or Tails").grid(column=2, row=2)
def flip_coin():
    values = ['heads', 'tails']
    return random.choice(values)
def get_player_choice():
    return player_choice
def choose_heads(player_choice = 'heads'):
    return
def choose_tails(player_choice = 'tails'):
    return
def point_player():
    pass
def point_computer():
    pass
ttk.Button(mainframe, text='Heads', command=choose_heads).grid(column=1, row=3)
ttk.Button(mainframe, text='Tails', command=choose_tails).grid(column=3, row=3)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
