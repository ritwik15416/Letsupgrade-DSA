# Q2. 
a = int(input("Enter 1st value:"))
b = int(input("Enter 2nd value:"))
def swap(a,b):
    a,b=b,a
    return a,b
print(swap(a,b))

# Q1.
class Sum:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(a,b):
        return a+b

a = int(input('enter 1st no: '))
b = int(input('enter 2nd no: '))
obj = Sum.add(a,b)
print(obj)
