# SQA101 - Software Quality Assurance 101

Welcome to the SQA101 repository! This resource is designed for Software Quality Assurance beginners, offering a foundation in testing using pytest and Selenium. Follow the instructions below to get started.

## Clone the Repository

To clone this repository to your local machine, use the following command:

```bash
git clone git@github.com:FESAr-SQA/SQA101.git
```

## Set up a Virtual Environment

It's a good practice to create a virtual environment to manage project-specific dependencies. In the project directory, run the following commands to create and activate a virtual environment:

### For Command Prompt (CMD):

```bash
# Create a virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\activate
```

### For PowerShell:

```bash
# Create a virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1
```

### For Linux/Mac:

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

## Install Dependencies

Ensure you have Python and pip installed on your machine. With the virtual environment activated, navigate to the project directory and install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

This command will install all the necessary dependencies for running test cases, including the pytest and Selenium packages.

## Run Test Cases with pytest

After installing the dependencies, execute the test cases using pytest. In the project directory, run the following command:

```bash
pytest
```

This will automatically discover and run all test cases in the project, leveraging the power of pytest for efficient and effective testing.

Feel free to explore the code and contribute to the SQA101 project. If you encounter any issues or have suggestions, please open an issue on GitHub.

Happy testing! 🚀
