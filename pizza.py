print("Welcome to SUFA pizza Delivery")
size = input("you want  s or m or l:")

#add_extra_cheese = input("say yes if you want extra cheese or else say no ")
price = 0
if size == "s" :
    print("you have to pay 150 ")
    price = 150
elif size == "l":
    print("you have to pay 200 ")
    price= 200
else :
    print("you have to pay 400")
    price = 400
add_pepperoni = input("say yes if you want pepperoni or else say no: ")
if add_pepperoni == "yes":
    price += 50
add_extra_cheese = input("say yes if you want extra cheese or else say no: ")
if add_extra_cheese == "yes":
    price +=50
    print(f"your total price is {price}")

