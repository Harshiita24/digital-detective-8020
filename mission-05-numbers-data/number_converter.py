# Number Converter - The Digital Detective
# Converts a decimal number to binary and hexadecimal using Python built-in functions

def main():
    print("--- Number Converter ---")
    user_input = input("Enter a positive decimal number: ").strip()
    
    if not user_input.isdigit():
        print("Please enter a valid positive whole number.")
        return
    
    decimal_number = int(user_input)
    binary_result = bin(decimal_number)
    hex_result = hex(decimal_number)
    
    print(f"Decimal:     {decimal_number}")
    print(f"Binary:      {binary_result}")
    print(f"Hexadecimal: {hex_result}")

if __name__ == "__main__":
    main()
