import math

minicalc = float(input("Input any decimal number: "))
area = float(input("Radius - area: "))
area = math.pi * math.pow(area, 2)

correct_code = "1q2w3e4r5t6y7u8i9o0p"
attempts = 4

while attempts > 0:
    code = input("CODE: ")
    if code == correct_code:
        print(f"Ceil: {math.ceil(minicalc)}")
        print(f"Floor: {math.floor(minicalc)}")
        print(f"Rounded: {round(minicalc)}")
        print(f"SqrRoot: {math.sqrt(minicalc)}")
        print(f"Rpow: {math.pow(minicalc, 2)}")
        print(f"Abs+: {abs(minicalc)}")
        print(f"The area is: {area}")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong Code!!! You have {attempts} attempt(s) left.\n")
        else:
            print("Too many wrong attempts. Exiting...")
