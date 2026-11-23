# The Digital Detective: Explore Your Computer & Build a Mini System Report
**Diwali Independent Learning Assignment**

A hands-on exploration of how personal computers work, from hardware and terminal commands to operating systems, Python scripts, binary numbers, Git, and networking.

---

## Student Information

| Field | Details |
| :--- | :--- |
| **Name** | Harshita Dhakad |
| **USN** | 2402608020 |
| **Campus / Section** | Newton School of Technology / AI & ML |
| **GitHub Username** | [Harshiita24](https://github.com/Harshiita24) |
| **GitHub Repository Name** | `digital-detective-8020` |
| **GitHub Repository URL** | [https://github.com/Harshiita24/digital-detective-8020](https://github.com/Harshiita24/digital-detective-8020) |

---

## About This Assignment

This assignment is a series of 9 missions to investigate how my computer works under the hood. Instead of just clicking through graphical menus, I used the terminal to inspect system hardware, manage files, monitor running processes, test Python code, convert between number bases, collaborate with Git and GitHub, and see how computers talk over a network.

Every mission was completed individually, verified on my own laptop, and saved with its own dedicated Git commit to show my progress step by step.

---

## My Learning

Working through these missions helped me understand practical concepts that usually feel abstract:
1. **How the Computer Handles Actions (IPOS):** Breaking down code editing showed me how pressing a key travels from the keyboard to the CPU and RAM, displays immediately on the screen, and gets saved permanently to the SSD.
2. **Terminal Navigation:** I got comfortable typing commands like `pwd`, `ls -lah`, `cp`, `mv`, and using pipes (`|`) to view output. It felt faster and more precise than clicking around in a file manager.
3. **Numbers and Text in Memory:** Working through binary and hexadecimal conversions by hand helped me see that computers really only store 0s and 1s, and standards like ASCII and UTF-8 are what let us turn those numbers into readable letters and symbols.

---

## Topics Explored

- **Computer Basics:** The Input-Process-Output-Storage (IPOS) cycle, hardware components, and software categories (system, application, utility).
- **Terminal Practice:** Essential file and folder commands, writing vs appending text (`>` vs `>>`), command flags, pipes (`|`), and package managers (Homebrew).
- **Operating Systems:** System details, checking disk space (`df -h`), running processes and PIDs, relative vs absolute paths, and file permissions (`rwx`).
- **Programs & Execution:** Running a Python program from the terminal and comparing how compilers and interpreters work.
- **Numbers & Data:** Converting between decimal, binary, and hexadecimal by hand and with Python, plus how ASCII and UTF-8 store text.
- **Git & GitHub:** Making commits, working on a separate branch (`update-about`), opening and merging a Pull Request, and pulling updates back to my computer.
- **Computer Networks:** Network types (LAN, MAN, WAN), network concepts (DNS, routers, protocols, packet switching, client-server), running `ping` and `nslookup`, and how websites load.

---

## Mission Index

| Mission | Focus Area | Status | Folder / Report |
| :---: | :--- | :---: | :--- |
| **0** | Repository and workspace setup | Completed | [mission-00-setup/](mission-00-setup/README.md) |
| **1** | Computer fundamentals and IPOS model | Completed | [mission-01-computer-basics/](mission-01-computer-basics/README.md) |
| **2** | Terminal operations, flags, and file management | Completed | [mission-02-terminal/](mission-02-terminal/README.md) |
| **3** | Operating system internals, processes, and permissions | Completed | [mission-03-operating-system/](mission-03-operating-system/README.md) |
| **4** | Program execution, compilers, and interpreters | Completed | [mission-04-programs/](mission-04-programs/README.md) |
| **5** | Number systems, Python verification, and text encoding | Completed | [mission-05-numbers-data/](mission-05-numbers-data/README.md) |
| **6** | Git collaboration, branching, and pull requests | Completed | [mission-06-git-github/](mission-06-git-github/README.md) |
| **7** | Computer networking, DNS lookup, and web communication | Completed | [mission-07-networking/](mission-07-networking/README.md) |
| **8** | Final review, verification, and submission checklist | Completed | [mission-08-final-report/](mission-08-final-report/README.md) |

*(Note: Following the assignment rules, each mission has its own dedicated commit in Git history.)*

---

## How to Run the Number Converter

Inside the `mission-05-numbers-data/` folder, there is a small Python program that takes a decimal number and converts it to binary and hexadecimal.

### Steps to run:
1. Open your terminal and change into the mission 5 folder:
   ```bash
   cd mission-05-numbers-data
   ```
2. Run the script using Python 3:
   ```bash
   python3 number_converter.py
   ```
3. Enter any positive number when prompted (for example: `42`):
   ```text
   --- Number Converter ---
   Enter a positive decimal number: 42
   Decimal:     42
   Binary:      0b101010
   Hexadecimal: 0x2a
   ```

---

## Folder Structure

```text
digital-detective-8020/
├── README.md
├── evidence/
│   └── .gitkeep
├── mission-00-setup/
│   └── README.md
├── mission-01-computer-basics/
│   └── README.md
├── mission-02-terminal/
│   └── README.md
├── mission-03-operating-system/
│   └── README.md
├── mission-04-programs/
│   ├── hello.py
│   └── README.md
├── mission-05-numbers-data/
│   ├── number_converter.py
│   └── README.md
├── mission-06-git-github/
│   └── README.md
├── mission-07-networking/
│   └── README.md
├── mission-08-final-report/
│   └── README.md
└── terminal-practice/
    ├── sample-renamed.txt
    └── sample.txt
```

---

## Tools & Environment

- **Operating System:** macOS (Apple Silicon arm64)
- **Shell:** Zsh (`/bin/zsh`)
- **Python:** Python 3.9.6
- **Git:** git version 2.54.0
- **Package Manager:** Homebrew 7.0.12
- **Editor:** VS Code / Terminal
