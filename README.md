# Requirements
- Python 3.6 or higher (https://www.python.org/downloads/)
    - Check with `python --version`
    - If you do not have python, you can install it from the link above.
- pip
    - Pip *should* already be installed with python but it can be weird depending on your setup.
    - Check with `pip --version`
    - If you do not have pip, you can install it with `python -m ensurepip --upgrade`
- git (https://git-scm.com/downloads)
# Installation
1. Clone the repository

`$ git clone https://github.com/GregShiner/matrix_calc.git`

`$ cd matrix_calc`

2. Virtual Environment (Optional)
It is recommended to use a virtual environment to install the dependencies. 
This will ensure that the dependencies do not conflict with other projects you may have.
If you do not have virtualenv installed, you can install it with pip:
## Linux/Unix/MacOS
`pip install virtualenv`

`python -m venv .`

`source bin/activate`
## Windows (Command Prompt)
`pip install virtualenv`

`python -m venv .`

`.\Scripts\activate`
## Windows (PowerShell)
`pip install virtualenv`

`python -m venv .`

`.\Scripts\Activate.ps1`

If you are using a virtual environment, you must run the command `source bin/activate` to activate the virtual environment before running the program.
You can run `deactivate` to deactivate the virtual environment.

3. Install the dependencies

`pip install -r requirements.txt`

4. Run the program

`python matrix_calc.py`