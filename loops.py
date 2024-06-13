# hello 
import re
import math
def rootByFormula(a,b,c): 
    print("by formula")
    discriminant = (b ** 2) - (4*a*c)
    if discriminant < 0: 
        print("Root are imaginary. Can't calculate its root")
        exit()
    
    first_value = (-b + math.sqrt(discriminant)) / (2*a)
    second_value = (-b - math.sqrt(discriminant)) / (2*a)

    print(first_value, second_value)

def is_negative(s):
     number_str = str(s)
     return number_str and number_str[0] == "-"

def calculate_factors(product_ac, sum_b):
    
  if product_ac == 0 or sum_b == 0:
      # print("None... 1")
      return None  # Handle cases where product or sum is 0

  first_factor = abs(product_ac)
  second_factor = 1
  is_negative_sum = is_negative(sum_b)

  while True:
    factor = find_first_positive_factor(abs(first_factor))  # Use efficient factor finding
    # print(first_factor, second_factor, factor)
    # print("factor: ", factor)
    if factor is None:
      # print("None here...")
      break
    first_factor /= factor
    # print("first factor: ", first_factor)
    second_factor = second_factor * factor
    # print("second factor: ", second_factor)

    # a * c = -14
    # a + c = -5
    # 7 , 2

    if int(first_factor) + int(second_factor) == int(abs(sum_b)) and int(first_factor) * int(second_factor) == int(abs(product_ac)):
      # print("1")
      if is_negative(sum_b): 
        return [-first_factor, -second_factor]
      else:
        return [first_factor, second_factor]
    elif is_negative_sum and int(first_factor) - int(second_factor) == int(abs(sum_b)) and int(first_factor * second_factor) == abs(product_ac):
        # print("2")
        if first_factor > second_factor: return [-first_factor, second_factor]
        else: return [first_factor, -second_factor]
    elif abs(int(first_factor) - int(second_factor)) == int(abs(sum_b)) and int(abs(first_factor)) * int(abs(second_factor)) == int(abs(product_ac)):
        # print("3")
        return [first_factor, -second_factor]

  return None  # No factors found

def find_first_positive_factor(number):
    if number <= 1:
      return None

    for i in range(2, int(number**0.5) + 1):
      if number % i == 0:
        return i

    return number if number > 1 else None
    
def isFactor(number, factor):
    if number % factor == 0: return True
    else: return False


def find_hcf(x, y):
  # Handle the base case where one number is 0
  if x == 0:
    return y, 0, 1
  elif y == 0:
    return x, 1, 0

  # Use the Euclidean Algorithm to efficiently find HCF
  while y != 0:
    x, y = y, x % y

  # After the loop, x will hold the HCF
  return x, int(x / x), int(y / x)

def find_hcf_and_quotients(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    hcf = gcd(a, b)
    return [hcf, a // hcf, b // hcf]

def remove_extra_plus(expression):
    # Replace " + -" with " -"
    cleaned = re.sub(r'\s*\+\s*-', ' -', expression)
    # Replace " + " with " " only if there's no "-" sign following it
    cleaned = re.sub(r'\s*\+\s*(?=[^0-9]*$)', ' ', cleaned)
    return cleaned


def has_only_zero_after_decimal(number):
  # Convert the float to a string representation
  number_str = str(number)

  # Split the string at the decimal point
  parts = number_str.split(".")

  # Check if there is a decimal part (more than one part after splitting)
  if len(parts) > 1:
    # Check if the decimal part contains only '0' characters
    return all(char == '0' for char in parts[1])
  else:
    # No decimal part, so it's an integer, return False
    return False

  
while True: 
    a = float(input("Enter the cofficient of x^2 tern (a): "))
    b = float(input("Enter the cofficient of x tern (b): "))
    c = float(input("Enter the constant tern (c): "))
    # a = 1
    # b = -5
    # c = -14
    print(f"({int(a)})x^2 + ({int(b)})x + ({int(c)})")
   
    # print(not has_only_zero_after_decimal(str(a)), not has_only_zero_after_decimal(str(b)), not has_only_zero_after_decimal(str(c)))
    isNumberAreInDecimal = not has_only_zero_after_decimal(str(a)) or not has_only_zero_after_decimal(str(b)) or not has_only_zero_after_decimal(str(c))
    if isNumberAreInDecimal: 
      rootByFormula(a, b, c) 
      exit()
      
    a = int(a)
    b = int(b)
    c = int(c)
    product = a * c
    factors = calculate_factors(product, b)
    # print(factors)
    if factors == None:
        # print("worng equation no factors")
        rootByFormula(a,b,c)
        exit()
    
    # print(f"Number {int(b)} are split into {int(factors[0])} and {int(factors[1])}")
    isFirstNumberFactorOfConstant = isFactor(c, factors[0])
    isSecondNumberFactorOfConstant = isFactor(c, factors[1])
    # print (isFirstNumberFactorOfConstant, isSecondNumberFactorOfConstant)
    if not isFirstNumberFactorOfConstant:
      temp = factors[0]
      factors[0] = factors[1]
      factors[1] = temp
     
    print(f"({a})x^2 + ({factors[0]})x + ({factors[1]})x + ({c})")
    hcf1, first_number_after_hcf, second_number_after_hcf = find_hcf_and_quotients(int(abs(a)), int(abs(factors[0])))
    # print(is_negative(factors[0]), int(factors[0]))
    if is_negative(int(factors[0])): 
        second_number_after_hcf = -second_number_after_hcf
    else: 
        second_number_after_hcf = +second_number_after_hcf
    # hcfval = -hcf if is_negative(factors[0]) else hcf    
    s1 = f"({first_number_after_hcf}x + {second_number_after_hcf} )"
   
     
    hcf2, third_number_after_hcf, forth_number_after_hcf = find_hcf_and_quotients(int(abs(factors[1])), int(abs(c)))
    if is_negative(factors[0]): 
        forth_number_after_hcf = -forth_number_after_hcf
    else: 
        forth_number_after_hcf = +forth_number_after_hcf
    hcfval = -hcf2 if is_negative(factors[1]) else hcf2    
    s2 = f"({third_number_after_hcf}x + {forth_number_after_hcf} )"


    factor_first_term = f"({hcf1}x + {hcfval})"
    factor_first_term = remove_extra_plus(factor_first_term)
    factor_second_term = remove_extra_plus(s1)
    # IMP 
    print(factor_first_term, f"{factor_second_term}")

    print()
    if is_negative(hcfval): 
      print("x = ", abs(hcfval), "/", hcf1, " = ", abs(hcfval)/hcf1, "Ans.")
      # print("x = ", abs(hcfval)/hcf1)
    else:
      print(f"x = -{hcfval, "/", hcf1} = -{hcfval/hcf1} Ans.")
      # print(f"x = -{hcfval/hcf1}")
    
    if is_negative(second_number_after_hcf):
      print("x = ",abs(second_number_after_hcf), "/", first_number_after_hcf, " = ", abs(second_number_after_hcf)/first_number_after_hcf, "Ans.")
      # print("x = ",abs(second_number_after_hcf)/first_number_after_hcf)
    else:
      print(f"x = -{second_number_after_hcf, "/", first_number_after_hcf} = -{second_number_after_hcf/first_number_after_hcf} Ans.")
      # print(f"x = -{second_number_after_hcf/first_number_after_hcf}")
      
        
        
              
        
        