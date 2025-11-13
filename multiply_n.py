# multiply_n.py
def multiply(numbers):
    """Multiply a list of numbers and return product."""
    prod = 1.0
    for n in numbers:
        prod *= n
    return prod

def parse_input(input_str):
    """Parse a space/comma separated string into floats."""
    sep = input_str.replace(',', ' ').split()
    return [float(x) for x in sep]

if __name__ == "__main__":
    try:
        s = input("Enter numbers (space or comma separated): ")
        nums = parse_input(s)
        if not nums:
            print("No numbers entered.")
        else:
            print("Product:", multiply(nums))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
