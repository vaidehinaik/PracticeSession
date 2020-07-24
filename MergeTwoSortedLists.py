class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def mergeTwoSortedLists(l1,l2):
    if l1 is None:
            return l2
    if l2 is None:
        return l1
    if l1 is None and l2 is None:
        return None
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.data > l2.data:
            curr.next = l2
            l2 = l2.next
        else:
            curr.next = l1
            l1 = l1.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None
        dummy = head = ListNode(0)
        carry = 0
        while l1 != None or l2 != None:
            if l1 is None:
                sum_val = l2.val+carry
                l2 = l2.next
            elif l2 is None:
                sum_val = l1.val+carry
                l1 = l1.next
            else:
                sum_val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            carry = sum_val//10
            head.next = ListNode(sum_val%10)
            head = head.next

        if carry != 0:
            head.next = ListNode(carry)
        return dummy.next

