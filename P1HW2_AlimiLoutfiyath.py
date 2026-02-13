# Loutfiyath Alimi
# 2/13/2026
# P1HW1
# This Program is to create some basic math on numbers



budget =int(input("enter your budget : "))
destination = input("enter your travel destination : ")
gaz = int(input("enter how much will you spend on gaz : "))
accomodation = int(input("enter how much will you spend on accomodation : "))
food = int(input("enter how much will you spent on food: "))


expenses = gaz + accomodation + food

result = budget - expenses

# Display the remainding Balance

print("-------- Travel Expenses--------")

print("\n " )
print(f"Gaz : {gaz}")
print(f"Accomodation : {accomodation}  ")
print(f"Food : {food} " )
print("\n " )

print(f"Remainding Balance is : {result}")
print("\n " )


