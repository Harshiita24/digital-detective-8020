# Mission 3 — Understand the operating system

## 1. Task / objective
The goal of Mission 3 is to explore how the operating system acts as the core supervisor of the computer. This involves inspecting the local OS environment, identifying user identity, measuring storage allocation, observing active running processes, distinguishing between absolute and relative filesystem paths, decoding Unix file permissions, and explaining the fundamental responsibilities of modern operating systems.

## 2. Work completed
- Inspected the local operating system environment and documented privacy-safe observations for OS version, user identity, disk space capacity, and system activity.
- Examined running processes, process identifiers (PIDs), and the difference between user-facing applications and background system daemons.
- Explored filesystem navigation by comparing absolute paths against relative paths with concrete examples from this repository.
- Decoded Unix file permission strings (`-rw-r--r--`) on practice files, identifying owner read/write capabilities.
- Summarized the six major responsibilities of an operating system with clear definitions and everyday examples.

---

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the specific operating system, kernel version, platform architecture, and release build running on the machine. | `macOS 27.2.1` (Build `26B131`), Darwin Kernel Version `27.2.0`, running on an `arm64` 64-bit architecture (Apple Silicon). |
| **Current account identity** | Displays the short username of the currently logged-in account running the terminal session. | Running under user account `[redacted]` with default shell `/bin/zsh`. |
| **Available and used storage** | Shows storage volume partitioning, total size, consumed disk space, free space available, and filesystem mount point. | Root data volume `/dev/disk3s5` on `/System/Volumes/Data`: Total size `926 GiB`, Used `177 GiB`, Available `721 GiB` (approx. `20%` capacity used). |
| **System activity snapshot** | Provides a real-time status of CPU load, active threads, memory pressure, and currently running system services. | Observed multi-core CPU activity with system processes, kernel threads, and GUI window compositing (`WindowServer`) running alongside active apps. |

---

### Task 3.2 — Understand processes

- **What is a process?**
  A process is a program in active execution. When an application binary stored on an SSD is launched, the operating system loads its machine instructions into memory, allocates RAM for its variables and stack, sets up file descriptors, and schedules it to run on the CPU.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique numerical integer assigned by the operating system kernel to every single process at the moment it is created. The OS and user tools use the PID to track process status, allocate resources, manage parent-child relationships, and send signals (such as pause, resume, or terminate/kill).
- **Two examples of processes running on this computer:**
  1. **Application Process:** `Google Chrome` (or `VS Code`) — a user-facing foreground application with interactive windows handling user browsing, rendering tabs, and executing JavaScript.
  2. **Background System Process:** `WindowServer` (or `launchd`) — an operating system service running continuously in the background that manages display drawing, compositor layers, and window rendering across all monitors.

---

### Task 3.3 — Understand paths and permissions

#### Absolute Path vs Relative Path:
- **Absolute Path:** An absolute path specifies the complete location of a file or folder starting all the way from the root directory (`/`). It is always unambiguous and valid regardless of where the current terminal shell is positioned.
  - *Example from repository:* `/Users/[redacted]/.../digital-detective-8020/terminal-practice/sample.txt`
- **Relative Path:** A relative path specifies the location of a target file or folder starting from the **current working directory** where the shell is presently located. It does not begin with a leading forward slash (`/`).
  - *Example from repository root:* `terminal-practice/sample.txt` (or stepping up from inside a subfolder: `../README.md`).

#### File Permissions Analysis:
Inspected `sample.txt` inside `terminal-practice/` using `ls -l`:
```text
-rw-r--r--  1 [redacted]  staff  76B Nov 23 09:29 sample.txt
```

Breaking down the permission string `-rw-r--r--`:
- Initial character `-`: Indicates a standard regular file (a directory would start with `d`).
- First triplet (`rw-`): **Owner permissions**. The owner has **Read** (`r`) and **Write** (`w`) permissions, but not **Execute** (`-`). The owner can open and edit the file, but cannot run it as a program.
- Second triplet (`r--`): **Group permissions**. Members of the `staff` group have **Read-only** access.
- Third triplet (`r--`): **Others permissions**. All other users on the system have **Read-only** access.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Allows the file contents to be inspected or read into memory. | Opening `sample.txt` in a text editor or reading it with `cat`. |
| **w — Write** | Allows the file contents to be edited, appended, overwritten, or truncated. | Saving updates to `sample.txt` using `>>` or an editor. |
| **x — Execute** | Allows the file to be executed as an executable binary or shell script; on directories, allows traversing inside. | Running a compiled program, a bash script, or entering a directory via `cd`. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Schedules CPU time among competing programs so that multiple applications appear to run simultaneously without locking the system. | The OS rapidly switches CPU cores between a streaming music player, a code editor, and background downloads without audio stuttering. |
| **Memory management** | Allocates slices of physical RAM to active programs, isolates memory so apps cannot crash each other, and reclaims space when programs exit. | Allocating 1.2 GB of RAM to a web browser window when opened, and instantly returning that memory to the free pool when closed. |
| **Device management** | Manages communication between software programs and connected hardware peripherals through standardized device drivers. | Translating mouse sensor coordinates into on-screen cursor movements, or sending formatted raster data to a laser printer. |
| **File management** | Organizes data on storage drives into an orderly hierarchy of folders and files, handling file creation, deletion, access timestamps, and storage layout. | Tracking where file blocks live on the SSD and preventing two programs from corrupting the same text document simultaneously. |
| **User interface / shell** | Provides a visual desktop (GUI) or a text-based terminal (CLI) allowing human users to interact with and control the system. | Providing the graphical desktop window manager, menu bars, and the Zsh terminal command shell. |
| **Security and permissions** | Enforces user authentication, sandboxing, and file access rules to protect system integrity and keep private data safe from unauthorized access. | Prompting for Touch ID or password before installing system-level software, and restricting normal users from modifying root OS binaries. |

---

## 3. Commands / tools used
- `uname -mprsv`: Checked Darwin OS kernel details and hardware architecture.
- `sw_vers`: Identified macOS product name, version, and build identifier.
- `whoami`: Verified the currently active user account identity.
- `df -h .`: Inspected disk filesystem size, consumed storage, and remaining capacity.
- `ls -l` / `ls -lah`: Inspected file permission strings and decoded permission triplets.
- `pwd` and `cd`: Tested transitions between relative and absolute directory paths.

## 4. My understanding
Before this mission, I thought of an operating system simply as the visual screens and icons on my laptop. Digging into processes, storage tables, and permissions made me realize that the OS is essentially a resource manager and gatekeeper. Without it, software programs would collide trying to access the CPU at the exact same time, overwrite each other's RAM, and read each other's private files. Unix permission triplets provide a simple, clean way to ensure that sensitive files are protected while still letting legitimate programs do their work.

## 5. Difficulties faced
Reading Unix permission strings can look confusing at first because they appear as a string of letters and dashes (`-rw-r--r--`). It was important to remember that the ten characters are divided into one file-type flag followed by three distinct 3-character groups (owner, group, everyone else).

## 6. How I resolved them
I broke the permission string down into chunks: character 1 for type (`-` or `d`), characters 2-4 for user owner (`rw-`), characters 5-7 for group (`r--`), and characters 8-10 for others (`r--`). This made reading permissions mechanical and clear.

## 7. Evidence / files
- `mission-03-operating-system/README.md`: Completed operating system exploration, process questions, path analysis, permissions guide, and OS responsibilities table.

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Target branch:** `main`
- **Remote destination:** `https://github.com/Harshiita24/digital-detective-8020`
