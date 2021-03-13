class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# for calculating length of linked list
def length(head):
    count = 0
    while head is not None:
        head = head.next
        count = count + 1
    return count


def length_recursion(head):
    if head == None:
        return 0
    else:
        return 1 + length_recursion(head.next)


def insertatirecurse(head, i, data):
    if i < 0:
        return head
    if i == 0:
        newnode = Node(data)
        newnode.next = head
        return newnode
    if head is None:
        return None

    smallhead = insertatirecurse(head.next, i - 1, data)
    head.next = smallhead
    return head


def insertati(head, i, data):
    if i < 0 or i > length(head):
        return head
    count = 0
    prev = None
    curr = head

    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1
    newnode = Node(data)
    if prev is None:
        head = newnode
    else:
        prev.next = newnode
        newnode.next = curr
    return head


def deletefromirecurse(head, i):
    if i < 0:
        return head

    if head is None:
        return None

    if i == 0:
        return head.next

    smallhead = deletefromirecurse(head.next, i - 1)
    head.next = smallhead
    return head


# for deleting node from ith position
def deletefromi(head, i):
    if i < 0 or i > length(head):
        return head
    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1
    if prev is None:
        head = head.next
    elif count == length(head):
        prev.next = None
    else:
        prev.next = None
        prev.next = curr.next
        curr = curr.next
    return head


# for print ith node in linked list
def printithnode(head, i):
    count = 0
    while head is not None:
        if count == i:
            print(head.data)
        count = count + 1
        head = head.next


def printll(head):
    while head is not None:
        print(str(head.data) + "-->", end=" ")

        head = head.next
    print("None")
    return


def find_node(head, i):
    curr = head
    count = 0
    while curr is not None:
        if curr.data == i:
            return count
        curr = curr.next
        count = count + 1
    return -1


def sort_linked_list(head):
    curr = head
    index = None
    if curr == None:
        return
    else :
        while curr is not None:
            index = curr.next
            while index is not None:
                if index.data < curr.data :
                    curr.data , index.data = index.data,curr.data
                index = index.next
            curr = curr.next
        return head

def find_duplicates(head):
    curr = head
    if head == None or head.next == None:
        return
    while curr.next is not None:
        if curr.data == curr.next.data:
            curr.next.data = None
            curr.next = curr.next.next
        else :
            curr = curr.next

    return head

def print_reverse(head):
    prev = None
    curr = head
    if head == None:
        return
    else:
        while curr is not None:
            prev = curr
            curr = curr.next
            if curr.next == None:
                head = curr

    return head





def taking_input():
    inputelements = [1,2,3,4,5]
    head = None
    tail = None
    for currdata in inputelements:
        if currdata == -1:
            break
        newnode = Node(currdata)
        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode
    return head


head = taking_input()
printll(head)
# print(length(head))
# printithnode(head, int(input("enter index to be searched for")))
# head = insertati(head,5,4)
# printll(head)
# head = insertati(head,2,5)
# printll(head)
# head = deletefromi(head,4)
# printll(head)
# print(length_recursion(head))
# head = insertatirecurse(head,int(input()),8)
# printll(head)
# head = deletefromirecurse(head,3)
# printll(head)
# print(find_node(head, 4))
# slist = sort_linked_list(head)
# printll(slist)
# head = find_duplicates(head)
# printll(head)
l = print_reverse(head)
printll(l)