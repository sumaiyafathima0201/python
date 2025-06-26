import random
game_images = ["rock", "paper" , "scissor"] #creating a list here
user_choose = int(input("what do you choose ? type 0 for rock , type 1 for paper or type 2 for scissor .\n "))
if user_choose >= 3 or user_choose < 0 :
    print("you choose an invalid number , you lose !")
else :
    print(game_images[user_choose]) # inside the bracket the user input will go based upon the input it take the item from the list
computer_choose = random.randint(0,2)
print(f"computer choice : ")
print(game_images[computer_choose])# inside the bracket the computer random input will go based upon the input it take the item from the list

if user_choose == 0 and computer_choose == 2: 
    print("you win ! ")
elif  user_choose == 2 and computer_choose == 0 :
    print("computer wins !")
elif computer_choose > user_choose :
    print ("you lose ! ")
elif user_choose > computer_choose :
    print ("you win !")
elif user_choose == computer_choose :
    print ("Draw Match !")
