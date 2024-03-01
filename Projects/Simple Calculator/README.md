# Calculator

A simple calculator program written in Python.

## Introduction

This Python program provides a basic calculator functionality, allowing users to perform arithmetic calculations using the command line interface.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Support for parentheses
- Error handling for invalid expressions

## Example

```bash
$ python calculator.py
Your calculation: 2 + 3 * 4
14
Your calculation: (10 - 3) / 2
3.5
Your calculation: exit
```

## How it works

1. **Input**: The program prompts the user to enter a mathematical expression.

2. **Evaluation**: The entered expression is passed to the `eval()` function, which evaluates the expression as a Python expression and returns the result. For example, if the user enters `2 + 3 * 4`, the `eval()` function evaluates it as `2 + (3 * 4)` and returns `14`.

3. **Display Result**: The calculated result is printed to the console.

4. **Loop**: The program continues to prompt the user for input and evaluate expressions in a loop until the user decides to exit.

5. **Error Handling**: If the user enters an invalid expression, such as a non-mathematical string or a syntax error, the program catches the exception and displays an error message, prompting the user to enter a valid expression.

6. **Exit**: The user can exit the program by typing `exit`.

Overall, the program provides a simple command-line interface for performing basic arithmetic calculations. It supports various arithmetic operations, including addition, subtraction, multiplication, and division, as well as parentheses for grouping expressions.