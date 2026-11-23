# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The goal of Mission 0 is to configure a clean, standardized development workspace for the entire assignment. This includes picking a valid repository name according to the naming formula (`digital-detective-<last-four-digits-of-USN>`), setting up the required directory hierarchy and Markdown templates, checking installed tools (Git and Python 3), and linking the local repository to a public GitHub remote.

## 2. Work completed
- Named the repository `digital-detective-8020` based on the assignment guideline (`digital-detective-` followed by the last four digits of USN `2402608020`).
- Created the project folder on the local machine and initialized Git tracking on the `main` branch.
- Created all required mission folders (`mission-00-setup` through `mission-08-final-report`) and the `evidence/` directory.
- Checked installed toolchain versions in the terminal for Git and Python 3.
- Drafted the root `README.md` containing student identification, assignment description, environment details, and a clickable mission navigation index.
- Created the remote GitHub repository at `https://github.com/Harshiita24/digital-detective-8020` and linked the local origin remote.

## 3. Commands / tools used
- `git init`: Initialized the local repository directory for version tracking.
- `git branch -M main`: Set the default branch name to `main`.
- `git remote add origin https://github.com/Harshiita24/digital-detective-8020.git`: Connected the local repository to GitHub.
- `python3 --version`: Verified the Python 3 interpreter (`Python 3.9.6`).
- `git --version`: Verified the Git command-line client (`git version 2.54.0 (Apple Git-157)`).
- `mkdir -p`: Created all required mission subdirectories cleanly from the command line.

## 4. My understanding
A Git repository serves as a trackable record of a project's evolution over time. Instead of saving multiple messy copies of files with names like "final_v2_really_final", Git captures snapshots of the exact state of files with meaningful messages explaining the reasons behind every change.

Splitting this assignment into numbered mission folders keeps each topic self-contained. When someone inspects the repository, they can examine terminal practice, operating system queries, or networking tests in isolation without wading through a single cluttered folder. This modular organization also makes debugging, grading, and incremental commits straightforward.

## 5. Difficulties faced
I had to make sure the repository name followed the exact naming rule without spaces, capital letters, or underscores so it conforms to standard GitHub URL conventions. Another point of attention was ensuring that creating the remote GitHub repository did not automatically add a default README, `.gitignore`, or license on GitHub before my local structure was pushed, which would have caused merge conflicts on the first push.

## 6. How I resolved them
I followed the assignment naming rule strictly (`digital-detective-8020`). When creating the repository on GitHub, I left it completely empty (without an auto-generated README or license), allowing the initial local commit and branch structure to push cleanly to `origin/main`.

## 7. Evidence / files
- Root documentation: `README.md`
- Mission setup file: `mission-00-setup/README.md`
- Toolchain checks:
  - Python: `Python 3.9.6`
  - Git: `git version 2.54.0 (Apple Git-157)`
- Created mission directories:
  - `mission-00-setup/`
  - `mission-01-computer-basics/`
  - `mission-02-terminal/`
  - `mission-03-operating-system/`
  - `mission-04-programs/`
  - `mission-05-numbers-data/`
  - `mission-06-git-github/`
  - `mission-07-networking/`
  - `mission-08-final-report/`
  - `evidence/`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Target branch:** `main`
- **Remote destination:** `https://github.com/Harshiita24/digital-detective-8020`
