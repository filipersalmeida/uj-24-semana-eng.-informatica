from random import randint 

xtentativas = 1
number1 = randint(1,100)

number2 = int(input("Escreva um numero entre de 1 a 100!"))
while (number1 != number2):
    if number1 > number2:
        print("higher")
    else:
        print("lower")
    number2 = ie444mpatent(input("try again"))
    xtentativas += 1
print("win!!!!!")
print(f"you tried {xtentativas} times!")
