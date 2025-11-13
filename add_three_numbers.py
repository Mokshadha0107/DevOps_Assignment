# add_three_numbers.py
def add_three_numbers(a, b, c):
    return a + b + c

if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        total = add_three_numbers(num1, num2, num3)
        print("The sum of the three numbers is:", total)
    except ValueError:
        print("Please enter valid numbers only.")
