# Mission 5 — Numbers and data

## 1. Task / objective
Learn how computers work with numbers and text in memory. This meant converting numbers by hand between decimal (base 10), binary (base 2), and hexadecimal (base 16), checking the math using Python in the terminal, writing a Python program (`number_converter.py`) to convert numbers automatically, and understanding how character encodings like ASCII and UTF-8 store letters.

## 2. Work completed
- Worked out seven number conversion problems step by step on paper and recorded the steps.
- Checked all calculations in the Python shell using `bin()`, `hex()`, and `int()`.
- Built and tested `number_converter.py`, running it with test values 42, 100, and 255.
- Looked up the ASCII codes for 'A' and 'a', explained why computers need character encoding, and gave an example of a character that basic ASCII cannot store.

---

### Task 5.1 — Convert numbers by hand

#### 1. Convert decimal 13 to binary
- Divide 13 by 2 repeatedly and write down remainders:
  - 13 ÷ 2 = 6, remainder 1
  - 6 ÷ 2 = 3, remainder 0
  - 3 ÷ 2 = 1, remainder 1
  - 1 ÷ 2 = 0, remainder 1
- Read remainders from bottom to top: **`1101`**
- Check: 8 + 4 + 0 + 1 = 13.

#### 2. Convert decimal 25 to binary
- Divide 25 by 2 repeatedly and write down remainders:
  - 25 ÷ 2 = 12, remainder 1
  - 12 ÷ 2 = 6, remainder 0
  - 6 ÷ 2 = 3, remainder 0
  - 3 ÷ 2 = 1, remainder 1
  - 1 ÷ 2 = 0, remainder 1
- Read remainders from bottom to top: **`11001`**
- Check: 16 + 8 + 0 + 0 + 1 = 25.

#### 3. Convert binary 1010 to decimal
- Multiply each bit by its power of 2 (from right to left: 1, 2, 4, 8):
  - (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)
  - = 8 + 0 + 2 + 0 = **`10`**

#### 4. Convert binary 1101 to decimal
- Multiply each bit by its power of 2:
  - (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)
  - = 8 + 4 + 0 + 1 = **`13`**

#### 5. Convert hexadecimal A to decimal
- In hexadecimal, the letters A through F represent values 10 through 15.
- Therefore, A = **`10`**

#### 6. Convert hexadecimal 1F to decimal
- In base 16, the right digit is 16^0 (ones) and the left digit is 16^1 (sixteens).
- '1' is in the 16s spot: 1 × 16 = 16
- 'F' is in the 1s spot (F = 15): 15 × 1 = 15
- Add them together: 16 + 15 = **`31`**

#### 7. Convert binary 1111 to hexadecimal
- Calculate decimal value of binary 1111:
  - (1 × 8) + (1 × 4) + (1 × 2) + (1 × 1) = 8 + 4 + 2 + 1 = 15
- In hexadecimal, 15 is written as the letter **`F`**.
- So binary 1111 in hex is **`F`** (or `0xf`).

---

### Task 5.2 — Verify using Python

| Conversion tested | Python expression | Result observed | Matches manual calculation? |
| :--- | :--- | :--- | :---: |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes |
| Binary 1010 to decimal | `int("1010", 2)` | `10` | Yes |
| Binary 1101 to decimal | `int("1101", 2)` | `13` | Yes |
| Hex A to decimal | `int("A", 16)` | `10` | Yes |
| Hex 1F to decimal | `int("1F", 16)` | `31` | Yes |
| Binary 1111 to hex | `hex(0b1111)` | `'0xf'` | Yes |

All the results matched what I got by hand.

---

### Task 5.3 — Build a small number converter
I wrote `number_converter.py` using Python's built-in functions:
- `input()` takes the number typed by the user as text.
- `int()` turns that text into an actual integer number.
- `bin()` converts the integer to a binary string starting with `0b`.
- `hex()` converts the integer to a hexadecimal string starting with `0x`.

#### Test runs:

| Test number | Binary output | Hexadecimal output |
| :---: | :--- | :--- |
| **42** | `0b101010` | `0x2a` |
| **100** | `0b1100100` | `0x64` |
| **255** | `0b11111111` | `0xff` |

---

### Task 5.4 — How is text stored?

- **ASCII codes for 'A' and 'a':**
  - Uppercase **`A`** is decimal **`65`** (in binary: `01000001`).
  - Lowercase **`a`** is decimal **`97`** (in binary: `01100001`).
  - The difference between them is exactly 32.

- **Why computers need an encoding standard:**
  Computers can only store numbers (0s and 1s), not actual alphabet letters. An encoding standard gives every letter a specific number so that when you save text on one computer, another computer reads the same numbers and shows the same words instead of gibberish.

- **Example of a character not in basic ASCII:**
  The Indian Rupee symbol **`₹`** (or the Euro sign **`€`**, or emojis like **`💻`**). Basic ASCII only goes up to 127 and only includes standard English letters and numbers, so newer standards like UTF-8 are needed to support symbols and other languages.

---

## 3. Commands / tools used
- Python 3 interactive shell: Used `bin()`, `hex()`, and `ord('A')` to verify calculations.
- `python3 mission-05-numbers-data/number_converter.py`: Ran the converter with test numbers.

## 4. My understanding
Binary makes total sense once you realize that computer hardware is just millions of tiny switches that can only be either on (1) or off (0). Hexadecimal is really helpful because writing out long lines of 0s and 1s is slow and easy to mess up; since 4 binary bits make exactly 1 hex digit, hex is just a neat shorthand for humans to read binary data. Seeing how ASCII turns 'A' into 65 also helped me understand how text actually sits inside computer memory.

## 5. Difficulties faced
When doing decimal-to-binary by hand, it was easy to accidentally write the remainder numbers from top to bottom instead of bottom to top.

## 6. How I resolved them
I checked my answer by adding the powers of two back up (like 16 + 8 + 1 = 25). If it didn't add up to my starting number, I knew I had flipped the remainders. Checking with `bin()` in Python confirmed the right order.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`: Python converter program.
- `mission-05-numbers-data/README.md`: Manual calculations, verification table, test runs, and encoding notes.

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Branch: `main`
- Remote URL: `https://github.com/Harshiita24/digital-detective-8020`
