# Mission 4 — How programs run

## 1. Task / objective
Create and run `hello.py`, then compare compilers and interpreters.

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
A compiler translates source code before it runs, often producing an executable. An interpreter runs code through a runtime. Compiled programs can run efficiently, while interpreted workflows make it easy to try changes quickly.

---

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Ran the Python script from the terminal.
- Text editor: Used to write the code and fill in notes.

## 4. My understanding
Compilers translate code before execution; interpreters run it through a runtime. Python lets me test changes quickly. A syntax error prevents the script from starting, while a runtime error can happen after earlier lines have run.

## 5. Difficulties faced
The `python` command may be missing or point to an older version on some computers.

## 6. How I resolved them
I used `python3` to run the script with Python 3.

## 7. Evidence / files
- `mission-04-programs/hello.py`: Working Python program.
- `mission-04-programs/README.md`: Comparison table and notes.

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Branch: `main`
- Remote URL: `https://github.com/Harshiita24/digital-detective-8020`
