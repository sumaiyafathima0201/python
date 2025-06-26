print("welcome to love calculator")
name1 = input("what is your name ?")
name2 = input("what is your partner name ?")
combined_names = name1 + name2
lower_names= combined_names.lower() #to take all the user input as small letter even if they send in capital 
#calculating true and love
t = lower_names.count("t") #count is used for count how many t in names
r = lower_names.count("r") #same for r
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))
if score > 50 and score <=70 :
    print("you are like bunbutter and jam")
elif score > 70 and score < 90 :
    print("you are like sea and sand")
else :
    print("no worries find another partner !!! ")
