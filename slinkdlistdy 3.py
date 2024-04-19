class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printlinkedlist(head):
    curr = head
    while curr != None:
        print(curr.data,end = " ")
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

n = int(input())
l = list(map(int,input().split()))
head = None
for ele in l:
    head = insertatendoftail(head,ele)
printlinkedlist(head)
