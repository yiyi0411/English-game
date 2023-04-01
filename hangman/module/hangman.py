# -*-coding:UTF-8-*- 
import numpy as np
import string, time
import pandas as pd
from datetime import datetime

class HangmanGame:
    def __init__(self, vocdb, life):
        self.__count = 0
        self.__life = life
        self.__vocdb = vocdb
        n_voc = vocdb.shape[0]
        pos = np.random.randint(0, n_voc)
        self.__ansdb = vocdb.iloc[pos-2:pos+3, :3]
        self.__ans = vocdb.iloc[pos, 1].lower()
        self.__ans_lst = list(self.__ans)
        self.__n = len(self.__ans_lst)
        self.__puzzle_lst = list('_' * self.__n)
        self.__guess_lst = []
        self.__dbf = True
        self.__case = string.ascii_lowercase + "()' "
        self.__help = 2
        print(f"This word has [{self.__n}] letters, and you have [{self.__life}] chances to guess!")
        
    def guess(self, guess):
        self.__count += 1
        self.__case = self.__case.replace(guess.lower(), "")
        round_ = f"*************** Round[{self.__count}] ***************"
        display(round_, clear = True)
        help_ = f"************ Help Times:[{self.__help}] ************"
        display(help_)
        if(guess in self.__ans_lst):
            pos = self.__ans_lst.index(guess)
            hitf = "Hit!"
            if(self.__ans_lst.count(guess) > 1):
                for i in range(pos, self.__n):
                    if(self.__ans_lst[i] == guess):
                        self.__puzzle_lst[i] = guess
            else:
                self.__puzzle_lst[self.__ans_lst.index(guess)]  = guess   
        else:
            self.__life -= 1
            hitf = "No Hit!"
        display(hitf)
        myans = "".join(self.__puzzle_lst)
        # print(myans)
        if(self.__life > 0 and myans == self.__ans):
            mylife = f'*************** Life [{self.__life}] **************'
            display(mylife)
            return 1
            
        #Not game ends 
        elif(self.__life > 0 and myans != self.__ans):
            # self.__guess_lst = list(self.__guess_lst)
            if(guess not in self.__guess_lst):
                self.__guess_lst.append(guess)
                guess_lst = self.__guess_lst
            else:
                guess_lst = "You have guessed this letter!"
            self.__guess_lst = list(np.sort(self.__guess_lst))
            mylife = f'*************** Life [{self.__life}] ***************'
            display(mylife)
            h1 = "Puzzle:"
            display(h1)
            display(self.__puzzle_lst)
            h2 = "Letters:"
            display(h2)
            display(guess_lst)
            display("****************************************")
            h3 = "You can use following letters!"
            display(h3)
            display("["+self.__case+"]")
            display("---------------------------------------")
        else:
            #life ==0:game fails
            mylife = f'*************** Life [{self.__life}] ***************'
            display(mylife)
            return 0
    
    def need_help(self):
        if(self.__life > 0):
            self.__help -= 1
            self.__life -= 1
            tips = []
            for i in range(self.__n):
                if(self.__puzzle_lst[i] == '_'):
                    tips.append(i)
            tip = np.random.randint(low=0, high=len(tips))
            guess = self.__ans_lst[tips[tip]]
            pos = self.__ans_lst.index(guess)
            if(tips[tip] == 0):
                self.__dbf == False
            if(self.__ans_lst.count(guess) > 1):
                for i in range(pos, self.__n):
                    if(self.__ans_lst[i] == guess):
                        self.__puzzle_lst[i] = guess
            else:
                # self.__puzzle_lst[self.__ans_lst.index(guess)]  = guess
                self.__puzzle_lst[tips[tip]] = guess
            result = self.guess(guess)
            display("***************  Help  ***************")
            display(f"You got the [{guess}] !")
            display("---------------------------------------")
            return result
            # self.__count += 1
            # self.__case = self.__case.replace(guess, "")
            # self.__guess_lst.append(guess)
            # display("***************  Help  ***************", clear=True)
            # round_ = f"*************** Round[{self.__count}] ***************"
            # display(f'*************** Life [{self.__life}] ***************')
            # display(f"You got the [{guess}] !")
            # display("Puzzle:")
            # display(self.__puzzle_lst)  
            # h2 = "Letters:"
            # display(h2)
            # display(self.__guess_lst)
            # display("****************************************")
            # h3 = "You can use following letters!"
            # display(h3)
            # display("["+self.__case+"]")
            # display("---------------------------------------")
        #     return 1
        # else:
        #     return 0
        
    def get_vocdb(self):
        self.__life -= 3
        return self.__vocdb
    
    def get_ans(self):
        return self.__ans
    
    def get_dbf(self):
        return self.__dbf
    
    def get_life(self):
        return self.__life
    
    def set_life(self, life):
        self.__life = life
        
    def get_help(self):
        return self.__help
    
    def get_ansdb(self):
        return self.__ansdb