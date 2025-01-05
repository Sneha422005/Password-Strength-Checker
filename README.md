# Password Strength Checker

This is a Flask-based web application that checks the strength of a password.  
It evaluates whether the password is **Weak**, **Moderate**, or **Strong** based on criteria such as length, inclusion of digits, uppercase letters, and special characters.  

---

## Features
- **Frontend**: A simple form to input a password and get its strength.
- **Backend**: A Flask API that evaluates password strength based on defined criteria.
- **Interactive UI**: Displays the strength of the entered password dynamically.

---

## Project Structure

Bone-Age  
|── app.py     
├── templates ---index.html      
|── README.md    


## Prerequisites

- Python 3.7+
- Flask



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
2.Set up a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate    
  venv\Scripts\activate
```
3.Install required dependencies:
  ```bash
  pip install flask

  ```
### Usage

1.Start the Flask server:
  ```bash
  python app.py
   ```
2.Open a web browser and navigate to :
  ```bash
  http://127.0.0.1:5000/

  ```
3.Enter a password in the form and view the evaluated password strength.
