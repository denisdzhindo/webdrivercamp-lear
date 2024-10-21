What’s the difference between errors and exceptions

In Python, an error is an issue that prevents your program from executing successfully. There are two main types of errors:

Syntax Errors: These occur when the Python interpreter encounters code that doesn't follow the correct syntax rules of the language. This is similar to a grammatical error in a sentence. If syntax errors are present, however, the interpreter will catch them before executing the program and inform you that it can't understand the code that you've written.
For example, if you try executing []] in Python, the code won't be executed, and a SyntaxError will instead be raised.

Runtime Errors or Exceptions:

When your program runs into an exception, Python is nice enough to stop and generate a nifty little message explaining where the error origianted and why occured. This can serve as good starting point to then further debug your code.
An exception, in Python, is raised when something unexpected happens during the execution of your program. For instance you try to convert the string "hello" into an integer, your program will raise a ValueError.
If you anticipate that a part of your code might, in some cases, raise an exception, you can surround that part of the code with a try/except block and prevent your program from completely crashing.
Python is an interpreted language, which means that all exceptions other than syntax errors occur at run-time, while the program is being executed.
For example, if you try executing [0, 1, 2][3] in Python, the code will indeed be executed, and the resulting IndexError will be raised at run-time.


if x = 5:  # SyntaxError: invalid syntax
    print("Hello")

What are exceptions and how to use them

When do we need to use exceptions

How to correctly handle an exception

What’s the purpose of catching exceptions

How to raise a builtin exception

When do we need to implement a clean-up action after an exception
