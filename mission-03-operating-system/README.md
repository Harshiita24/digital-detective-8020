# Mission 3 — Understand the operating system

## 1. Task / objective
Explore how the operating system manages my laptop. This involved checking system information (OS version, user account, storage space), understanding what processes and PIDs are, learning the difference between absolute and relative paths, reading file permission letters (`rwx`), and explaining the main jobs of an operating system.

## 2. Work completed
- Checked my laptop's operating system version, active username, storage usage, and running system activity in the terminal.
- Looked up what a process and PID mean, with examples of foreground and background programs.
- Compared absolute paths with relative paths using examples from my assignment folder.
- Checked the permission letters on `sample.txt` to see what permissions the owner has.
- Explained the six main responsibilities of an operating system with simple everyday examples.

---

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Tells you which OS is running and what kind of processor the machine has. | Running `macOS` (Version 27.2.1, Darwin Kernel) on an Apple Silicon 64-bit chip (`arm64`). |
| **Current account identity** | Shows the username of the account currently logged into the terminal. | Logged in as user `[redacted]` using the Zsh shell. |
| **Available and used storage** | Shows how much storage space is on the drive and how much is free. | Disk partition `/dev/disk3s5`: Total size `926 GiB`, Used `177 GiB`, Free `721 GiB` (about `20%` space used). |
| **System activity snapshot** | Gives a quick look at CPU usage and running programs. | Observed system tasks and background services running smoothly with low overall CPU load. |

---

### Task 3.2 — Understand processes

- **What is a process?**
  A process is just any program that is actively running on the computer. When you click an app to open it, the computer loads its instructions into RAM, gives it system resources, and it becomes a running process.
- **What does the PID column represent?**
  PID stands for **Process ID**. It is a unique identification number that the operating system assigns to every single running program so it can keep track of them, give them CPU time, or shut them down if they freeze.
- **Two examples of processes running on my laptop:**
  1. **Google Chrome** (or **VS Code**): An application running in the foreground that I interact with directly.
  2. **WindowServer**: A background system process that macOS uses to draw windows, buttons, and graphics on the screen.

---

### Task 3.3 — Understand paths and permissions

#### Absolute Path vs Relative Path:
- **Absolute Path:** The full, complete address of a file starting from the very root of the computer (`/`). No matter what folder your terminal is currently in, an absolute path always points to the exact same file.
  - *Example:* `/Users/[redacted]/.../digital-detective-8020/terminal-practice/sample.txt`
- **Relative Path:** The address of a file based on where your terminal is currently standing. It does not start with a `/`.
  - *Example:* `terminal-practice/sample.txt` (or `../README.md` to look one folder up).

#### Understanding File Permissions:
I checked `sample.txt` with `ls -l` and got:
```text
-rw-r--r--  1 [redacted]  staff  76B Nov 23 09:29 sample.txt
```

Breaking down `-rw-r--r--`:
- The first dash `-` means it is a regular file (not a folder).
- The next three letters `rw-` are the **Owner permissions**:
  - `r` (Read): Yes, I can open and read the file.
  - `w` (Write): Yes, I can edit and save changes to the file.
  - `-` (Execute): No, I cannot run it like a program.
- The remaining letters (`r--r--`) mean group members and other users can only read the file, but cannot edit it.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Lets you open and view the file's text. | Opening `sample.txt` to read what is written inside. |
| **w — Write** | Lets you edit, add text, or save changes to the file. | Modifying the file or adding a line with `>>`. |
| **x — Execute** | Lets you run the file as a program or script. | Running a bash script or Python file from the terminal. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Decides which running program gets to use the CPU and for how long, switching between them quickly so nothing freezes. | Letting me listen to music in the background while typing code in VS Code without the music pausing. |
| **Memory management** | Gives chunks of RAM to open apps so they have room to work, and takes it back when an app closes. | Giving 500 MB of RAM to a browser window, and freeing that RAM when I close the tab. |
| **Device management** | Helps apps talk to hardware like keyboards, mice, screens, and printers using drivers. | Turning my mouse movements into the cursor moving across the screen. |
| **File management** | Keeps all files and folders organized on the hard drive so data doesn't get lost or corrupted. | Saving my documents into folders and letting me find them easily later. |
| **User interface / shell** | Gives humans a way to control the computer, either through clickable icons (GUI) or text commands (CLI). | The macOS desktop with the dock and windows, or the Terminal app. |
| **Security and permissions** | Protects system files and makes sure one user or app cannot mess with another user's private data. | Asking for my password or fingerprint before installing new software. |

---

## 3. Commands / tools used
- `uname -mprsv`: Checked my Mac's kernel and processor type.
- `sw_vers`: Showed macOS version and build number.
- `whoami`: Displayed my current logged-in user account.
- `df -h .`: Checked total, used, and free storage on my drive.
- `ls -l`: Checked file permissions and file sizes.

## 4. My understanding
I used to think the operating system was just the desktop background and windows. Doing this mission helped me realize it does all the heavy lifting behind the scenes. Without an operating system, programs wouldn't know how to share the screen, memory, or processor, and would crash into each other. File permissions also make a lot of sense now; they prevent unauthorized apps or users from accidentally overwriting important files.

## 5. Difficulties faced
Looking at the permission string `-rw-r--r--` looked like random letters at first glance.

## 6. How I resolved them
I broke it down into chunks: the first character tells you if it's a file or folder, and then the next 9 characters are split into three sets of three (owner, group, and everyone else). Once I looked at it that way, it was really simple to read.

## 7. Evidence / files
- `mission-03-operating-system/README.md`: System specs, process notes, path explanations, and permissions table.

## 8. Commit details
- Commit message: `Document operating system and file management`
- Branch: `main`
- Remote URL: `https://github.com/Harshiita24/digital-detective-8020`
