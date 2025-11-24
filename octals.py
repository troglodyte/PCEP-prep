from AppKit import NSBeep
import sys

print(0o1234, end="\n\n")
try:
    print(oct(int(input('Give me an int to convert to octal: '))))
except Exception as e:
    if sys.platform == 'darwin':
        NSBeep()
    print(f"Error: {e}")

