line1 = ["⬜","⬜","⬜"]
line2 = ["⬜","⬜","⬜"]
line3 = ["⬜","⬜","⬜"]
map = [line1, line2, line3]
print("Hiding your  Treasue ! X mark the stop.")
position = input() #where you want to put the treasure
letter = position[0].lower() #POSITION 0 IS FOR INPUT FIRST THING
var = ["a" , "b", "c"] #THREE POSSIBLE LETTERS TO WRITE IN INPUT
letter_index = var.index(letter)  #IN ABC IF USER CHOOSE B MEANS INDEX GOING TO GIVE 1 OR A MEANS 0 
number_index = int(position[1]) - 1 #POSITION 1 IS FOR INPUT SECOND THING
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}") #TO MAKE 3X3 GRID
