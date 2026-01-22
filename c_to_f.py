def f2c(f):
    return (f-32)/1.8

print(f2c(32))
print(f2c(95))


for l in 'letter':
    print(l)
else:
    # Happens when l becomes None
    print(l)
    print('gotcha')
print('done')

for l in '':
    print(l)
    if l == 'd': 
        break
else: 
    # Happens if for loop fails
    print('done')


n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else while")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else for")

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

print("\n")
x = 1
while x < 11:
    if x % 2 != 0:
        print(x, end="-")
    x += 1
    
print('\n')
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
    
print('\n')
for digit in "0165031806510":
    if digit == "0":
        print('x', end="")
    print(digit, end="")

print(str(range(4)))