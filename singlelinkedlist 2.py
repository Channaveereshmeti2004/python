class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printlinkedlist(head):
    curr = head
    while curr != None:
        print(curr.data,end = "-->")
        curr = curr.next
    print()
def insertatendoftail(head,ele):
    newblock = Node(ele)
    if head == None:
        return newblock

    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newblock

    return head

l = [11, 22, 33, 44, 55, 66, 77,88, 99, 110]
head = None
for ele in l:
    head = insertatendoftail(head,ele)
printlinkedlist(head)
