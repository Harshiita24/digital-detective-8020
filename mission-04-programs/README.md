# Mission 4 — How programs run

## 1. Task / objective
The goal of Mission 4 is to investigate how source code written by human developers is converted into instructions a computer's CPU can carry out. This involves creating and executing a minimal Python script (`hello.py`) from the terminal, comparing how compilers and interpreters process programming languages, and evaluating the engineering trade-offs between ahead-of-time compilation and runtime interpretation.

## 2. Work completed
- Created `hello.py` inside `mission-04-programs/` containing a single print statement displaying `"Hello from Python"`.
- Executed the script from the command line using `python3 mission-04-programs/hello.py` and verified the output stream.
- Built a detailed comparison table between compilers and interpreters analyzing timing, output artifacts, language examples, and technical advantages.
- Wrote a clear explanation in my own words breaking down how compilers and interpreters translate and execute software.

---

### Task 4.1 — Create and run a Python program
- File path: `mission-04-programs/hello.py`
- Program code:
  ```python
  print("Hello from Python")
  ```
- Command used to run:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- Observed terminal output:
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translation happens entirely ahead of time (AOT) in a dedicated build step before the program runs. | Translation happens instruction-by-instruction at runtime while the program is actively executing. |
| **Typical output** | A standalone binary executable file containing native machine code (e.g., an ELF binary, Mach-O executable, or `.exe`). | No permanent binary executable file saved on disk; instructions are translated into temporary bytecode/memory operations executed immediately by the interpreter. |
| **One example** | C / C++ (`gcc` or `clang`), Rust (`rustc`), or Go. | Python (`python3`), Ruby, or PHP. |
| **One advantage** | Maximum runtime execution speed and performance optimization, along with detecting syntax and type errors before any user runs the code. | Immediate developer feedback loop with zero compile delays, highly interactive debugging, and code portability across platforms that have the interpreter installed. |

#### Difference between a compiler and an interpreter:
A compiler translates an entire source code file into native machine instructions all at once before the program is ever launched, producing a standalone executable file that the CPU runs directly. In contrast, an interpreter reads and evaluates source code statements line by line while the application is active, executing the logic dynamically without generating a separate binary on disk. Because compiled binaries talk directly to the processor hardware, they run significantly faster and do not require developer tools installed on the end-user's computer. Interpreters, however, make programming and testing far quicker because you can alter code and run it instantly without waiting for a lengthy compilation step, making them ideal for scripting, experimentation, and rapid software development.

---

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Ran the Python 3 interpreter against the source script.
- `cat`: Verified file contents prior to execution.
- Text editor: Created and formatted the Python script and mission documentation.

## 4. My understanding
Computers and processors can only understand binary electrical instructions (machine code). Because human beings cannot easily write millions of raw binary bits, we write code in high-level languages like Python, C, or Rust. Compilers do all the translation work upfront so the computer gets raw machine code ready for top speed, while interpreters act like a real-time translator sitting between our code and the processor. I also learned that modern Python actually uses a hybrid approach: CPython compiles `.py` files into intermediate bytecode (`.pyc`), and the Python Virtual Machine (PVM) interprets that bytecode at runtime.

## 5. Difficulties faced
Running Python files using the bare command `python` can sometimes trigger an error or call an outdated Python 2 environment on macOS systems.

## 6. How I resolved them
I explicitly used `python3`, ensuring that macOS invokes the modern Python 3.9 interpreter installed on the path.

## 7. Evidence / files
- `mission-04-programs/hello.py`: Python script displaying `"Hello from Python"`.
- `mission-04-programs/README.md`: Program execution verification and compiler vs interpreter analysis.

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Target branch:** `main`
- **Remote destination:** `https://github.com/Harshiita24/digital-detective-8020`
