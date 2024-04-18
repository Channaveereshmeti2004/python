try:
    a = 10 / 5
    print(a)
except:                  # it exicute if the exception is raised
    print("some exception raised")
else:                    #if there is no exeption it exicute
    print("no exeption is raised ")
finally:                  #it exicute both condition 
    print("this is final block")
print("ot side the try block")



output:
	2.0
no exeption is raised 
this is final block
ot side the try block

