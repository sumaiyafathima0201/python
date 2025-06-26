import random
name = ["ASRA", "ZUBAIDA", "ASMA", "SHABANA", "ARSHIYA", "FHAKMITHA", "SUMAIYA"]
num_items = len(name)
random_choice = random.randint(0, num_items-1)
person_who_will_pay =name[random_choice]
print(person_who_will_pay+" "+"have to pay the bill")