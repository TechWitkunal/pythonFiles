age = int(input("Enter your age: "))
you = ""

if age >= 0 and age < 13: 
    you = "Child"
elif age <= 19: 
    you = "Teenager"
elif age <= 59: 
    you = "Adult"
elif age >= 60: 
    you = "Senior"
else:
    you = ""
    print("Enter correct age")


print("You are: ", you)