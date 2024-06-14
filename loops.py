import customtkinter
import re
import math

# Set up the CustomTkinter interface
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x450")
frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

a_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter the coefficient of x^2 term (a): ")
a_entry.pack(pady=10)
b_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter the coefficient of x term (b): ")
b_entry.pack(pady=10)
c_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter the constant term (c): ")
c_entry.pack(pady=10)

result_textbox = customtkinter.CTkTextbox(master=frame, width=450, height=150)
result_textbox.pack(pady=20)

def rootByFormula(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        result_textbox.configure(text="Root are imaginary. Can't calculate its root")
        return
    
    first_value = (-b + math.sqrt(discriminant)) / (2 * a)
    second_value = (-b - math.sqrt(discriminant)) / (2 * a)
    
    result_textbox.configure(text=f"Roots by formula: {first_value}, {second_value}")

def is_negative(s):
    number_str = str(s)
    return number_str and number_str[0] == "-"

def calculate_factors(product_ac, sum_b):
    if product_ac == 0 or sum_b == 0:
        return None

    first_factor = abs(product_ac)
    second_factor = 1
    is_negative_sum = is_negative(sum_b)

    while True:
        factor = find_first_positive_factor(abs(first_factor))
        if factor is None:
            break
        first_factor /= factor
        second_factor = second_factor * factor

        if int(first_factor) + int(second_factor) == int(abs(sum_b)) and int(first_factor) * int(second_factor) == int(abs(product_ac)):
            if is_negative(sum_b):
                return [-first_factor, -second_factor]
            else:
                return [first_factor, second_factor]
        elif is_negative_sum and int(first_factor) - int(second_factor) == int(abs(sum_b)) and int(first_factor * second_factor) == abs(product_ac):
            if first_factor > second_factor:
                return [-first_factor, second_factor]
            else:
                return [first_factor, -second_factor]
        elif abs(int(first_factor) - int(second_factor)) == int(abs(sum_b)) and int(abs(first_factor)) * int(abs(second_factor)) == int(abs(product_ac)):
            return [first_factor, -second_factor]

    return None

def find_first_positive_factor(number):
    if number <= 1:
        return None

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return i

    return number if number > 1 else None

def isFactor(number, factor):
    return number % factor == 0

def find_hcf(x, y):
    if x == 0:
        return y, 0, 1
    elif y == 0:
        return x, 1, 0

    while y != 0:
        x, y = y, x % y

    return x, int(x / x), int(y / x)

def find_hcf_and_quotients(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    hcf = gcd(a, b)
    return [hcf, a // hcf, b // hcf]

def remove_extra_plus(expression):
    cleaned = re.sub(r'\s*\+\s*-', ' -', expression)
    cleaned = re.sub(r'\s*\+\s*(?=[^0-9]*$)', ' ', cleaned)
    return cleaned

def has_only_zero_after_decimal(number):
    number_str = str(number)
    parts = number_str.split(".")
    if len(parts) > 1:
        return all(char == '0' for char in parts[1])
    else:
        return False

def calculate():
    try:
        a_str = a_entry.get().strip()
        b_str = b_entry.get().strip()
        c_str = c_entry.get().strip()
        
        print(f"a_str: '{a_str}', b_str: '{b_str}', c_str: '{c_str}'")
        
        a = float(a_str)
        b = float(b_str)
        c = float(c_str)
    except ValueError:
        result_textbox.delete(1.0, customtkinter.END)
        result_textbox.insert(customtkinter.END, "Please enter valid numerical values")
        return
    
    # result_textbox.delete(1.0, customtkinter.END)
    result_textbox.insert(customtkinter.END, "Calculating...\n")

    init(a, b, c)

def highlight_result(textbox, result):
    # Clear the textbox first
    textbox.delete(1.0, customtkinter.END)
    # Insert the result text
    textbox.insert(customtkinter.END, result)
    # Highlight the "Ans." part
    start_idx = "1.0"
    while True:
        start_idx = textbox.search("Ans.", start_idx, customtkinter.END)
        if not start_idx:
            break
        end_idx = f"{start_idx} + {len('Ans.')}c"
        textbox.tag_add("highlight", start_idx, end_idx)
        textbox.tag_config("highlight", foreground="red")
        start_idx = end_idx

def init(a, b, c):
    # result_textbox.delete(1.0, customtkinter.END)
  
    result = f"Equation: ({int(a)})x^2 + ({int(b)})x + ({int(c)})\n"
   
    isNumberAreInDecimal = not has_only_zero_after_decimal(str(a)) or not has_only_zero_after_decimal(str(b)) or not has_only_zero_after_decimal(str(c))
    if isNumberAreInDecimal:
        rootByFormula(a, b, c)
        return

    a = int(a)
    b = int(b)
    c = int(c)
    product = a * c
    factors = calculate_factors(product, b)
    if factors is None:
        rootByFormula(a, b, c)
        return

    isFirstNumberFactorOfConstant = isFactor(c, factors[0])
    isSecondNumberFactorOfConstant = isFactor(c, factors[1])
    if not isFirstNumberFactorOfConstant:
        temp = factors[0]
        factors[0] = factors[1]
        factors[1] = temp

    result += f"({a})x^2 + ({factors[0]})x + ({factors[1]})x + ({c})\n"
    hcf1, first_number_after_hcf, second_number_after_hcf = find_hcf_and_quotients(int(abs(a)), int(abs(factors[0])))
    if is_negative(int(factors[0])):
        second_number_after_hcf = -second_number_after_hcf
    else:
        second_number_after_hcf = +second_number_after_hcf

    s1 = f"({first_number_after_hcf}x + {second_number_after_hcf})"
    hcf2, third_number_after_hcf, forth_number_after_hcf = find_hcf_and_quotients(int(abs(factors[1])), int(abs(c)))
    if is_negative(factors[0]):
        forth_number_after_hcf = -forth_number_after_hcf
    else:
        forth_number_after_hcf = +forth_number_after_hcf
    hcfval = -hcf2 if is_negative(factors[1]) else hcf2
    s2 = f"({third_number_after_hcf}x + {forth_number_after_hcf})"

    factor_first_term = f"({hcf1}x + {hcfval})"
    factor_first_term = remove_extra_plus(factor_first_term)
    factor_second_term = remove_extra_plus(s1)
    result += f"Factors: {factor_first_term} {factor_second_term}\n"

    if is_negative(hcfval):
        result += f"x = {abs(hcfval)} / {hcf1} = {abs(hcfval) / hcf1} (Ans.)\n"
    else:
        result += f"x = -{hcfval} / {hcf1} = {-hcfval / hcf1} (Ans.)\n"
    
    if is_negative(second_number_after_hcf):
        result += f"x = {abs(second_number_after_hcf)} / {first_number_after_hcf} = {abs(second_number_after_hcf) / first_number_after_hcf} (Ans.)\n"
    else:
        result += f"x = -{second_number_after_hcf} / {first_number_after_hcf} = {-second_number_after_hcf / first_number_after_hcf} (Ans.)\n"

    highlight_result(result_textbox, result)

calculate_button = customtkinter.CTkButton(master=frame, text="Calculate", command=calculate)
calculate_button.pack(pady=20)

root.mainloop()


