print("starting line")
a = [11, 22, 33]

try:
    a = 10 / 0
except NameError:
    print("exception raised due to undefined variable")
except IndexError:
    print("exception raised due to index out of rang")
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
exception raised due to zero division error
this is final block
ot side the try block
