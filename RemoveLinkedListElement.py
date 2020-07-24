def removeLinkedListElement(head,val):
    if head is None:
        return None
    while head and head.val == val:
        head = head.next
    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

