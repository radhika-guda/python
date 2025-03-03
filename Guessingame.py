# using While loop to build number guessing GAME

Secret_number=9
Guess_count=0
Guess_limit=3
while Guess_count<Guess_limit:
    guess=int(input("Guess:"))
    Guess_count+=1
    if guess==Secret_number:
        print("You won!")
        break
else:
    print("Sorry You failed!")


