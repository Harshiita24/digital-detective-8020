# Mission 5 — Numbers and data

## 1. Task / objective
The goal of Mission 5 is to understand how computers represent numerical values and text using binary bits. This involves performing manual number conversions by hand across decimal (base 10), binary (base 2), and hexadecimal (base 16) formats, verifying the arithmetic using Python's built-in functions, writing an interactive Python utility (`number_converter.py`) that converts decimal inputs into binary and hex, and explaining character encoding standards (ASCII vs. UTF-8).

## 2. Work completed
- Worked through seven manual conversion problems by hand showing step-by-step arithmetic (successive division, positional weighting, and 4-bit nibble mapping).
- Verified every calculation using Python's interactive interpreter and confirmed complete agreement.
- Implemented and executed `number_converter.py`, testing positive integer inputs (42, 100, and 255) and recording the results.
- Investigated ASCII and UTF-8 encoding mechanisms, documented the decimal values for uppercase `'A'` and lowercase `'a'`, explained the necessity of character encodings, and gave non-ASCII character examples.

---

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary** | **Method: Repeated division by 2**<br>• 13 ÷ 2 = 6, Remainder = **1** (LSB)<br>• 6 ÷ 2 = 3, Remainder = **0**<br>• 3 ÷ 2 = 1, Remainder = **1**<br>• 1 ÷ 2 = 0, Remainder = **1** (MSB)<br>Reading remainders from bottom to top (MSB to LSB): **`1101₂`**<br>*(Verification: 8 + 4 + 0 + 1 = 13)* |
| **Convert decimal 25 to binary** | **Method: Repeated division by 2**<br>• 25 ÷ 2 = 12, Remainder = **1** (LSB)<br>• 12 ÷ 2 = 6, Remainder = **0**<br>• 6 ÷ 2 = 3, Remainder = **0**<br>• 3 ÷ 2 = 1, Remainder = **1**<br>• 1 ÷ 2 = 0, Remainder = **1** (MSB)<br>Reading remainders from bottom to top: **`11001₂`**<br>*(Verification: 16 + 8 + 0 + 0 + 1 = 25)* |
| **Convert binary 1010 to decimal** | **Method: Sum of positional powers of 2**<br>• Bit 3 (value 2³ = 8): 1 × 8 = 8<br>• Bit 2 (value 2² = 4): 0 × 4 = 0<br>• Bit 1 (value 2¹ = 2): 1 × 2 = 2<br>• Bit 0 (value 2⁰ = 1): 0 × 1 = 0<br>Total = 8 + 0 + 2 + 0 = **`10₁₀`** |
| **Convert binary 1101 to decimal** | **Method: Sum of positional powers of 2**<br>• Bit 3 (value 2³ = 8): 1 × 8 = 8<br>• Bit 2 (value 2² = 4): 1 × 4 = 4<br>• Bit 1 (value 2¹ = 2): 0 × 2 = 0<br>• Bit 0 (value 2⁰ = 1): 1 × 1 = 1<br>Total = 8 + 4 + 0 + 1 = **`13₁₀`** |
| **Convert hexadecimal A to decimal** | **Method: Hexadecimal single-digit value**<br>In base 16, values 10 through 15 are denoted by letters A through F (A=10, B=11, C=12, D=13, E=14, F=15).<br>• Position 16⁰: A = 10 × 16⁰ = 10 × 1 = **`10₁₀`** |
| **Convert hexadecimal 1F to decimal** | **Method: Positional powers of 16**<br>• Digit '1' (position 16¹): 1 × 16¹ = 16<br>• Digit 'F' (position 16⁰, F = 15): 15 × 16⁰ = 15 × 1 = 15<br>Total = 16 + 15 = **`31₁₀`** |
| **Convert binary 1111 to hexadecimal** | **Method: 4-bit nibble grouping**<br>Evaluate binary 1111 in decimal: (1 × 8) + (1 × 4) + (1 × 2) + (1 × 1) = 8 + 4 + 2 + 1 = 15.<br>In base 16, the decimal number 15 is represented by the single symbol **`F`**.<br>Answer: **`F₁₆`** (or `0xF`) |

---

### Task 5.2 — Verify using Python

| Conversion tested | Python expression | Result observed | Matches manual calculation? |
| :--- | :--- | :--- | :---: |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes |
| Binary 1010 to decimal | `int("1010", 2)` | `10` | Yes |
| Binary 1101 to decimal | `int("1101", 2)` | `13` | Yes |
| Hexadecimal A to decimal | `int("A", 16)` | `10` | Yes |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` | Yes |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes |

All manual calculations match Python's built-in numeric evaluation functions exactly.

---

### Task 5.3 — Build a small number converter
I implemented `number_converter.py` inside this folder. The program prompts the user for a decimal integer, parses it with `int()`, uses `bin()` and `hex()` for the transformations, strips the leading notation prefixes (`0b` and `0x`), and prints clean tabular results.

#### Explanation of Python conversion functions:
- `bin(x)`: Converts an integer `x` into a binary string prefixed with `'0b'`. It represents how the value is composed in powers of two.
- `hex(x)`: Converts an integer `x` into a lowercase hexadecimal string prefixed with `'0x'`. It groups bits into 4-bit chunks (nibbles) for compact display.

#### Testing Results:

| Test number | Binary output | Hexadecimal output |
| :---: | :--- | :--- |
| **42** | `101010` (Prefix: `0b101010`) | `2A` (Prefix: `0x2a`) |
| **100** | `1100100` (Prefix: `0b1100100`) | `64` (Prefix: `0x64`) |
| **255** | `11111111` (Prefix: `0b11111111`) | `FF` (Prefix: `0xff`) |

---

### Task 5.4 — How is text stored?

- **ASCII decimal codes:**
  - Uppercase **`A`**: **`65`** (Binary: `01000001`, Hex: `0x41`)
  - Lowercase **`a`**: **`97`** (Binary: `01100001`, Hex: `0x61`)
  *(Notice that uppercase and lowercase letters differ by exactly 32, meaning a single bit flip in bit-position 5 changes case!)*

- **Why a computer needs an encoding standard:**
  Computers only store electrical high and low voltages that represent binary 0s and 1s; they have no native concept of the alphabet. An encoding standard functions like a universal dictionary that assigns a specific numeric code to every character, ensuring that text written on one machine displays accurately on another without turning into meaningless symbols.

- **Example of a character not part of basic ASCII:**
  The Indian Rupee symbol **`₹`** (Unicode code point `U+20B9`, encoded in UTF-8 as three bytes: `0xE2 0x82 0xB9`), or the Euro sign **`€`**, or an emoji like **`💻`**. Basic ASCII only defines 128 characters (codes 0 to 127), which covers basic English letters, digits, and control characters, but cannot represent international currencies, accents, or symbols without UTF-8.

---

## 3. Commands / tools used
- Python 3 interactive shell / one-liners: Verified mathematical conversions and ASCII ordinal values using `ord('A')` and `ord('a')`.
- `python3 mission-05-numbers-data/number_converter.py`: Executed and tested the interactive conversion script.
- Terminal standard input redirection (`<<<`): Passed test integers directly into the script.

## 4. My understanding
Base systems are simply different ways of counting the same physical quantities. Humans use decimal (base 10) because we have ten fingers. Computers use binary (base 2) because transistors have two stable physical states: on (1) or off (0). Hexadecimal (base 16) was invented for human programmers because long binary strings like `11111111` are tedious and prone to typos; since exactly four binary bits equal one hexadecimal digit, hex gives us a compact shorthand for binary data.

Similarly, text encoding bridges human communication and binary memory. ASCII was a great initial standard for English, but the internet requires global communication, which is why UTF-8 has become the universal standard by supporting over a million characters while remaining backward-compatible with 7-bit ASCII.

## 5. Difficulties faced
When doing repeated division for decimal-to-binary by hand, it is easy to accidentally write the remainder digits from top to bottom instead of bottom to top, which reverses the most significant and least significant bits.

## 6. How I resolved them
I double-checked my manual binary strings against the sum of powers of two (e.g. 16 + 8 + 1 = 25). If the arithmetic did not match 25, I knew the bits had been reversed. Verifying with Python's `bin()` function provided a final check.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`: Interactive Python conversion script.
- `mission-05-numbers-data/README.md`: Documented arithmetic proofs, Python checks, test run tables, and text encoding notes.

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Target branch:** `main`
- **Remote destination:** `https://github.com/Harshiita24/digital-detective-8020`
