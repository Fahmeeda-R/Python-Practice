secret_num=6
while True:
    num=int(input("Guess the number:"))
    if num == secret_num:
        print("You are correct!")
        break
    elif num >= secret_num:
        print("Too high")
    else:
        print("Too low")