import random
list=["Rock","Paper","Scissor"]
choice=1
print("==Welcome to Rock-Paper-Scissor game==")
while(choice):
    computer_choice=random.choice(list)
    user_choice=input("Enter your move (Rock/Paper/Scissor) : ")
    print("User_choice =  ",user_choice,"|| Computer_choice = ",computer_choice)
    if(user_choice==computer_choice):
        print("Tie, you both choses same move.")
    elif(user_choice=="Paper"):
        if(computer_choice=="Rock"):
            print("Paper beats Rock, Congratulations You win!!!")
        else:
            print("Scissor beats Paper, Computer win!!!")
    elif(user_choice=="Scissor"):
        if(computer_choice=="Paper"):
            print("Scissor beats Paper, Congratulations You win!!!")
        else:
            print("Rock beats Scissor, Computer win!!!")
    elif(user_choice=="Rock"):
        if(computer_choice=="Paper"):
            print("Paper beats Rock, Congratulations You win!!!")
        else:
            print("Rock beats Scissor, Computer win!!!")
    else:
        print("Enter valid move:")
    print('1. To continue game enter "1"')
    print('2. For Quit enter "0')
    choice=int(input("Enter your choice."))
print("==Thanks for playing Rock-paper-Scissor game==")

