# Mission 1 — Know your computer

## 1. Task / objective
The goal of Mission 1 is to examine how hardware and software work together to form a functioning computer system. This involves breaking down an everyday computing task through the Input-Process-Output-Storage (IPOS) model, categorizing hardware and different tiers of software (system, application, and utility), and analyzing computer-controlled systems used in public everyday environments.

## 2. Work completed
- Selected and traced an everyday computing workflow (*writing a Python script in a text editor and saving it*) across all four IPOS stages.
- Created a hardware and software classification table listing five hardware components and five software programs with their software types and purposes.
- Identified and analyzed three standalone computer systems encountered in daily life (Metro Ticket Vending Machine, ATM, and Smart Traffic Light Controller), detailing their main purposes, physical inputs, and physical outputs.

---

### Task 1.1 — Trace one activity using IPOS
**Activity:** Writing a Python script in VS Code and saving it to disk.

| Stage | What happens in this activity | Hardware / component involved |
| :--- | :--- | :--- |
| **Input** | I type lines of Python code on the keyboard. Each keypress generates an electrical interrupt that the keyboard controller sends to the operating system as keycodes. | Built-in laptop keyboard / USB keyboard |
| **Processing** | The CPU accepts the keyboard interrupts, translates keycodes into text characters using character encoding tables, and stores the edited text buffer in active RAM. The editor checks syntax on the fly. | CPU (Apple Silicon) and System RAM |
| **Output** | The graphics chip renders the text characters into visual font pixels and displays them instantly in the editor window on the screen so I can read what I am typing. | Liquid Retina Display / GPU |
| **Storage** | When I press `Cmd + S` (Save), the operating system takes the current text buffer from RAM and writes the file bytes into a persistent folder on the solid-state drive so it remains safe after closing the app or turning off the machine. | Internal NVMe SSD |

#### How the activity moves through the stages:
The workflow starts the moment physical energy is applied to the keyboard keys (Input). The CPU captures these raw signals, coordinates with the OS to translate them into characters, and keeps the current state in temporary system memory (Processing). While this happens in fractions of a millisecond, the GPU draws each character to the monitor so I get immediate feedback on what was typed (Output). Finally, when I instruct the computer to save, the data transitions from volatile RAM to non-volatile flash memory on the SSD (Storage), ensuring my work is not lost when power is turned off.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| Built-in keyboard | Hardware | Not applicable | Captures physical key presses to input text, commands, and shortcuts into the computer. |
| Retina Display | Hardware | Not applicable | Presents the visual graphical interface, terminal windows, text, and browser pages to the user. |
| Trackpad | Hardware | Not applicable | Detects fingertip movement and taps to navigate the cursor and trigger system gestures. |
| Apple M-Series RAM | Hardware | Not applicable | Provides high-speed, volatile temporary workspace for active running applications and operating system data. |
| Internal NVMe SSD | Hardware | Not applicable | Stores the operating system files, user documents, and installed programs permanently. |
| macOS | Software | Operating system software | Manages system hardware, schedules CPU tasks, handles memory, and provides access controls and file systems. |
| Visual Studio Code | Software | Application software | Provides an environment for creating, editing, and managing code files and scripts. |
| Google Chrome | Software | Application software | Loads web pages, runs web applications, and handles web lookups and documentation. |
| Terminal | Software | Utility software | Gives direct text-based command-line access to run commands, scripts, and file management tools. |
| Activity Monitor | Software | Utility software | Displays live CPU, memory, disk, and network resource consumption across running processes to help troubleshoot slow tasks. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Authenticates bank customers and dispenses cash securely from their accounts. | Numeric PIN keypad or debit card chip reader. | Mechanical cash dispenser slot or printed paper transaction receipt. |
| **Metro Ticket Vending Machine (TVM)** | Allows passengers to select transit destinations and purchase journey tokens or recharge smart cards. | Touchscreen destination button or UPI QR code scanner. | Dispensed RFID travel token / printed QR slip and fare display screen. |
| **Intelligent Traffic Signal** | Coordinates vehicular traffic flow at a road intersection using timers and sensor loops. | Inductive metal loop detector embedded under the road asphalt (detects vehicle presence). | Colored red, amber, and green LED light panels facing the road lanes. |

---

## 3. Commands / tools used
- Text editor (VS Code) to draft tables and notes.
- Terminal commands (`sw_vers`, `uname -mprsv`) to verify local hardware architecture while documenting hardware components.

## 4. My understanding
A computer is not just a single smart box; it is an integrated chain of hardware modules directed by software. The IPOS model helped me see how everyday actions follow a strict cycle: without input there is nothing to compute, without processing input remains raw electrical noise, without output a user has no way to confirm what the computer did, and without storage all results vanish the second power drops.

I also learned how software falls into different levels: the operating system acts as the underlying foundation controlling access to hardware, applications allow users to do productive work like browsing or coding, and utilities keep the system healthy, monitored, and organized.

## 5. Difficulties faced
When looking at everyday systems like traffic lights or ticket dispensers, it is easy to forget they are full computers with microcontrollers, memory, inputs, and outputs rather than simple mechanical switches.

## 6. How I resolved them
I broke each everyday machine down by asking: "Where does it get information?" (sensors, keypads), "Where does it make decisions?" (embedded processor/controller), and "What physical action or display results?" (LEDs, motors, screens).

## 7. Evidence / files
- `mission-01-computer-basics/README.md`: Completed IPOS, hardware/software, and everyday computer system tables.

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Target branch:** `main`
- **Remote destination:** `https://github.com/Harshiita24/digital-detective-8020`
