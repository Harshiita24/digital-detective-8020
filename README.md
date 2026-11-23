# The Digital Detective: Explore Your Computer & Build a Mini System Report
**Diwali Independent Learning Assignment**

An investigative, hands-on computer systems study exploring hardware-software interaction, terminal workflows, operating system internals, program execution, number systems, Git version control, and computer networking.

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

## Assignment Overview

This project documents a systematic investigation into the inner workings of personal computers and Unix-like operating systems. Completed as a sequence of nine focused missions, each section explores a core computing concept through direct terminal commands, manual arithmetic, code execution, and system observations.

Every mission has been researched, verified on my own machine, documented with observations, and committed separately to record an authentic progression of learning.

---

## My Learning

Working through these hands-on missions provided several practical insights into computer architecture and everyday developer workflows:
1. **The IPOS Cycle in Action:** Tracing a task like code editing highlighted how input devices, CPU scheduling, GPU rendering, and SSD non-volatile storage pass data back and forth seamlessly.
2. **Terminal Fluency and Precision:** Using command-line tools (`pwd`, `ls -lah`, `cp`, `mv`, and pipes like `| head -n 5`) proved much faster than GUI clicking and revealed how Unix programs chain inputs and outputs together cleanly.
3. **Number Systems and Encoding:** Performing manual binary, decimal, and hexadecimal conversions clarified how computers structure raw memory into 4-bit nibbles and 8-bit bytes, and why standards like UTF-8 are essential for global text representation.

---

## Topics Explored

- **Computer Fundamentals & Architecture:** The Input-Process-Output-Storage (IPOS) model, hardware components (CPU, RAM, SSD, GPU), and software classification (system, application, utility).
- **Terminal & Command-Line Fluency:** Directory navigation, safe file manipulation, output redirection (`>` vs `>>`), flags (`ls -lah`), Unix pipelines (`|`), and package managers (Homebrew).
- **Operating System Internals:** Kernel inspection, user identity, filesystem mounts (`df -h`), process management (PIDs), relative vs absolute paths, and Unix permission triplets (`rwx`).
- **Program Execution:** How source code runs, compiler ahead-of-time (AOT) machine code vs interpreter runtime evaluation, and Python script execution.
- **Data Representation & Text Encoding:** Decimal, binary, and hexadecimal arithmetic conversions, Python verification functions (`bin()`, `hex()`, `int()`), and character encoding standards (ASCII vs UTF-8).
- **Version Control & Collaboration:** Git workflow (`status`, `add`, `commit`, `log`), feature branching, GitHub Pull Requests, and code review lifecycles.
- **Computer Networking:** Network scopes (LAN, MAN, WAN), protocols (TCP/IP, HTTP/HTTPS, DNS), packet switching, client-server architecture, and live network diagnostics (`ping`, `nslookup`).

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

*Note: In accordance with assignment instructions, each mission was completed, documented, and committed separately with a dedicated, descriptive Git commit message.*

---

## Instructions for Running the Number Converter

The repository includes an interactive Python number conversion utility in `mission-05-numbers-data/number_converter.py`.

### How to Run:
1. Open your terminal and navigate into the `mission-05-numbers-data` folder:
   ```bash
   cd mission-05-numbers-data
   ```
2. Execute the script using Python 3:
   ```bash
   python3 number_converter.py
   ```
3. When prompted, enter any positive decimal integer (e.g. `42`):
   ```text
   ==========================================
      Digital Detective: Number Converter    
   ==========================================
   Enter a positive decimal integer: 42

   --- Conversion Results ---
   Decimal (Base 10):     42
   Binary (Base 2):       101010  (Prefix notation: 0b101010)
   Hexadecimal (Base 16): 2A  (Prefix notation: 0x2a)
   ==========================================
   ```

---

## Workspace Structure

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

## Development Environment & Prerequisites

- **Operating System:** macOS (Darwin arm64)
- **Shell:** Zsh (`/bin/zsh`)
- **Python Version:** Python 3.9.6
- **Git Version:** git version 2.54.0 (Apple Git-157)
- **Package Manager:** Homebrew 7.0.12
- **Text Editor:** VS Code / Terminal CLI
