from random import randint
number1 = randint(1,3)
    
    #1: ROCK
    #2: PAPER 
    #3: SCISSORS

number2 = int(input("Escolhe um numero de 1 a 3 (1-rock, 2-paper, 3-scissors)"))
if number1 == number2:
    print("draw")
          
        
elif number1 == 1 and number2 == 2:
    print("win")

