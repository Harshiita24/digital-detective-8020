# Mission 6 — Git and GitHub

## 1. Task / objective
The goal of Mission 6 is to understand the Git version control lifecycle and collaborative GitHub workflows. This includes mastering the core local workflow (`status`, `add`, `commit`, `log`), creating and publishing an isolated feature branch (`update-about`), opening a formal Pull Request on GitHub into `main`, reviewing and merging the PR, pulling the updated history back to the local repository, and writing an original glossary of fundamental Git commands.

## 2. Work completed
- Inspected repository status and analyzed the practical distinction between the working tree, the staging area (index), and committed history.
- Created and switched to a new branch named `update-about`.
- Updated root `README.md` on the feature branch with a reflective "My Learning" section summarizing core insights from earlier missions.
- Staged and committed the update with the message `"Add My Learning section to root README"`, and pushed `update-about` to GitHub.
- Opened Pull Request #1 on GitHub from `update-about` into `main`, reviewed the file diff, and merged it into `main`.
- Switched back to the local `main` branch and pulled remote merge commits using `git pull origin main`.
- Authored a comprehensive Git command glossary explaining nine foundational operations in plain language.

---

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** (`git status`) | Shows which branch you are on, highlights which files have been modified or staged, and flags untracked files that Git is not yet recording. |
| **Stage selected changes** (`git add <file>`) | Moves specified file modifications into the staging index, essentially queuing them up to be included in the next commit snapshot. |
| **Create a commit** (`git commit -m "<msg>"`) | Records a permanent, cryptographically hashed snapshot of all currently staged changes with a descriptive message explaining the change. |
| **View commit history** (`git log`) | Lists the sequential ledger of previous commits, showing author identity, timestamps, commit hashes, and commit descriptions. |

#### Difference between staging a change and committing it:
Staging (`git add`) is like packing items into a box before shipping; you get to decide exactly which files belong together in a logical group, and you can still unpack or modify them before sealing the package. Committing (`git commit`) is officially sealing the box, stamping it with an unalterable tracking barcode and timestamp, and placing it permanently onto the project's historical timeline.

---

### Task 6.2 — Create and use a branch
1. Created and checked out a dedicated feature branch:
   ```bash
   git checkout -b update-about
   ```
2. Edited root `README.md` to insert the "My Learning" section highlighting three takeaways:
   - IPOS cycle orchestration across hardware components.
   - Speed and precision of command-line tools and pipelines over GUIs.
   - Binary data representation and character encodings.
3. Inspected status, staged, committed, and published the branch:
   ```bash
   git status
   git add README.md
   git commit -m "Add My Learning section to root README"
   git push -u origin update-about
   ```

---

### Task 6.3 — Create and merge a Pull Request
1. Opened the repository on GitHub (`https://github.com/Harshiita24/digital-detective-8020`).
2. Compared `update-about` against base branch `main`.
3. Created **Pull Request #1**:
   - **PR URL:** `https://github.com/Harshiita24/digital-detective-8020/pull/1`
   - **Title:** `Add My Learning section to root README`
   - **Description:** Documented key reflections from Missions 0 through 5.
4. Reviewed the diff on GitHub to confirm only the intended 9 lines were added.
5. Successfully completed the merge on GitHub into `main` (Merge commit `9817ea0`).
6. Returned to the local terminal, checked out `main`, and pulled the latest merged commits:
   ```bash
   git checkout main
   git pull origin main
   ```

#### Why branches and Pull Requests are essential for teamwork:
A **branch** provides an isolated sandbox where an individual engineer can write, test, and break code freely without risking the stability of the shared `main` codebase.

A **Pull Request (PR)** provides a formal review arena. Instead of developers silently overwriting each other's code on a shared branch, a PR allows peers to inspect the exact line-by-line diff, run automated test suites, discuss architecture or edge cases, and ensure code quality standards before changes are officially merged into production.

---

### Task 6.4 — Build your Git command glossary

| Operation | Command example | One-line explanation in your own words |
| :--- | :--- | :--- |
| **Initialise a repository** | `git init` | Sets up a brand new, empty Git tracking system inside the current folder by generating the hidden `.git` directory. |
| **Check status** | `git status` | Gives an instant snapshot of your current branch, staged files, unstaged modifications, and untracked items. |
| **Stage changes** | `git add <file>` | Queues up specific edited files into the staging index so they will be included in the next commit. |
| **Commit changes** | `git commit -m "msg"` | Permanently records all staged files as a timestamped snapshot in the project's historical ledger. |
| **View history** | `git log --oneline` | Displays a readable chronological list of all recorded commits, their unique hash identifiers, and descriptions. |
| **Create or list branches** | `git branch` / `git branch <name>` | Lists all local branches in the repository, or creates a new parallel branch line without switching to it. |
| **Switch branches** | `git checkout <name>` / `git switch <name>` | Moves your working directory and active pointer to a different branch to work on another line of changes. |
| **Publish changes** | `git push <remote> <branch>` | Uploads local commits across the network to synchronize them with a remote hosting platform like GitHub. |
| **Retrieve remote changes** | `git pull <remote> <branch>` | Downloads new commits from the remote repository and immediately merges them into your active local branch. |

---

## 3. Commands / tools used
- `git status`: Inspected repository state at each workflow checkpoint.
- `git checkout -b update-about`: Created and switched to the feature branch.
- `git add README.md`: Staged documentation updates.
- `git commit -m "..."`: Recorded meaningful atomic commit messages.
- `git push -u origin update-about`: Published feature branch to GitHub.
- GitHub Pull Request API / Web UI: Opened, reviewed, and merged PR #1 into `main`.
- `git checkout main` and `git pull origin main`: Synchronized local `main` with remote merge commits.
- `git log --graph --oneline`: Visualized the branch divergence and merge commit graph.

## 4. My understanding
Version control is not just about backing up files; it is about communication and coordination. Committing frequently with clear, descriptive messages creates an explainable audit trail of how software evolves. Learning to branch and open pull requests showed me how real engineering teams work concurrently without trampling on each other's code.

## 5. Difficulties faced
Remembering to switch back to `main` and execute `git pull` after merging a PR on GitHub is a step that can easily be skipped. If you continue making new commits locally on `main` without pulling first, your local and remote branches will diverge, forcing you to resolve an unnecessary merge conflict later.

## 6. How I resolved them
Right after completing the merge on GitHub, I executed `git checkout main` followed immediately by `git pull origin main` in my terminal, confirming that local `main` fast-forwarded to match remote `origin/main` before starting any new work.

## 7. Evidence / files
- Feature branch: `update-about` (visible on GitHub)
- Pull Request: `https://github.com/Harshiita24/digital-detective-8020/pull/1` (Merged status)
- Merge commit: `9817ea0`
- `mission-06-git-github/README.md`: Complete workflow tables, PR documentation, and Git glossary.

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Target branch:** `main`
- **Remote destination:** `https://github.com/Harshiita24/digital-detective-8020`
