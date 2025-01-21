def insertNodeAtHead(llist, data):
    if llist is None:
        llist = SinglyLinkedListNode(data)
        return llist
    temp = SinglyLinkedListNode(data)
    temp.next = llist
    llist = temp
    return temp