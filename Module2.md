# Python Essentials 1: Module 2 - Basic, eg: Operators, Literals etc
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

### Types
* Refers to `int`, `string`, `float`, etc
* The type of a literal determines how python will store it in memory
* You can use underscores in numbers, e.g.: -100_000_000
* Floats cannot be empty
* Scientific notation uses 'eE', e.g.: 3e8
  * exponent (after 'eE')
  * base (before 'eE')

```python
"""
Python always chooses the _more economical 
form of the number's presentation_, and you 
should take this into consideration when creating literals.
"""
print(0.000000000000000000001) # outputs: 1e-21
```

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
### Arithmetic Operators
* `+ - * / // % **`
* `**` exponentiantion (to the power of)
  * `2**3` is 2 to the power of 3
  * when both args are ints, result is an int
  * when one arg is a float, result is a float  
* `//` integer divisional 
  * The result of integer division is always rounded to the nearest integer value that is less than the real (not rounded) result.
  * rounding always goes to the lesser integer.
  * `print(6. // 4) # 1.0`
  * Integer division can also be called *floor division*
* `%` Modulo, like php **remainder left after the integer division**
* `-` Expects two args, left: *minuend* and right: *subtrahend*
* Will prioritize mathematical operations in order, The phenomenon that causes some operators to act before others is known as **the hierarchy of priorities**.  
* The **binding** of the operator determines the order
* *most* operators use left side binding
  * `**` exponentiation operator uses right side binding
* subexpressions, `(parenthesis)` are calculated first
  * Parenthesis can improve readability
* **Unary operator** is an operator with only one operand, eg `-1`, `+3`
* **Binary operator** is an _operator_ with two, eg: `4+5` etc

| Priority | Operator | |
|---|:---|---:|
| 1 | `**` | | 
| 2 | `+`,`-` | unary| 
|3|`*`,`/`,`//`,`%`
|4|`+`,`-`|binary|

### Notables
> In Python you can use escaped chars ('\n') in single quoted strings, unlike PHP

### Variables
* A variable comes into existence as a result of assigning a value to it (no need to declare it)
* use `=` to assign 
* 'best practice' is to use snake_case
* not allowed to use a variable which doesn't exist (throws error '... is not defined') 


### Comments
* Ommited at runtime
* should give 'self-commenting' names
  * don't use confusing var names



### Miscellaneous
> Function names should be significant  

> Strings are delimited with quotes (either ' or ")  

> In Python, there cannot be more than one instruction per line  

> Python processes the instructions from top to bottom in order 



