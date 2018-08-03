''' This program is to find the secret number'''
print("Please think of the number between 0 and 100")
High = 100
Low = 0
N = 0
S = 50
print("Is your secret number" + str(50))
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.")
print("Enter 'c' to indicate I guessed correctly.")
while 1:
    N = int((Low+High)/2)
    print("Is your secret number" + str(N))
    X = input()
    if X == 'h':
        High = N
    elif X == 'l':
        Low = N
    elif X == 'c':
        print("Game over. Your secret number was:" + str(N))
        break
    else:
        print("Sorry, I did not understand your input")
        break
