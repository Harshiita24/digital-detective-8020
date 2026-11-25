# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Practice file commands, writing and appending text, flags, pipes, and package managers in the terminal.

## 2. Work completed
- Practiced nine fundamental terminal commands inside the assignment folder and wrote down what each command did and what I saw on screen.
- Made a separate folder called `terminal-practice/` where I created a text file, added lines using `>` and `>>`, and made a renamed backup copy.
- Tested different flags with `ls` to see how hidden files and file sizes are displayed.
- Tested the pipe symbol by connecting `ls -la` to `head -n 5`.
- Checked Homebrew on my Mac to see which version is installed and what packages it manages.

---

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display** (`pwd`) | Shows the complete folder path where the terminal is currently working. | Printed `/Users/[redacted]/.../digital-detective-8020`. |
| **Directory listing** (`ls`) | Lists the names of files and folders inside the current folder. | Showed all my mission folders like `mission-00-setup`, `README.md`, etc. |
| **Detailed listing** (`ls -l`) | Shows files in a detailed list with permissions, owner, size, and date modified. | Showed details like `-rw-r--r--` for files and `drwxr-xr-x` for folders. |
| **Change directory** (`cd ..` then `cd digital-detective-8020`) | Moves up to the parent folder or into a specific subfolder. | Moving up changed my current path, and typing `cd digital-detective-8020` brought me right back. |
| **Create directory** (`mkdir terminal-practice`) | Makes a brand new folder. | Created a new folder named `terminal-practice` inside the project. |
| **Create empty file** (`touch terminal-practice/sample.txt`) | Creates a new blank file. | Created an empty file named `sample.txt`. |
| **Copy file** (`cp terminal-practice/sample.txt terminal-practice/sample-copy.txt`) | Makes an exact duplicate of a file with a new name. | Created a second copy called `sample-copy.txt` while keeping the original. |
| **Move / rename file** (`mv terminal-practice/sample-copy.txt terminal-practice/sample-renamed.txt`) | Renames a file or moves it to a new location. | `sample-copy.txt` was renamed to `sample-renamed.txt`. |
| **Display file contents** (`cat terminal-practice/sample.txt`) | Prints the text inside a file right onto the terminal screen. | Printed out the text lines stored in the file without opening an editor. |

---

### Task 2.2 — Practise file changes safely
Inside the `terminal-practice/` folder, I created `sample.txt` and tested writing and appending text:
1. Added the first line: `echo "Line 1: Investigating digital artifacts." > terminal-practice/sample.txt`
2. Added the second line: `echo "Line 2: Appending findings safely." >> terminal-practice/sample.txt`
3. Displayed the file using `cat terminal-practice/sample.txt` to confirm both lines were there:
   ```text
   Line 1: Investigating digital artifacts.
   Line 2: Appending findings safely.
   ```
4. Made a backup copy and renamed it:
   ```bash
   cp terminal-practice/sample.txt terminal-practice/sample-backup.txt
   mv terminal-practice/sample-backup.txt terminal-practice/sample-renamed.txt
   ```

#### Answers to questions:
- **What is the difference between replacing a file's contents and adding text to the end?**
  When you use a single arrow (`>`), it wipes out whatever was already in the file and replaces it with the new text. When you use a double arrow (`>>`), it leaves the old content alone and adds the new line to the very end of the file.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) leaves the original file where it was and creates a second duplicate file somewhere else. Moving (`mv`) either renames the file or shifts it to a new folder, so the original file disappears from the old spot.
- **What information does the current-directory display provide?**
  `pwd` shows the exact path of where you are right now in the computer's folder tree. It helps make sure you don't accidentally create, edit, or delete files in the wrong place.
- **Why is a directory-listing operation useful?**
  `ls` lets you see what files and folders are around you. Without it, you would have to guess file names completely in the dark.

---

### Task 2.3 — Understand flags and pipes

#### Flags (`ls` vs `ls -lah`):
- `ls`: Just gives a simple list of file names in plain columns.
- `ls -lah`:
  - `-l`: Shows extra details like permissions, owner, size, and date.
  - `-a`: Shows hidden files too (files that start with a dot, like `.git`).
  - `-h`: Makes file sizes easy to read (like showing `3.6K` or `480B` instead of long numbers of bytes).

#### The Pipe (`|`):
- Command used: `ls -la | head -n 5`
- What I saw:
  ```text
  total 8
  drwxr-xr-x@ 15 [redacted]  staff   480 Nov 23 09:29 .
  drwxr-xr-x@  4 [redacted]  staff   128 Nov 23 09:12 ..
  drwxr-xr-x@ 12 [redacted]  staff   384 Nov 23 09:29 .git
  -rw-r--r--@  1 [redacted]  staff  3640 Nov 23 09:23 README.md
  ```
- **What the pipe symbol does:**
  The pipe symbol (`|`) takes the output of the command on the left and immediately feeds it as the input to the command on the right.
- **What each side does:**
  - Left side (`ls -la`): Lists every file and folder in detail.
  - Right side (`head -n 5`): Catches that list, grabs only the first five lines, and prints them out.

---

### Task 2.4 — Understand package managers
- **Homebrew version:** `Homebrew 7.0.12`
- **Packages managed:** It manages developer tools on my laptop like `git`, `python@3.10`, `curl`, `ffmpeg`, and `sqlite`.

#### Why package managers are useful:
A package manager installs and updates tools and their dependencies. For example, `brew install <tool>` installs a tool through Homebrew.

---

## 3. Commands / tools used
- `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat` for file tasks.
- `>` and `>>` for writing and appending text.
- `|` (pipe) with `head -n 5` to filter output.
- `brew --version` and `brew list` to inspect Homebrew.

## 4. My understanding
The terminal became easier with practice. I learned that `>` replaces file contents, while `>>` adds to them, so I used a separate practice folder.

## 5. Difficulties faced
I used `>` instead of `>>` when adding a second line and overwrote the first line.

## 6. How I resolved them
I checked the file with `cat sample.txt` and added the lines again using `>>` for the second line.

## 7. Evidence / files
- `mission-02-terminal/README.md`: Terminal notes, questions, and observations.
- `terminal-practice/sample.txt`: Practice text file with two lines.
- `terminal-practice/sample-renamed.txt`: Renamed backup file.

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Branch: `main`
- Remote URL: `https://github.com/Harshiita24/digital-detective-8020`
