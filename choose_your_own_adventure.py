name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You awaken at the end of a crossroads, it has come to an end and you can go either left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across (walk/swim). ").lower()

    if answer == "swim":
        print("You swim halfway across the river before you notice a ripple in the water. You were eaten by an alligator. You lose.")

    elif answer == "walk":
        print("You walk for many miles before succumbing to exhaustion, you ran out of water and collapse. You lose.")
        
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge. It looks unstable. Do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back to the main road and lose.")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stranger. They give you gold, you win!")

        elif answer == "no":
            print("You ignore the stranger. They are offended, you lose!")
    
        
    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

print("Thank you for playing", name)

