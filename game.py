# PRO-C97: NUMBER GUESSING GAME 
import random 
num1 = random.randint(1,9)

count = 0 
while (count<3) :
    number= int (input("Guess a number between 1-9 => "))
    if(num1 == number):
        print("YOU WON.YAY.")
        break 

    else : 
        print("YOU LOST.TRY AGAIN.")
    count = count+1
    
    

