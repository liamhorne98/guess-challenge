import random
number = random.randint(1,10)
guess_tries = 3
while guess_tries<=3:
    guess_int = int(input("guess the number:"))
    if guess_int==number:
        print ("You win")
        break
    else:
        print("You lose")
        guess_tries=guess_tries-1
        if guess_tries==0:
            break