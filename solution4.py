import random

# Getting password length from user
length = int(input("Enter the desired password length (between 3 and 15): "))

# Validating password length
if length < 3 or length > 15: 
    print("Password length should be between 3 and 15 characters.") 
    exit()

# Lists of characters to choose from
alphaInCapital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphaInSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '&']

genPass = ""

# Generating password
# Generating password
for i in range(length): 
    # Depending on the length of the password, choose characters from different lists
    if i % 4 == 0:
        genPass += random.choice(alphaInCapital)
    elif i % 4 == 1:
        genPass += random.choice(alphaInSmall)
    elif i % 4 == 2:
        genPass += random.choice(numbers)
    else:
        genPass += random.choice(symbols)

# Shuffling the characters in the genPass string
genPassList = list(genPass)
random.shuffle(genPassList)
mixed_genPass = ''.join(genPassList)

# Truncate the password to the desired length
mixed_genPass = mixed_genPass[:length]

print("Generated password:", mixed_genPass)
