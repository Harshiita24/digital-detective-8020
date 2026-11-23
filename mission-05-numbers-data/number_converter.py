#!/usr/bin/env python3
"""
Number Converter - The Digital Detective
Converts a user-supplied decimal integer into binary and hexadecimal representations.
"""

def main():
    print("==========================================")
    print("   Digital Detective: Number Converter    ")
    print("==========================================")
    
    user_input = input("Enter a positive decimal integer: ").strip()
    
    if not user_input.isdigit():
        print("Error: Please enter a valid non-negative whole number.")
        return
    
    decimal_value = int(user_input)
    
    # Python built-in conversion functions
    # bin() returns string starting with '0b'
    # hex() returns string starting with '0x'
    binary_full = bin(decimal_value)
    hex_full = hex(decimal_value)
    
    binary_raw = binary_full[2:]
    hex_raw = hex_full[2:].upper()
    
    print("\n--- Conversion Results ---")
    print(f"Decimal (Base 10):     {decimal_value}")
    print(f"Binary (Base 2):       {binary_raw}  (Prefix notation: {binary_full})")
    print(f"Hexadecimal (Base 16): {hex_raw}  (Prefix notation: {hex_full})")
    print("==========================================")

if __name__ == "__main__":
    main()
