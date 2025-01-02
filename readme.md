# Python & Django Setup Guide

This guide walks through setting up Python, installing Django, and working with some basic and advanced concepts, including using `pyenv` for Python version management and `pip` for managing Python packages.

---
 [Prerequisites](#prerequisites)
## Table of Contents


1. [Install Python](#1-install-python)
   - [Download Python](#11-download-python)
   - [Install Python](#12-install-python)
   - [Verify Installation](#13-verify-installation)
   - [Basic python Examples](#14-basic-python-examples)

2. [Install Virtual Environment](#2-install-virtual-environment)
   - [Managing Python Versions with `pyenv`](#21-managing-python-versions-with-pyenv)
   - [Using `pip` to Install Packages](#22-using-pip-to-install-packages)
3. [Advanced Python Examples](#3-advanced-python-examples)
   - [Installing Packages with `pip`](#31-installing-packages-with-pip)
   - [Making HTTP Requests with `requests`](#32-making-http-requests-with-requests)
   - [Reading and Writing JSON Data](#33-reading-and-writing-json-data)
4. [Create a Django Project](#4-create-a-django-project)
   - [Create a Django Project](#41-create-a-django-project)
   - [Run the Development Server](#42-run-the-development-server)


---

## Prerequisites

Before we begin, ensure you have the following:

- A working *Python* installation (Python 3.7 or higher recommended).
- A *code editor* like Visual Studio Code (VSCode), PyCharm, or Sublime Text.
- *Command-line access* (Terminal on macOS/Linux, Command Prompt/PowerShell on Windows).

---


## 1. Install Python

### 1.1. Download Python

Visit the official Python website:

- https://www.python.org/downloads/

Choose the latest stable version and download the appropriate installer for your system (Windows, macOS, or Linux).

### 1.2. Install Python

**Windows**:  
- Run the installer and ensure you check the box *"Add Python to PATH"*.  
- Follow the installation prompts.

**macOS**:  
- Open the downloaded `.pkg` file and follow the instructions to install Python.

**Linux (Ubuntu Example)**:  
- Open a terminal and install Python by using your package manager.

### 1.3. Verify Installation

After installing, open a terminal or command prompt and check your Python version by running:

```bash
python --version
```
 
or  

```bash 
python3 --version  
```
This should print the version of Python installed, e.g., `Python 3.10.x`.

---
### 1.4 Basic Python Examples

### 1.4.1 Hello World


```bash 
print("Hello, World!")
```
### 1.4.2 Working with Variables

```bash 
name = "Alice"
age = 25

print(f"Name: {name}, Age: {age}")
```

### 1.4.3. Conditional Statements

```bash
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### 1.4.5. Loops

```bash
for i in range(5):
    print(i)

```

# 2. Install Virtual Environment

It's good practice to work within a *virtual environment* to manage project dependencies.

### 2.1. Create a Virtual Environment

1. Navigate to your project folder.
2. Create the virtual environment.
3. Activate the virtual environment:
   - For *Windows*, follow the appropriate steps for your terminal.
   - For *macOS/Linux*, follow the appropriate steps for your terminal.



### 2.2 Using `pip` to Install Packages

`pip` is the package installer for Python, and it allows you to install Python packages from the Python Package Index (PyPI). You can install libraries such as Django, `requests`, and many others. Here's a quick overview of how to use `pip`:

1. **Install a package using `pip`**:

   To install a package, use the following command:
   
   `pip install <package-name>`

   Example to install Django:

   `pip install django`

2. **List installed packages**:

   To see all the installed packages and their versions, run:

   `pip list`

3. **Uninstall a package**:

   If you no longer need a package, you can uninstall it with:

   `pip uninstall <package-name>`

4. **Freeze installed packages to a requirements file**:

   It’s common practice to create a `requirements.txt` file to track the exact versions of packages your project depends on. To generate this file:

   `pip freeze > requirements.txt`

   To install packages from the `requirements.txt` file:

   `pip install -r requirements.txt`

---



# 3.1. Managing Python Versions with `pyenv`

`pyenv` is a tool used to manage multiple versions of Python on your system. It allows you to easily switch between different versions of Python for different projects. Here’s a quick guide to using `pyenv`:

1. **Install `pyenv`**:
   - On *macOS* or *Linux*, you can install `pyenv` using `Homebrew` (macOS) or by following the installation instructions on https://github.com/pyenv/pyenv.
   - On *Windows*, you can use https://github.com/pyenv-win/pyenv-win.

2. **Install a new version of Python**:
   - After installing `pyenv`, use the following command to install a specific version of Python, for example, Python 3.10.5:
   
     `pyenv install 3.10.5`

3. **Set a global Python version**:
   - To set the default Python version across your system, use the following:
   
     `pyenv global 3.10.5`

4. **Switch Python versions**:
   - To switch Python versions for a specific project, you can set the local Python version by running:
   
     `pyenv local 3.9.7`

5. **Verify the current Python version**:
   - You can verify the active Python version with the following:
   
     `pyenv version`

---


# Advanced Python Examples

### 3.1. Installing Packages with `pip`

You can use `pip` (Python’s package installer) to install additional Python packages. For example, to install the `requests` package, you would simply use `pip install requests`.

### 3.2. Making HTTP Requests with `requests`

The `requests` library allows you to send HTTP requests easily. Here's an example:

python
import requests

response = requests.get('https://example.com')
print(response.status_code)

### 3.3. Reading and Writing JSON Data
The json module is useful for working with JSON data. Here’s an example of reading and writing JSON data:

bash import json

# Writing JSON data
data = {"name": "Alice", "age": 25}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Reading JSON data
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)




## 3. Advanced Python Examples

### 3.1. Installing Packages with `pip`

You can use `pip` (Python’s package installer) to install additional Python packages. For example, to install the `requests` package, you would simply use `pip install requests`.

### 3.2. Making HTTP Requests with `requests`

The `requests` library allows you to send HTTP requests easily. Here's an example:

```python
import requests

response = requests.get('https://example.com')
print(response.status_code)
```


3.3. Reading and Writing JSON Data
The json module is useful for working with JSON data. Here’s an example of reading and writing JSON data:

```bash
import json

# Writing JSON data
data = {"name": "Alice", "age": 23}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Reading JSON data
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)
```


# 4. Create a Django Project

## 4.1. Create a Django Project
To start a new Django project, use the Django CLI to create a project. This will create a directory called mysite with the necessary Django project structure.

## 4.2. Run the Development Server
Navigate into the project directory and run the server:

Start the server with Django's built-in development server.
Visit http://127.0.0.1:8000 in your browser to see your Django site in action!


Navigate into the project directory and run the server:

Start the server with Django's built-in development server.
Visit http://127.0.0.1:8000 in your browser to see your Django site in action!