import tkinter as tk
from tkinter import messagebox
import random

class GuessGame:
    def __init__(game,master):
        game.master = master
        game.master.title("Full-Screen Number Guessing Game")
        game.master.attributes('-fullscreen',True)
        game.frame = tk.Frame(game.master , bg = "black" , padx = 50 , pady = 50)
        game.frame.pack(expand = True , fill = 'both')
        game.input()

    def input(game):
        for widget in game.frame.winfo_children():
            widget.destroy()

        title = tk.Label(game.frame , text = "Guessing Range", font = ("Times New Roman" , 32) , bg = "black" , fg = "white")
        title.pack(pady = 15)

        tk.Label(game.frame,text = "Starting Range : ",font = ("Times New Roman",20) , bg = "black" , fg = "white").pack()

        game.start_val = tk.Entry(game.frame , font = ("Times New Roman" , 20))
        game.start_val.pack(pady = 5)

        tk.Label(game.frame , text = "Ending Range : ",font = ("Times New Roman" , 20),bg = "black",fg = "white").pack()

        game.end_val = tk.Entry(game.frame , font = ("Times New Roman" , 20))
        game.end_val.pack(pady = 5)

        game.submit = tk.Button(game.frame , text = "Start Game",font = ("Times New Roman",18),
                                command = game.start)
        game.submit.pack(pady = 20)

    def start(game):
        try:
            game.start_range = int(game.start_val.get())
            game.end_range = int(game.end_val.get())

            if game.start_range >= game.end_range:
                return ValueError("starting must be lesser than the ending.")

            game.maximum_attempts = min(25 , max(5 , (game.end_range - game.start_range) // 4))
            game.secret_num = random.randint(game.start_range , game.end_range)
            game.remaining = game.maximum_attempts
            game.setup()

        except ValueError:
            messagebox.showerror("Invalid Input","Please enter the valid numbers (start < end).")

    def setup(game):
        for widget in game.frame.winfo_children():
            widget.destroy()

        tk.Label(game.frame , text = "Guessing a Number" , font = ("Times New Roman" ,34) , bg = "black" , fg = "white").pack(pady = 20)
        tk.Label(game.frame ,
                 text = f"Guess a number between {game.start_range} and {game.end_range}\nYou have {game.maximum_attempts} more attempts . ",
                 font = ("Times New Roman",20),bg = "black" , fg = "white").pack(pady = 20)

        game.entry = tk.Entry(game.frame , font = ("Times New Roman",24),width = 10)
        game.entry.pack()

        game.guess = tk.Button(game.frame , text = "Guess" , font = ("Times New Roman" , 20) , command = game.guess)
        game.guess.pack(pady = 20)

        game.msg = tk.Label(game.frame , text = "", font = ("Times New Roman", 24),bg = "black" , fg = "yellow")
        game.msg.pack(pady = 10)

        game.exit = tk.Button(game.frame , text = "Exit" , font = ("Times New Roman",16),command = game.master.destroy , bg = "red" , fg = "white")
        game.exit.pack(side = "bottom" , pady = 30)

    def guess(game):
        try:
            guess = int(game.entry.get())
            game.entry.delete(0 , tk.END)

            if guess < game.start_range or guess > game.end_range:
                game.msg.config(text = f"Guess must be between {game.start_range}-{game.end_range}.")
                return
            
            game.remaining -= 1
            

            if guess < game.secret_num:
                game.msg.config(text = f"Too low ! Attempts left: {game.remaining}")

            elif guess > game.secret_num:
                game.msg.config(text = f"Too high ! Attempts left : {game.remaining}")

            else:
                messagebox.showinfo("You Win ! ",f"You guessed it ! The number is {game.secret_num}.")
                game.master.destroy()
                return

            if game.remaining == 0:
                messagebox.showinfo("Game Over" , f"Out of attempts !\nThe number you missed is {game.secret_num}.")
                game.master.destroy()
            
        except ValueError:
            game.msg.config(text = "Please enter a valid number ..!")
        
if __name__ == "__main__":
    window = tk.Tk()
    app = GuessGame(window)
    window.mainloop()
            
            
            


    
        
                                
