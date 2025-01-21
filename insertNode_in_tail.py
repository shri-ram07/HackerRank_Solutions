def insertNodeAtTail(head, data):
    if head is None:
        head=SinglyLinkedListNode(data)
        return head
    new = SinglyLinkedListNode(data)
    temp = head
    while temp.next:
        temp=temp.next
    temp.next=new
    return head