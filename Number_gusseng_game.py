import random 
a = random.randint(1, 30)
print("Lets play Number Guessing game")
print("I will give you some hints also")
b = int(input("Choose a number between 1 to 30: "))
if b == a :
    print("You Win!")
elif b < a :
    print("Your Number is smaller")
else:
    print("Your Number is Greater")
    
print("The Correct number is", a )
    
