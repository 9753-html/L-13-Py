def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    return a / b
print("a. Add, b. Subtract, c. Multiply, d. Divide")
ch = input("Please Enter choice:")
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second Number"))
if ch == 'a':
    print("Sum:", add(n1,n2))
elif ch == 'b':
    print("Sub:", subtract(n1,n2))
elif ch == 'c':
    print("Product:", multi(n1,n2))
elif ch == 'd':
    print("Division:", div(n1,n2))
else:
    print("INVALID")