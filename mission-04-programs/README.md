# Mission 4 — How programs run

## 1. Task / objective
Understand how code written by humans actually runs on a computer. This involved making a simple Python script named `hello.py`, running it from the terminal, and comparing the difference between a compiler and an interpreter.

## 2. Work completed
- Created a one-line Python script called `hello.py` inside `mission-04-programs/` that prints `"Hello from Python"`.
- Ran the script in the terminal using `python3` and confirmed the message appeared.
- Made a comparison table between compilers and interpreters looking at when translation happens, what files they create, examples of each, and their main advantages.
- Wrote a short paragraph explaining the difference in my own words.

---

### Task 4.1 — Create and run a Python program
- File path: `mission-04-programs/hello.py`
- Code:
  ```python
  print("Hello from Python")
  ```
- Command used to run:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- Terminal output:
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire code file all at once before the program starts running. | Translates and runs the code line by line while the program is actively executing. |
| **Typical output** | Creates a standalone executable binary file (like a `.exe` or app file) that can run on its own. | Does not create a standalone executable file on disk; it executes statements directly in memory. |
| **One example** | C, C++, or Go. | Python, Ruby, or JavaScript. |
| **One advantage** | The program runs much faster because all translation is already finished ahead of time. | Much easier and faster for testing and debugging because you can make changes and run them right away without waiting to compile. |

#### Difference between a compiler and an interpreter:
A compiler translates the entire source code of a program into computer machine code all at once before you ever run it, creating a separate executable file. An interpreter, on the other hand, reads your code line by line and carries out each instruction as it goes. Because compiled programs are already in machine code, they run much faster and don't require the original code to be opened. But interpreted languages like Python make learning and writing code much friendlier because you can test small changes immediately without waiting for a build step.

---

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Ran the Python script from the terminal.
- Text editor: Used to write the code and fill in notes.

## 4. My understanding
Computers only understand 0s and 1s, so they cannot read English words like `print` directly. Compilers and interpreters are the tools that do the translation work for us. Compilers are like translating an entire book into another language before giving it to someone to read, while interpreters are like a live translator translating what someone says sentence by sentence in real time. Since Python is interpreted, if you make a syntax error on line 10, lines 1 through 9 will still execute until it reaches the mistake.

## 5. Difficulties faced
On some computers, typing `python` might give an error or try to run an older version.

## 6. How I resolved them
I always made sure to type `python3` in the terminal so it uses the modern Python 3 interpreter.

## 7. Evidence / files
- `mission-04-programs/hello.py`: Working Python program.
- `mission-04-programs/README.md`: Comparison table and notes.

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Branch: `main`
- Remote URL: `https://github.com/Harshiita24/digital-detective-8020`
