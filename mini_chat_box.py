# I am making a mini chat box who is able to answer certain questions
a = input("Hello Sir, Can I Know Your Name : ")
print("Hello", a )
b = input(f"(How Can I Help You : ")
if b == "Help me in my homework":
    c = input("What is your Homework : ")
    print("Sorry this type of question is not in my data ")
elif b == "lets play a game":
    print ("Lets Play Rock , Paper and Scissor")
    import random
choice = ["rock" , "paper" , "scissor"]
print("Lets Play Rock Paper and scissors game")
a = input("Choose rock paper or scissor : ")
b = random.choice(choice)
print("Mine is :", b)
if a == "paper" and b == "rock":
    print("Aw ! You win")
elif a == "scissor" and b == "paper" :
    print("You win")
elif a == "rock" and b =="scissor":
    print("You win")
else:
    print("I win Bro ! Yuu Huu") #completed
e = input("What is your Experience :")
if e == "bad":
    print("I will improve it.")
elif e == "good":
    print("Thank you, i wil improve more")
else:
    print("Thanks FOr Your Feedback.")
