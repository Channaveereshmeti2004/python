print("starting line")
a = [11, 22, 33]

try:
    print(a)
    print(a[2])
except:
    print("some exeption raised")
else:
    print("no exeption is raised")

finally:
        print("this is final block")
print("ot side the try block")


output:
starting line
[11, 22, 33]
33
no exeption is raised
this is final block
ot side the try block
