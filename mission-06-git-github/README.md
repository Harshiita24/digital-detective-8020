# Mission 6 — Git and GitHub

## 1. Task / objective
Practice Git commands, create the `update-about` branch, update the README, merge a pull request, and pull the changes locally. Write a short Git glossary.

## 2. Work completed
- Checked repository status and learned what staging (`git add`) and committing (`git commit`) actually do.
- Made a new branch called `update-about` and switched to it.
- Added a short "My Learning" section to the main `README.md` file describing things I learned in the earlier missions.
- Committed the change and pushed the `update-about` branch to GitHub.
- Created Pull Request #1 on GitHub, checked the changed lines, and merged the PR into `main`.
- Switched back to `main` locally and pulled the merged changes with `git pull origin main`.
- Wrote a 9-command Git glossary explaining each operation in plain words.

---

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** (`git status`) | Shows which branch you are on, which files you have changed, and which ones are ready to be committed. |
| **Stage selected changes** (`git add <file>`) | Selects specific files and gets them ready to be saved in the next commit snapshot. |
| **Create a commit** (`git commit -m "<msg>"`) | Saves a permanent checkpoint of all your staged changes with a short message explaining what you did. |
| **View commit history** (`git log`) | Shows the list of past commits, who made them, when they were made, and their commit messages. |

#### Difference between staging a change and committing it:
Staging (`git add`) selects changes for the next commit. Committing (`git commit`) saves those staged changes as a snapshot with a message and an ID.

---

### Task 6.2 — Create and use a branch
1. Created the new branch in terminal:
   ```bash
   git checkout -b update-about
   ```
2. Added the "My Learning" section to `README.md` reflecting on what I learned so far.
3. Staged, committed, and pushed the branch to GitHub:
   ```bash
   git add README.md
   git commit -m "Add My Learning section to root README"
   git push -u origin update-about
   ```

---

### Task 6.3 — Create a Pull Request
1. Opened my repository on GitHub (`https://github.com/Harshiita24/digital-detective-8020`).
2. Compared `update-about` with `main`.
3. Created **Pull Request #1**:
   - Title: `Add My Learning section to root README`
   - Description: Added a section reflecting on computer basics, terminal operations, and data representation.
4. Reviewed the diff to make sure only the intended lines were added.
5. Merged the Pull Request into `main` on GitHub.
6. Returned to my terminal, switched back to `main`, and pulled the update:
   ```bash
   git checkout main
   git pull origin main
   ```

#### Why branches and Pull Requests are useful:
A **branch** lets me work on changes separately before merging them into `main`.

A **Pull Request (PR)** lets others review, discuss, and test changes before they are merged.

---

### Task 6.4 — Build your Git command glossary

| Git operation | Command | One-line explanation in your own words |
| :--- | :--- | :--- |
| **Initialise a repository** | `git init` | Turns the current folder into a Git repository so it can start tracking your file changes. |
| **Check status** | `git status` | Shows which files are modified, staged, or untracked in your folder right now. |
| **Stage changes** | `git add <file>` | Adds a file to the staging area so it gets included in your next commit. |
| **Commit changes** | `git commit -m "message"` | Saves a permanent snapshot of your staged files with a description of what changed. |
| **View history** | `git log --oneline` | Displays a neat list of past commits and their messages in order. |
| **Create or list branches** | `git branch` | Lists all the branches in your project or creates a new one. |
| **Switch branches** | `git checkout <name>` | Switches your working files to a different branch. |
| **Publish changes** | `git push origin <branch>` | Uploads your local commits from your computer up to GitHub. |
| **Retrieve remote changes** | `git pull origin <branch>` | Downloads the latest commits from GitHub and merges them into your local branch. |

---

## 3. Commands / tools used
- `git status`, `git add`, `git commit`, `git log`: Core local workflow.
- `git checkout -b update-about`: Created the feature branch.
- `git push -u origin update-about`: Pushed the branch to GitHub.
- GitHub web interface & API: Opened, reviewed, and merged PR #1.
- `git checkout main` and `git pull origin main`: Pulled the merged changes back down to my laptop.

## 4. My understanding
Git tracks changes on my computer. GitHub hosts the repository online. Branches let me work separately, and pull requests let people review changes before merging them.

## 5. Difficulties faced
It was easy to forget to pull the changes after merging the PR on GitHub.

## 6. How I resolved them
I switched to `main` and ran `git pull origin main` after the merge.

## 7. Evidence / files
- Feature branch: `update-about`
- Merged Pull Request: `https://github.com/Harshiita24/digital-detective-8020/pull/1`
- `mission-06-git-github/README.md`: Notes, workflow explanation, and glossary.

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Branch: `main`
- Remote URL: `https://github.com/Harshiita24/digital-detective-8020`
