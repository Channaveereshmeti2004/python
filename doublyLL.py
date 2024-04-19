class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def PrintHeadtoTail(head):
    print("head to tail")
    curr = head
    while curr != None:
        print(curr.data,end = "-->")
        curr = curr.next
    print()

def PrintTailToHead(tail):
    print("tail to head")
    curr = tail
    while curr != None:
        print(curr.data,end = "-->")
        curr = curr.prev
    print()

#object creation
obj1 = Node(121)
obj2 = Node(145)
obj3 = Node(678)
obj4 = Node(637)
obj5 = Node(12)

#LINK establish
obj1.next = obj2
obj2.prev = obj1

obj2.next = obj3
obj3.prev = obj2

obj3.next = obj4
obj4.prev = obj3

obj4.next = obj5
obj5.prev = obj4

PrintHeadtoTail(obj1)
PrintTailToHead(obj5)


output:
head to tail
121-->145-->678-->637-->12-->
tail to head
12-->637-->678-->145-->121-->
