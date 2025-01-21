def printLinkedList(head):
    if head is None:
        print("Empty Linked List")
        return
    temp = head
    while temp:
        print(temp.data)
        temp=temp.next