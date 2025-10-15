import random
a =  input("Helllo Code Runner! What is your name ? : ")
print()
if a == "Prail":
    print("Hello Code Owner!")
else:
    print(f"Hello {a} !, Let's Play a game")


print()
print("The game is number guessing game ") 

print()
print("You will choose two mumbers")
print()
print("Then i will chose a random number and you will guess it !")
s = int(input("Enter a number : "))
u = int(input("Enter second number (greater than 1st number) ; "))
if u<=s :
    print("Error, Second number is smaller or equal to first number")
else:
    print("Let me choose a random number !")
    
d = random.randint(s,u)
i= int(input("Ok Guess the number i have choosed: "))

def check(i):
    if i == d :
        print("Damn ! You won Haha")
    else:
        print("Try again")
    
    l = int(input("Second Chance : "))
    if l == d :
          print("Damn ! You won Haha")
    else:
        print("Try again")
        
    m = int(input("Last Chance : "))
    if m == d :
          print("Damn ! You won Haha")
    else:
        print("Try again")
        
check(i)
        










"""if i==d :
    print("Damn ! You won Haha")
else:
    print("Try again :)")
k= int(input("Ok Guess the number 2nd chance: "))
if k==d :
    print("Damn ! You won Haha")
else:
    print("Try again")
y = input("Last Chance : ")
if y==d :
    print("You win !")
else :
    ("You loose run the code again to play again ")
print()
print(f"The number i have choesn was {d}")
print()
print(f"Thanks You for running this code {a}! Have a good day ") """