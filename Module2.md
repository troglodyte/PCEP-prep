# Python Essentials 1: Module 2
### Functions
- Cause some effect
- evaluate a value
- return an evaluated value
- have an 'effect' & 'result'
- Can have arguments
- functions have parenthesis

### Source of functions 
- Built-in functions
- Modules
- User-defined functions

### Invoking a function
- "The function name (print in this case) along with the parentheses and argument(s), forms the function invocation."
1. First checks if the name is legal
2. Checks the functions requirements, to see if it allows you to invoke it
3. Python leaves the code for a moment, to jump to the function you want to invoke
4. Executes its code, causes the desired effect
5. Returns to your code and resumes Execution
6. Calling a function is referred to as `function invocation` or `function call`

### `print()`
* Sends the result to the output device (e.g. the console)
* Can take all types of data
* Does not return anything
* With multiple arguments adds a space between them, all on one line
  * e.g. `print('a','b') # 'a b'`

### Strings
* can be single or double quotes, (escaping chars is possible in _each_)

### Literals
* "A literal is data whose values are determined by the literal itself" 
* like `123` _is_ 123, `c` is not.
* You use literals 'to encode data and put them into your code'

### Functional Arguments
* Passing arguments with commas is called '*the positional way*'
  * `print('a', 'b') # 'a b'`
* You can pass arguements by *'Keyword Arguments'*
  * `print('hi', end=" ") # 'hi ' (no new line at the end), next print will be on this line`
    * the `end=` keyword *implicitly* uses `\n` (as default = implicitly)
  * You cannot use positional arguments after keyword arguments
    * e.g. `print('hi', end=" ", 'there') # SyntaxError`
  * Keyword arguments can be used in any order
  * 

### Notables
> In Python you can use escaped chars ('\n') in single quoted strings, unlike PHP

### Miscellaneous
> Function names should be significant  

> Strings are delimited with quotes (either ' or ")  

> In Python, there cannot be more than one instruction per line  

> Python processes the instructions from top to bottom in order 



