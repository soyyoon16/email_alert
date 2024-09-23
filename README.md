# Problem 3: Mailer Alert System

This project allows you to send email alerts using Python. It includes the `alert.py` script to send emails using the `mailer.py` utility.

## How to Run

Start the SMTP debugging server:
   ```bash
   python -m smtpd -n -c DebuggingServer localhost:1025
   ```

## Process
1. Set Up Project Folder:
- Created a project folder and placed the `alert.py` and `mailer.py` scripts into the module.

2. Initialize Project with Poetry:
- Ran `poetry init` to generate a `pyproject.toml` file.
- Installed necessary dependencies using `poetry install`.

3. Create Git Repository:
- Initialized a Git repository using `git init`.
- Set up a remote repository on GitHub and pushed the initial project structure.

4. Write Documentation:
- Wrote an informative `README.md` file, providing details about the Mailer Alert System and instructions for using the project.

5. Set Up GitHub Actions Workflow:
- Created a workflow file (`mailer-ci.yml`) under `.github/workflows/` to automate testing, building documentation, and deploying the project using CI/CD.

6. Install and Configure Pre-commit Hooks:
- Installed pre-commit using `pip install pre-commit`.
- Set up a `.pre-commit-config.yaml` file and ran `pre-commit install` to enforce code quality checks.

7. Build Sphinx Documentation:
- Ran `sphinx-quickstart` to set up the `docs` folder.
- Configured `conf.py` to enable extensions and set up the theme.
- Built the documentation using `poetry run sphinx-build -b html docs/ docs/_build`.