a = int(input("Enter a number to find that is prime number or not : "))
for i in range(2, a):
    if (a%i) == 0:
        print("This is not prime number")
        break
    else:
        print("This is prime number")
        break