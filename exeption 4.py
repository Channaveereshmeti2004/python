print("starting line")
a = [11, 22, 33]

try:
    print(y)
    
except NameError:
    print("exception raised due to undefined variable")
try:
    print(a[5])
except IndexError:
    print("exception raised due to index out of rang")
try:
    a = 10 / 2
except ZeroDivisionError:
    print("exception raised due to zero division error")
except:
    print("some exeption raised")
else:
    print("no exeption is raised")

finally:
        print("this is final block")
print("ot side the try block")



output:

starting line
exception raised due to undefined variable
exception raised due to index out of rang
no exeption is raised
this is final block
ot side the try block
