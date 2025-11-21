"""
Import nltk word library and tkinter
"""

from tkinter import *
import tkinter.messagebox
from tkinter import PhotoImage

import nltk 
nltk.download("words")
from nltk.corpus import words
    
from PossibleLetters import Alphabet



def game():    
    
    def welcome():
        width = screen.winfo_screenwidth()
        height = screen.winfo_screenheight()
        screen.geometry("%dx%d" % (width,height)) 
        screen.title("Simple Wordle: Player vs Player") 
        screen.configure(bg="#FFF8E7")
        
        Label(screen, text="Welcome to Wordle - Simple edition!").pack()
  
    def currentScreen(current,next):
        current.pack_forget()
        next.pack()

    def only_char(char):
        return char.isalpha()
    def only_nums(char):
        return char.isdigit()

    def screen1(root, frame1, frame2):    
        Label(frame1, text="Enter your secret 5-letter word:").pack()
        check = (frame1.register(only_char), "%S")
        Input = Entry(frame1, validate="key", validatecommand=check)
        Input.pack()
        Input.focus()
        def secret():
                word = Input.get()
                if (word.lower() in words.words()) and (len(word) == 5):
                    for letter in word:
                        secret_word.append(letter)
                    secret_word.pop(0)
                    currentScreen(frame1,frame2)
                    screen2(root, attempt_Frame, player_frame)
                elif (word.lower() in words.words()) and ((len(word) < 5) or (len(word) > 5)):
                        tkinter.messagebox.showinfo("Error", f"You entered a {len(word)}-letter word, but a 5-letter word is needed. Try again!")
                else:
                    tkinter.messagebox.showinfo("Error", "Not a valid word, try again!")

        
        Input.bind("<Return>", lambda event: secret())
        frame1.pack()
        return frame1

    def screen2(root, frame2, frame3):     
        Label(frame2, text="Input allowed number of attempts: ").pack()
        checknum = (frame2.register(only_nums), "%S")
        NChoice = Entry(frame2, validate="key", validatecommand=checknum)
        NChoice.pack()
        NChoice.focus()
        def answer():
            global N
            try:
                num = int(NChoice.get())
                if (1 <= num) and (num <= 5):
                    N = num
                    currentScreen(frame2,frame3)
                    screen3(root, player_frame, 0)
                else:
                    tkinter.messagebox.showinfo("Error", "Must input an integer between 1-5!")
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Must input a valid integer!")
        NChoice.bind("<Return>", lambda event: answer())
        
        frame2.pack()  
        return frame2
    
    def screen3(root, frame3, attempts):
        player_word = []
        choice = None 
        chance = None
        def new_attempt():
            nonlocal attempts, choice, chance


            if choice:
                choice.destroy()
            if chance:
                chance.destroy()
            
            attempts += 1
            chance = Label(frame3, text=f"Enter your attempt #{attempts}: ")
            chance.pack()

            check = (frame3.register(only_char), "%S")
            choice = Entry(frame3, validate="key", validatecommand=check)
            choice.pack()
            choice.focus()
            choice.bind("<Return>", lambda event: Pchoice())
            if attempts >= (N + 1):
                tkinter.messagebox.showinfo("Game Over", f"You used all {N} attempts. Better luck tomorrow!")
                screen.destroy()
                return

        new_attempt()

        def Pchoice():
            word = choice.get()
            if (word.lower() in words.words()) and (len(word) == 5):
                player_word.clear()
                for letter in word:
                    player_word.append(letter)
                

                letter_in_the_right_spot = 0
                for i in range(len(player_word)):
                    for r in range(len(secret_word)):
                        if (player_word[i] == secret_word[r]) and (i == r):
                            image = Alphabet(player_word[i])
                            if image:
                                Label(screen, image=image).pack()
                                print(f"{player_word[i]} is in the secret_word and in the correct spot #{i + 1}")
                                letter_in_the_right_spot += 1
                        elif (player_word[i] in secret_word):
                            print(f"{player_word[i]} is in the secret_word but not in the correct spot")
                        

                if player_word == secret_word:
                    print(f"Congrats you won using {attempts} attempt(s)")
                    tkinter.messagebox.showinfo("You Win!", f"Congrats! You guessed the word in {attempts} attempt(s).")
                    screen.destroy()
                else:
                    new_attempt()
                    
                    

            elif (word.lower() in words.words()) and ((len(word) < 5) or (len(word) > 5)):
                tkinter.messagebox.showinfo("Error", f"You entered a {len(word)}-letter word, but a 5-letter word is needed. Try again!")
            else:
                tkinter.messagebox.showinfo("Error", "Not a valid word, try again!")

        choice.bind("<Return>", lambda event: Pchoice())

    secret_word = [""]
    screen = tkinter.Tk()
    secret_frame = tkinter.Frame(screen)
    attempt_Frame = tkinter.Frame(screen)
    player_frame = tkinter.Frame(screen)
    welcome()
    screen1(screen, secret_frame, attempt_Frame)
    screen.mainloop() 

if __name__ == "__main__":
    game()
