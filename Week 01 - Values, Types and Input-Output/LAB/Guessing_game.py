from random import randint

User_guess = False
print("hello user!, welcome to the random number guessing game!")
print("=" * 40)
Goal_number = randint(1, 100)
print("A random number between 1 and 100 has been generated.")
User_guess = int(input("Please try to guess it: "))
if User_guess == Goal_number:
    print("Congraulations! You guessed correctly!")
    User_guess = True
elif User_guess == Goal_number + 1 or User_guess == Goal_number - 1:
    print("So Close, you were off by just one!")
elif User_guess > 100 or User_guess < 1:
    print("the generated number is between 1 and 100, please try again!!")
while User_guess != Goal_number:
    User_guess = int(input("Please try to guess it: "))
    if User_guess == Goal_number:
        print("Congratulations you guessed correctly!")
        User_guess = True
    elif User_guess == Goal_number + 1 or User_guess == Goal_number - 1:
        print("So close!, you were off by just one!")
    elif User_guess > 100 or User_guess < 1:
        print("the number generated is between 1 and 100, please try again!")