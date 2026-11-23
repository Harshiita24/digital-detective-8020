# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The goal of Mission 2 is to gain confidence working directly with the Unix command-line interface. This includes executing fundamental file and directory manipulation commands (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`), understanding how redirection (`>` vs `>>`) works, comparing flag variations (`ls` vs `ls -lah`), using pipelines to connect processes (`ls -la | head -n 5`), and explaining the role of a package manager like Homebrew.

## 2. Work completed
- Practiced the nine essential terminal operations inside the repository and documented what each command does alongside actual terminal observations.
- Created an isolated `terminal-practice/` directory to experiment safely with text file creation, overwriting, appending, copying, and renaming.
- Analyzed command flags by comparing standard directory output against a detailed listing with hidden entries and human-friendly file size units.
- Tested Unix pipeline redirection by feeding directory output into the `head` command, examining how the data stream flows from one program into another.
- Inspected the local package manager (Homebrew `7.0.12`) and recorded its version and managed packages.

---

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display** (`pwd`) | Prints the full absolute path from the root directory to the folder where the shell is currently positioned. | Output showed the full working directory path (`/Users/[redacted]/.../digital-detective-8020`). |
| **Directory listing** (`ls`) | Lists visible file and folder names in the current directory in alphabetical columns. | Displayed mission folders (`mission-00-setup` to `mission-08-final-report`), `README.md`, and `evidence`. |
| **Detailed listing** (`ls -l`) | Displays entries in a long list format showing Unix file permissions, link counts, owner, group, file size in bytes, and last modification timestamp. | Showed detailed permission strings like `-rw-r--r--` for files and `drwxr-xr-x` for directories. |
| **Change directory** (`cd ..` then `cd digital-detective-8020`) | Navigates upward into the parent folder, or down into a named subdirectory. | Stepping up (`cd ..`) changed the shell path to the parent folder. Returning (`cd digital-detective-8020`) brought the shell back to the project root. |
| **Create directory** (`mkdir terminal-practice`) | Creates a new subdirectory with the given name if it does not already exist. | Created the new directory `terminal-practice/` inside the repository. |
| **Create empty file** (`touch terminal-practice/sample.txt`) | Creates a blank 0-byte file, or updates the modification time of an existing file without altering its contents. | A new text file named `sample.txt` was created with initial size 0 bytes. |
| **Copy file** (`cp terminal-practice/sample.txt terminal-practice/sample-copy.txt`) | Duplicates the source file to a new target path, leaving the original file completely untouched. | A separate duplicate file `sample-copy.txt` appeared in the practice folder with matching contents. |
| **Move / rename file** (`mv terminal-practice/sample-copy.txt terminal-practice/sample-renamed.txt`) | Moves a file to another location or changes its filename within the same directory without duplicating data blocks. | `sample-copy.txt` was renamed to `sample-renamed.txt`; the old name ceased to exist. |
| **Display file contents** (`cat terminal-practice/sample.txt`) | Concatenates and streams the raw text content of a file directly to standard output in the terminal. | Printed the stored text lines directly to the terminal screen without opening an interactive GUI editor. |

---

### Task 2.2 — Practise file changes safely
Inside `terminal-practice/`, I created `sample.txt` and practiced text manipulation:
1. Wrote initial line: `echo "Line 1: Investigating digital artifacts." > terminal-practice/sample.txt`
2. Appended second line: `echo "Line 2: Appending findings safely." >> terminal-practice/sample.txt`
3. Verified both lines using `cat terminal-practice/sample.txt`:
   ```text
   Line 1: Investigating digital artifacts.
   Line 2: Appending findings safely.
   ```
4. Made a backup copy and renamed it:
   ```bash
   cp terminal-practice/sample.txt terminal-practice/sample-backup.txt
   mv terminal-practice/sample-backup.txt terminal-practice/sample-renamed.txt
   ```

#### Conceptual Questions:
- **What is the difference between replacing a file's contents and adding text to the end?**
  The single chevron operator (`>`) truncates the destination file to zero bytes before writing, completely overwriting whatever was previously stored. The double chevron operator (`>>`) appends new text to the end of the existing file stream, preserving everything already there.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) creates an independent duplicate of the file in another location, consuming additional disk space. Moving (`mv`) renames the file or adjusts its filesystem directory pointer; the original entry disappears from the source location, and no duplicate is created.
- **What information does the current-directory display provide?**
  `pwd` (Print Working Directory) provides the exact absolute path from the filesystem root (`/`) down to the specific folder where the terminal is active. This prevents mistakes such as creating or deleting files in the wrong directory.
- **Why is a directory-listing operation useful?**
  `ls` gives immediate visibility into what files, directories, and hidden dotfiles exist in a folder. Without it, you would have to guess file names blindly before running commands.

---

### Task 2.3 — Understand flags and pipes

#### Flags comparison (`ls` vs `ls -lah`):
- `ls`: Shows only visible file and directory names in simple columns without metadata.
- `ls -lah`:
  - `-l`: Formats output as a long list with permissions, ownership, byte size, and timestamps.
  - `-a`: Displays all entries, including hidden files and directories starting with a dot (like `.git` and `.DS_Store`).
  - `-h`: Formats file sizes in human-readable units (`K`, `M`, `G`) instead of raw byte counts (e.g., `3.6K` instead of `3640`).

#### Pipeline test (`ls -la | head -n 5`):
- Command run: `ls -la | head -n 5`
- Output observed:
  ```text
  total 8
  drwxr-xr-x@ 15 [redacted]  staff   480 Nov 23 09:29 .
  drwxr-xr-x@  4 [redacted]  staff   128 Nov 23 09:12 ..
  drwxr-xr-x@ 12 [redacted]  staff   384 Nov 23 09:29 .git
  -rw-r--r--@  1 [redacted]  staff  3640 Nov 23 09:23 README.md
  ```
- **What the pipe (`|`) does:**
  The pipe operator takes the standard output (`stdout`) of the program on its left and connects it directly into the standard input (`stdin`) of the program on its right.
- **What each side contributes:**
  - Left side (`ls -la`): Generates the full detailed listing of all files and directories in the current folder.
  - Right side (`head -n 5`): Filters the incoming stream from the left, prints only the first five lines, and discards the rest.

---

### Task 2.4 — Understand package managers
- **Check Homebrew version:** `brew --version`
  - Output: `Homebrew 7.0.12`
- **Managed packages inspection:** `brew list`
  - Homebrew is currently managing packages on this system including `git`, `python@3.10`, `python@3.14`, `curl`, `ffmpeg`, `cmake`, and `sqlite`.

#### Why package managers are useful:
A package manager automates finding, downloading, compiling, configuring, and updating software libraries from trusted repositories. Instead of manually searching websites for DMG or tarball installers, resolving missing dependencies by hand, and struggling with uninstallation, a single command like `brew install <tool>` downloads the software and all its required prerequisite libraries automatically into standardized system paths. It also makes updating all system development tools as simple as running `brew upgrade`.

---

## 3. Commands / tools used
- `pwd`: Confirmed active working directory.
- `ls`, `ls -l`, `ls -lah`: Inspected folder contents with flags for detailed permissions and human-readable units.
- `cd`: Navigated up and down directory paths.
- `mkdir`: Created the `terminal-practice` sandbox folder.
- `touch`: Created initial empty practice files.
- `echo ... >` and `echo ... >>`: Practiced file overwriting and appending.
- `cp`: Created backup file duplicates.
- `mv`: Renamed files safely.
- `cat`: Read file contents directly in terminal.
- `|` (pipe) with `head -n 5`: Streamed and truncated output.
- `brew --version` and `brew list`: Inspected local macOS package manager configuration.

## 4. My understanding
The terminal is much faster and more precise than relying only on a graphical file manager (Finder). By combining commands with flags, we can alter how tools format output, and by using pipes, we can chain simple, focused single-purpose tools together into powerful pipelines. Practicing safe file operations inside a dedicated subfolder also taught me the importance of checking whether a redirect uses `>` or `>>` before running it, because accidentally typing `>` can erase an important file instantly.

## 5. Difficulties faced
A common slip when first using redirect operators is forgetting whether `>` replaces or appends. When testing, typing `>` a second time overwrote the first line rather than adding to it.

## 6. How I resolved them
I checked `cat sample.txt`, saw only the second line remained, and re-tested carefully using `>>` to confirm that appending leaves the original content intact and writes to the next line.

## 7. Evidence / files
- `mission-02-terminal/README.md`: Documented command tables, questions, flag explanations, and pipeline analysis.
- `terminal-practice/sample.txt`: Verified two-line appended text file.
- `terminal-practice/sample-renamed.txt`: Renamed copy of the practice file.

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Target branch:** `main`
- **Remote destination:** `https://github.com/Harshiita24/digital-detective-8020`
