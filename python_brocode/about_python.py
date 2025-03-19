# # Python is primarily an interpreted language
# #
# # This means that Python code is executed line by line by the interpreter at runtime.
# 2. The Python Interpreter Process
# The Python interpreter follows these main steps to execute code:
#
# Step 1: Lexical Analysis
# The first step is tokenization. The interpreter reads the raw Python code and splits it into tokens (meaningful sequences like keywords, operators, identifiers, etc.).
# Example:
# The line print("Hello, World!") is broken down into:
# print (function name)
# ( (open parenthesis)
# "Hello, World!" (string)
# ) (closing parenthesis)
# Step 2: Parsing (Syntax Analysis)
# The tokens are passed to the parser. The parser checks the syntax of the code and creates a parse tree (or Abstract Syntax Tree, AST).
# It verifies that the code follows Python’s syntax rules (e.g., indentation, parentheses balance).
# Step 3: Compilation to Bytecode
# The parsed code is then converted into bytecode.
# Bytecode is a lower-level representation of your Python code, which is platform-independent.
# Why Bytecode? Python compiles the code into bytecode so it can be run on any platform with the Python interpreter, without needing to recompile it each time.
# The bytecode is a set of instructions for the Python Virtual Machine (PVM).
# Step 4: Python Virtual Machine (PVM)
# The PVM is the actual runtime engine that executes the bytecode.
# The bytecode is interpreted line-by-line by the PVM. This allows Python to be flexible, as the interpreter can execute any Python code.
# The PVM is platform-dependent, meaning different systems have their own PVMs (e.g., CPython, PyPy, Jython).
# Step 5: Execution
# The PVM executes the bytecode and produces the desired output, such as printing to the screen, performing calculations, or interacting with files.
# Example Output:
#
# bash
# Copy code
# Hello, World!
# How Python Handles Memory
# Memory management in Python is handled by automatic garbage collection.
# Python uses reference counting to track how many references point to an object.
# When an object’s reference count drops to zero, the memory is automatically freed.
# Python also uses a garbage collector to deal with cycles (e.g., objects referring to each other).
# Types of Python Interpreters
# CPython: The default and most widely used interpreter. Written in C and translates Python code to bytecode and then executes it on the PVM.
# PyPy: A highly efficient interpreter that uses Just-In-Time (JIT) compilation to speed up Python code execution.
# Jython: Python for the Java platform, compiling Python code to Java bytecode.
# IronPython: Python for the .NET framework, compiling Python code to .NET Common Intermediate Language (CIL).
# Stackless: A version of CPython that supports micro-threads for concurrent programming.
# Key Concepts in Python’s Execution Model
# Interpreter: The program that reads and executes Python code.
# Bytecode: A low-level representation of Python code that the Python Virtual Machine (PVM) can execute.
# Python Virtual Machine (PVM): The engine that executes Python bytecode.
# Garbage Collection: Automatically managing memory by cleaning up unused objects.
# Python's Execution Flow
# You write Python code (e.g., hello.py).
# Interpreter reads the code, breaks it into tokens, and parses it into an abstract syntax tree (AST).
# The AST is compiled to bytecode.
# The bytecode is executed by the PVM (Python Virtual Machine).
# Output is produced, and memory is cleaned up by garbage collection.
# Python’s Interactive Mode
# Python also has an interactive mode where you can execute Python code line by line in the interpreter (REPL: Read-Eval-Print-Loop).
# You can access it by typing python in the terminal:
# bash
# Copy code
# >>> print("Hello, World!")
# Hello, World!
# In interactive mode, the Python interpreter:
#
# Reads the code.
# Evaluates the expression.
# Prints the result.
