from datetime import datetime

# geting age form user
age = int(input("Enter your age: "))

# getting current day 
now = datetime.now()
day = now.strftime("%A")

# if age is above 18 or equal than price = 12 else 8
price = 12 if age >= 18 else 8
if day == "Wednesday": price -= 2

print("Ticket price for you is:", "$",price)