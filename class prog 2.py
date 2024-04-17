class Box:
    def __init__(self, currname,currrollno,currdbmsmarks,currosmarks,currjavamarks,currdsmarks,currcmarks):
        self.name = currname
        self.rollno = currrollno
        self.dbmsmarks = currdbmsmarks
        self.osmarks = currosmarks
        self.javamarks = currjavamarks
        self.dsmarks = currdsmarks
        self.cmarks = currcmarks

student1 = Box( "channa",263,88,75,92,95,80)
print(student1.name)
print(student1.rollno)
print(student1.cmarks)


student2 = Box("veeresh",561,78,65,64,89,38)
print(student2.name)
print(student2.rollno)
print(student2.cmarks)

output:
channa
263
80
veeresh
561
38
