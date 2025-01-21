def insertNodeAtPosition(llist, data, position):
    if llist is None:
        llist = SinglyLinkedListNode(data)
        return llist
    pos = 0
    temp = SinglyLinkedListNode(data)
    itr = llist

    while pos != position:
        pos += 1
        itr_prev = itr
        itr = itr.next
    temp2 = itr
    temp.next = temp2
    itr_prev.next = temp
    return llist