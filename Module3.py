n = int(input('Enter a number: '))
print(True if n > 100 else False)

n1 = int(input('Enter another number: '))
n2 = int(input('Enter yet another number: '))
n3 = int(input('Enter yet another number: '))

largest_number = max(n1, n2, n3)
smallest_number = min(n1, n2, n3)
print("Largest number: " + str(largest_number))
print("Smallest number: " + str(smallest_number))

s = input('')

if s == 'SPATH':
    print(s)
elif s== 'spath':
    print("I want a big spath!")
else:
    print('SPATH! not ' + s)

income = float(input("Enter the annual income: "))

if income < 85_528:
    tax_gross = income * .18
    tax = tax_gross - 556
else:
    tax_gross = 14_839.2
    overage = income - 85_528
    tax = tax_gross + (overage * .32)

tax = round(tax, 0)
print(
    "The tax is:",
    tax if tax > 0 else 0,
    "thalers"
    )
