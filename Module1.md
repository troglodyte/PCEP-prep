## Python Essentials 1 - Beginner Course
### Definitions
* IL = Instruction List
* Lexis = Dictionary
* Syntax = set of rules
* Semantics = set of rules determining if a certain phrase makes sense
* IL is the alphabet of a machine language
  * Source code written in a source file
  * Source code is 'A program written in a high-level programming language'
  

### Compilation vs. interpretation
Two ways to transforming a program from a high-level programming language into machine language
* Compilation: translated, compiled 
* Interpretation: executed, interpreted
  * If the interpreter finds an error, it finishes its work immediately. The only result in this case is an error message.  
  * so the trio "read-check-execute" can be repeated many times - more times than the actual number of lines in the source file, as some parts of the code may be executed more than once).
  * Python is an interpreted language.
  * If you want to program in Python, you'll need the Python interpreter. 
  * Often referred to as a 'Scripting Language', programs called 'scripts'

### What is Python?
* Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.
* Monty Python's Flying Circus
* Python was created by **Guido van Rossum**, born in 1956 in Haarlem, the Netherlands

### Python Goals
* Easy and intuitive
* Open source
* Understandable
* Suitable for everyday tasks
* Python is mature and trustworthy.

### Python Pros
* easy to learn
* easy to teach
* easy to use
* easy to understand
* easy to obtain, install and deploy 

### Python drawbacks
* Python is not fast.
* harder to test

### Direct Competitors
* Perl - scripting language
* Ruby - scripting language

### Where is Python?
* Internet services
* developing tools
* everyday applications
* scientists, testers

### Where Python is not used?
* low-level programming
* mobile device applications

### Python Versions
* Python 2.7 - no longer new features, still supported
* Python 3.x - current version
* breaking changes
* Python 3 is a complete different language
* If you're going to start a new Python project, you should use Python 3, and this is the version of Python that will be used during this course.
* All 3x versions are backward compatible with previous 3x versions
 
### Python Software Foundation 
* All Pythons coming from the PSF are written in the "C" language.
* This is why the PSF implementation is often referred to as CPython.

### Cython
* when you're absolutely sure that your code is correct and produces valid results, you can translate it into "C". Certainly, "C" will run much faster than pure Python.
* This is what Cython is intended to do – to automatically translate the Python code (clean and clear, but not too swift) into "C" code (complicated and talkative, but agile).

### Jython 
* Java implementation of Python.
* Note: the current Jython implementation follows Python 2 standards. 
* There is no Jython conforming to Python 3, so far.

### PyPy 
* Python implementation written in Python.
* It is actually a subset of Python.
* The source code of PyPy is not run in the interpretation manner, but is instead translated into the C programming language and then executed separately.
* PyPy is compatible with the Python 3 language.

### IDLE is an acronym: Integrated Development and Learning Environment.

### Python Errors
* traceback
* location of the error, could be misleading
  * python shows the line where it noticed the error, not necessarily the line where the error actually occurred.
* content of the erroneous line
* name of the error
