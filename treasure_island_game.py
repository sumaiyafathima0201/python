print("welcome to the treasure island")
print("your mission is to find Treasure")
choice1 = input('you are at a cross road , where you want to go ? if it left means type "left" and if it right means type "right".').lower()
if choice1 == "left":
    choice2 = (input('you have come to a lake , type "wait" to wait for the boat or type "swim" to swim ')).lower()
    if choice2 == "wait" :
           choice3 = print(input("you reached in an unharmed island . there is a house with three doors . choose colour between 'red' or 'blue' or 'yellow'"))
           if choice3 == "red" :
                  print("its a room full of fire, GAME OVER")
           elif choice3 == "yellow":
                  print("you won the game")
           elif choice3 == "blue":
                 print("you enter room full of beast, GAME OVER")
           else :
                 print("NO OPTIONS OF DOOR")
    else :
           print("you got attack by an shark, GAME OVER")
else: 
       print("you fell into a hole , GAME OVER")




