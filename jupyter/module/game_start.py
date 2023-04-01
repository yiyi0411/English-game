# -*-coding:UTF-8-*- 
import numpy as np
import string, time
import pandas as pd
from datetime import datetime

def game_start(game):
    case = list(string.ascii_lowercase) + ["(", ")", "'"," "]
    vocdb = game.get_vocdb()
    game.set_life(game.get_life()+3)
    while(1):
        guess = input("Use tips or\nGuess letter:")
        guess = guess.lower()
        if(game.get_life() <=  0):
            display("Fail the game!", clear=True)
            print("Sorry! You don't have enough lifes!")
            print(f"Sorry! Answer is {game.get_ans()}.")
            display(game.get_ansdb().style.hide(axis='index'))
            break

        elif(guess == "help"):
            helpt = game.get_help()
            if(helpt > 0):
                result = game.need_help()
                if(result == 1):
                    display("You win the game!", clear=True)
                    print(f"Answer is {game.get_ans()}.")
                    display(game.get_ansdb().style.hide(axis='index'))
                    break
                elif(result == 0):
                    display("Fail the game!", clear=True)
                    print(f"Sorry! Answer is {game.get_ans()}.")
                    display(game.get_ansdb().style.hide(axis='index'))
                    break
            else:
                s = "You can't use this any more!"
                display(s, clear=True)

        elif(guess == "db"):
            # db = game.get_vocdb()
            rows = 10
            flag = game.get_dbf()
            if(flag == True):
                game.get_vocdb()
                mylife = game.get_life()
                if(mylife <= 0):
                    print("Life is 0!")
                    print("Fail the game!")
                    print(f"Sorry! Answer is {game.get_ans()}.")
                    display(game.get_ansdb().style.hide(axis='index'))
                    break

                elif(mylife > 0 and mylife < 2):
                    print("You don't have enough lifes!") 

                else:
                    for i in range(int(vocdb.shape[0]/rows)):
                        pos = rows*i
                        db = game.get_vocdb()
                        db = db.iloc[0+pos:rows+pos,:2+1]
                        h = f'*************** Life [{mylife}] ***************'
                        display(h, clear=True)
                        display(db.style.hide(axis='index'))
                        time.sleep(2)
                    game.set_life(mylife)
                    db = "Time's Up!"
                    life = (f'*************** Life [{game.get_life()}] ***************')
                    display(db, clear=True)
                    display(life)
            else:
                s = "You can't use this any more!"
                display(s, clear=True)

        elif(guess == "dbp"):
            rows = 10
            flag = game.get_dbf()
            numbers = [str(i) for i in range(int(vocdb.shape[0]/rows)+1)]
            if(flag == True):
                past = datetime.now()
                now = datetime.now()
                dt = 0
                game.get_vocdb()
                mylife = game.get_life()
                if(mylife <= 0):
                    print("Life is 0!")
                    print("Fail the game!")
                    print(f"Sorry! Answer is {game.get_ans()}.")
                    display(game.get_ansdb().style.hide(axis='index'))
                    break

                elif(mylife > 0 and mylife < 2):
                    print("You don't have enough lifes!")                     

                else:                  
                    db = game.get_vocdb()
                    db = db.iloc[:rows,:2]
                    display(mylife, clear=True)
                    display(db.style.hide(axis='index'), clear=True)
                    while(dt <= 30):
                        page = input("Page:")
                        if(page not in numbers):
                            s = "No this page"
                            display(s, clear=True)

                        else:
                            page = int(page)
                            page -= 1
                            now = datetime.now()
                            dt = abs(past.second - now.second)
                            if(dt > 30):
                                break

                            # for i in range(int(vocdb.shape[0]/rows)):
                            pos = rows * page
                            db = game.get_vocdb()
                            db = db.iloc[0+pos:rows+pos,:2+1]
                            display(mylife, clear=True)
                            display(db.style.hide(axis='index'), clear=True)
                    game.set_life(mylife)
                    db = "Time's Up!"
                    life = (f'*************** Life [{game.get_life()}] ***************')
                    display(db, clear=True)
                    display(life)
            else:
                s = "You can't use this any more!"
                display(s, clear=True)


        elif(guess in case and game.get_life() > 0):
            result = game.guess(guess)
            if(result == 1):
                display("You win the game!", clear=True)
                print(f"Answer is {game.get_ans()}.")
                display(game.get_ansdb().style.hide(axis='index'))
                break
            elif(result == 0):
                display("Fail the game!", clear=True)
                print(f"Sorry! Answer is {game.get_ans()}.")
                display(game.get_ansdb().style.hide(axis='index'))
                break
        elif(guess == "exit"):
            print("Exit the game!")
            break
        else:
            print("It is not allowed!")