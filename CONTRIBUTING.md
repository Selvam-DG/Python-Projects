# Contributing to Python Projects

Thank you for your interest in contributing!!

This repository is a collection of Python projects for **beginners to advanced developers**.

We welcome 
- new projects
- Enhancements to exisiting ones
- Bug fixes
- Improvements to documentation.

## How to Contribute

### 1. Fork the Repository

 Click the **"Fork"** button at the top-right of the page to create your own copy of the repo.

### 2. Clone your fork

``` bash 
git clone https://github.com/your_username/python-projects.git
cd python-projects
```

### 3. Create a Branch

```bash
git checkout -b feature/project-name

```

### 4. Add Your Project
- create a new **folder** in the root directory with the project name

```bash
mkdir project-name
cd project-name
```
- Add your `.py` files and a `README.md` in that folder.
- Name your Project folder using `kebab-case`(eg., `todo-list-cli`)

### 5. Update the Root `README.md`
- Add your project to the main `README.md` under the appropriate section.
    - Beginner Project
    - Intermediate Project
    - Advanced Project
- Use the table format to link your project folder and includes a short description

``` markdown
| [todo-list-cli](./todo-list-cli) | A CLI app to manage your to-do list |
```

### 6. Commit and Push

```bash 
git add .
git commit -m "Add project: your-project-name"
git push origin feature/project-name
```

### 7. Open a Pull Request (PR)
- Go to your forked repo on GitHub
- Click “Compare & pull request”
- Fill out the pull request template (if available)
- Make sure your description explains the project and any setup instructions
- Submit the pull request

## Contribution Checklist
Before submitting Your PR, make sure:
- [ ]Your project is inside a new folder at the root level.
- [ ] You have added a `README.md` inside your project folder with:
    - What the project does
    - How to run it
    - Any dependencies or setup instructions
- [ ] Your code follows Python style and is clean and readable
- [ ] You have updated the main `README.md` with your project link
- [ ] Your code runs without errors

## Project Folder Structure Example
```css
python-projects/
├── todo-list-cli/
│   ├── main.py
│   └── README.md
├── README.md
└── CONTRIBUTING.md

```
## Code Style Guidelines
- Use snake_case for variable and function names
- Keep code modular (avoid one huge file if possible)
- Add comments where necessary for readability
- Avoid unnecessary complexity

## Need Help?
- If you face any issues, feel free to:
    - Open an issue
    - Start a GitHub discussion


## 🙌 Final Note
**We welcome developers of all skill levels. Your contributions matter!**

Let’s make this repository a great place to learn and grow together.