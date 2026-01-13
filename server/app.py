#!/usr/bin/env python3
"""
Flask Application for Python Operations with Routing and Views

This application demonstrates basic Flask routing and view functionality
including string manipulation, counting, and mathematical operations.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    Index route that displays the application title.
    
    Returns:
        str: HTML string containing the application title in an h1 tag
    """
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    """
    Print route that displays and prints a string.
    
    Args:
        string (str): The string to print and display
        
    Returns:
        str: The input string for browser display
    """
    print(string)
    return string

@app.route('/count/<int:num>')
def count(num):
    """
    Count route that displays numbers from 0 to num-1 on separate lines.
    
    Args:
        num (int): The upper bound for counting (exclusive)
        
    Returns:
        str: Numbers from 0 to num-1 separated by newlines
    """
    return '\n'.join(str(i) for i in range(num)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    """
    Math route that performs mathematical operations on two numbers.
    
    Args:
        num1 (int): First number
        operation (str): Mathematical operation to perform
        num2 (int): Second number
        
    Returns:
        str: String representation of the calculation result
    """
    # Use dictionary for operations but maintain exact same behavior
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        'div': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    
    if operation in operations:
        result = operations[operation](num1, num2)
        return str(result)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)