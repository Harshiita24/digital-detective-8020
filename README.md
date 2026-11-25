# The Digital Detective
**Diwali Independent Learning Assignment**

My notes and practice from nine missions covering computer basics, the terminal, Python, Git, and networking.

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

I explored my laptop through nine missions: checking hardware, managing files, running Python, converting numbers, using Git, and testing network commands. Each mission has its own report and Git commit.

---

## My Learning

1. **Computer basics:** Typing and saving code connects the keyboard, CPU, RAM, screen, and SSD.
2. **Terminal:** I practiced commands such as `pwd`, `ls -lah`, `cp`, and `mv`, plus pipes (`|`).
3. **Data:** Binary and hex conversions helped me understand how numbers are stored. ASCII and UTF-8 explain how numbers represent text.

---

## Topics Explored

- **Computer basics:** IPOS, hardware, and types of software.
- **Terminal:** Files, flags, `>` vs `>>`, pipes, and Homebrew.
- **Operating systems:** System details, disk space, processes, PIDs, paths, and `rwx` permissions.
- **Programs:** Running Python and comparing compilers with interpreters.
- **Data:** Decimal, binary, hex, ASCII, and UTF-8.
- **Git:** Commits, the `update-about` branch, pull requests, merging, and pulling.
- **Networks:** LAN, MAN, WAN, DNS, routers, protocols, packets, client-server, `ping`, and `nslookup`.

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

Each mission folder has a `README.md` with its report. Here is where everything lives:

```text
digital-detective-8020/
├── README.md                     # Start here
├── evidence/                     # Evidence folder (.gitkeep)
├── mission-00-setup/              # Project setup
├── mission-01-computer-basics/    # Hardware, software, and IPOS
├── mission-02-terminal/           # Terminal practice
├── mission-03-operating-system/   # Processes, paths, and permissions
├── mission-04-programs/           # Program notes and hello.py
├── mission-05-numbers-data/       # Number notes and number_converter.py
├── mission-06-git-github/         # Git workflow and glossary
├── mission-07-networking/         # Network notes and command results
├── mission-08-final-report/       # Final review and checklist
└── terminal-practice/             # sample.txt and sample-renamed.txt
```

---

## Tools & Environment

- **Operating System:** macOS (Apple Silicon arm64)
- **Shell:** Zsh (`/bin/zsh`)
- **Python:** Python 3.9.6
- **Git:** git version 2.54.0
- **Package Manager:** Homebrew 7.0.12
- **Editor:** VS Code / Terminal
