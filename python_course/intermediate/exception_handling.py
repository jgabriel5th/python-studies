'''
Exception Handling: it's when the code is written right, but the user finds a way to break it.
As my professor says: "Don't trust the users, they'll always find a way to break the code."
Error: programming error is mainly known as bugs and the process to remove bugs from the program is called debugging.

Types of Errors:
Syntax Errors - Error in the source code of a program, any aspects of the code that do not conform to the syntax of the
chosen programming language will generate a syntax error. Also called compilation errors.
Logic Errors - They usually occur due to improper logic used in the program. They are difficult to debug.
Runtime Errors - Syntax and Logic are right, but for example: dividing any number by zero will result in a runtime error.

Exceptions:
Runtime Errors are called Exception, because the Syntax and Logic are right, but something or someone can cause an Exception.
Python provides ways for the developer to handle these Exceptions in order to avoid the program to crash.
This concept of handling Runtime Errors is named Exception Handling.

Examples of Exceptions:
- Division by Zero
- Value Error
- Addition of two incompatible types
- Accessing a nonexistent index of a sequence
- Opening a file that doesn't exist.

Benefits of Exception Handling:
- It makes your code more prepared for Exceptions.
- Therefore, it avoids the code to be broken.

Exception Class:
- It's the base class from which exceptions inherit.
- All the common built-in exceptions inherit from this class.

Common Exceptions:
StandardError - Base class for all built-in exception except StopIteration and SystemExit.
ArithmeticError - Numeric calculation errors.
FloatingPointError - When a floating-point calculation fails.
ZeroDivisionError - Division or modulo by zero happens.
EOFError - When there is no input from the the input() function and the end of the file is reached.
ImportError - When an import statement fails.
KeyboardInterrupt - When the user interrupts program execution, example: by pressing Ctrl+c.
IndexError - When an index is not found in a sequence.
NameError - When an identifier is not found in the local or global namespace.
IOError - When an input/output operation fails, for example print statement or open() when trying to open a file that doesn't exist.
SyntaxError - Error in Python syntax.
IndentationError - Error when indentation is not specified properly.
TypeError - When an operation or function is used with an invalid data type, a data that was not specified.
ValueError - When the built-in function's arguments have invalid values specified.

Try-Except and Finally: statements used to handle Exceptions in Python.
Try - If a particular operation can raise an exception, it must be put inside the try clause.
Except - If the exception is raised, it'll be passed to the except statement, the developer will put a code to inside it to handle the exception.
Finally(optional) - In some cases, a code must be executed rather the Exception was raised or not, then there is finally statement.

Observations:
- If, nothing happens inside the try statement, the code will be executed normally.
- A single try can have multiple except blocks.
- A generic expect clause can be used to handle any exception. It is used the Exception class.
- After the except clause, it is possible to include an else-clause, it'll be executed if try doesn't raise any exception.

Try-Except(finally) Syntax
try:
    # Code that can raise the error
except Exception1:
    # If Exception1 happens, execute this block of code
except Exception2:
    # If Exception2 happens, execute this other block of code
finally:
    # A block of code that'll be executed even if an Exception raise or not.
'''

# Testing Try-Except:
try:
    print(name) # NameError
except Exception: # Using generic Exception class(pretending that I don't know what error will be raised)
    print("An error has occurred. Please contact the developer.")

# Putting more details
try:
    print(name)
except NameError as e:
    print(f"An error has occurred, please contact the developer. Error: {e}")

# Now trying a clean code
name2 = "Botafogo"
try:
    print(name2)
except NameError as e:
    print(f'Some error occurred. Please contact the developer: {e}') 

# Testing with Division:
try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print(f'Division is: {num1 / num2}') # Whenever an exception is raised, the statements after it are skipped.
except ZeroDivisionError:
    print('Sorry, but you cannot divide a number by zero')
except KeyboardInterrupt:
    print('That was a keyboard error, probably you pressed ctrl+c')
finally:
    print('Thank you for seeing this repository!')

'''
Raise Statement:
- It's possible to manually raise an exception in Python

Syntax:
raise Exception('Message')
- Exception is the type of exception(ex: ZeroDivisionError, KeyboardInterrupt)
- The argument 'Message' is a value for the exception which is optional.
'''

# Testing Raise Statement:
try:
    x = int(input('Enter a positive integer: '))
    if x <= 0:
        raise ValueError("Not a positive number")
except ValueError as e:
    print("Please type only numbers")