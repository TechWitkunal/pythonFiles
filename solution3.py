# geting age form user
score = int(input("Enter your score: "))

if score >= 101 or score < 0: 
    print("Please enter valid marks b/w 0 and 100")
    exit()

# if age is above 18 or equal than price = 12 else 8
if score < 60: grade = "F"
elif score <= 69: grade = "D" 
elif score <= 79: grade = "C" 
elif score <= 89: grade = "B" 
elif score <= 100: grade = "A" 

print("Your grade is: ", grade)