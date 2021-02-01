
import art
import random

# Rules
#    Rock wins against scissors.
#    Scissors win against paper.
#    Paper wins against rock.


if __name__ == '__main__':
    rps=[]
    rps.append(art.rock)
    rps.append(art.paper)
    rps.append(art.scissors)

    user_choice=int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors: "))
    print("Your Choice: ")
    print(rps[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer Choice: ")
    print(rps[computer_choice])
    if user_choice<0 or user_choice>2:
        print("Invalid choice")
    elif user_choice==0 and computer_choice==2:
        print("You Win")
    elif user_choice==2 and computer_choice==0:
        print("You Lose")
    elif user_choice>computer_choice:
        print("You Win")
    elif user_choice<computer_choice:
        print("You Lose")
    else:
        print("Draw")

# to add try except
#add while to ask to play again
# use def
#add readme
#optimize code


