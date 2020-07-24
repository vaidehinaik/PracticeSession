class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0

    def length(self):
        return self.size

    def insertAtBeginning(self, data):
        n = Node(data = data)
        if self.start is not None:
            n.next = self.start
        self.start = n
        self.size += 1
        # print("xyz {}".format(self.start.data))

    def insertAtEnd(self,data):
        n = Node(data = data)
        if self.start is None:
            self.start = n
        else:
            curr = self.start
            while curr.next is not None:
                curr = curr.next
            curr.next = n
        self.size += 1


    def removeFromBeginning(self):
        if self.start is None:
            print("List is empty")
        else:
            start = self.start.next
        self.size -= 1

    def removeAtEnd(self):
        if self.start is None:
            print("List is empty")
        else:
            curr = self.start
            while curr.next.next != None:
                curr = curr.next
            curr.next = None
        self.size -= 1


    def display(self):
        # print("---> {}".format(self.start))
        if self.start is None:
            print("List is empty")
        else:
            curr = self.start
            while curr is not None:
                print("---> {}".format(curr.data))
                curr = curr.next

    # def isCyclic(self,head):
    #     slow = head
    #     fast = head
    #     while fast is not None and fast.next is not None:
    #         if slow is fast:
    #             return True
    #         slow = slow.next
    #         fast = fast.next.next
    #     return False
    #
    #
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if head is None:
    #         return False
    #     slowPointer = head
    #     fastPointer = head.next
    #     while slowPointer is not None and fastPointer is not None:
    #         if slowPointer == fastPointer:
    #             return True
    #         slowPointer = slowPointer.next
    #         fastPointer = fastPointer.next
    #         if fastPointer is not None:
    #             fastPointer = fastPointer.next
    #     return False


    # def hasCycle(self, head: ListNode) -> bool:
    #     if head is None:
    #         return None
    #     slow = head
    #     fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #         if slow == fast:
    #             return True
    #     return False


    # def addNode(self,data):
    #     n = Node(data=data)
    #     if (self.start == None):
    #         start = n
    #     else:
    #         n.next = self.start
    #         self.start = n
    #
    # def deletNode(self):
    #     if self.start != None:
    #         temp = self.start
    #         self.start = self.start.next
    #         temp = None


    # def removeElements(self, head, val):
    #     """
    #     :type head: ListNode
    #     :type val: int
    #     :rtype: ListNode
    #     """
    #     if head is None:
    #         return None
    #     while head and head.val == val:
    #         if head.next:
    #             head = head.next
    #         else:
    #             return None
    #     curr = head
    #     while curr and curr.next:
    #         if curr.next.val == val:
    #             curr.next = curr.next.next
    #         else:
    #             curr = curr.next
    #     return head


    # def middleNode(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if head is None:
    #         return None
    #     slow = head
    #     fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.start = None
#         self.size = 0
#     def length(self):
#         self.size


# Deep copy:

# if not head:
#     return None
# curr = head
# d = dict()
# dummy = Node(0)
# new_curr = dummy
# while curr:
#     n = Node(curr.val)
#     new_curr.next = n
#     new_curr = new_curr.next
#     d[curr] = new_curr
#     curr = curr.next
# curr = head
# while curr != None:
#     if curr.random == None:
#         d[curr].random = None
#     else:
#         rand = curr.random
#         new_addr = d[rand]
#         d[curr].random = new_addr
#     curr = curr.next
# return dummy.next
#
#
#
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBeginning(data=50)
    ll.insertAtBeginning(data=40)
    ll.insertAtBeginning(data=30)
    ll.insertAtBeginning(data=20)
    ll.insertAtBeginning(data=40)
    ll.display()
    ll.removeFromBeginning()
    ll.removeFromBeginning()
    ll.display()
    ll.isCyclic()




# def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:
#             return None
#         curr = head.next
#         d = dict()
#         new_curr = head2 = Node(head.val)
#         d[head] = new_curr
#         while curr:
#             n = Node(curr.val)
#             new_curr.next = n
#             new_curr = new_curr.next
#             d[curr] = new_curr
#             curr = curr.next
#         curr = head
#         while curr != None:
#             if curr.random == None:
#                 d[curr].random = None
#             else:
#                 rand = curr.random
#                 new_addr = d[rand]
#                 d[curr].random = new_addr
#             curr = curr.next
#         return head2
#



# def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#
#         if head is None:
#             return None
#         prev = None
#         while head:
#             curr = head
#             head = head.next
#             curr.next = prev
#             prev = curr
#         return curr
#
#


# def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """
#
#         node.val = node.next.val
#         node.next = node.next.next
#


# def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         if l1 is None and l2 is None:
#             return None
#         dummy = ListNode(0)
#         curr = dummy
#         while l1 and l2:
#             if l1.val < l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
#         curr.next = l1 or l2
#         return dummy.next


# def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#
#         if head is None:
#             return None
#         curr = head
#         while curr and curr.next:
#             if curr.val == curr.next.val:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
#         return head
#



# def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#
#         # if headA is None:
#         #     return headB
#         # if headB is None:
#         #     return headA
#         # if headA and headB is None:
#         #     return None
#         currA = headA
#         currB = headB
#         while currA and currB:
#             if currA.next is None:
#                 currA = headB
#             else:
#                 currA = currA.next
#             if currB.next is None:
#                 currB = headA
#             else:
#                 currB = currB.next
#         return currA



# def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         def reverseList(head):
#             if head is None:
#                 return None
#             prev = None
#             while head:
#                 curr = head
#                 head = head.next
#                 curr.next = prev
#                 prev = curr
#             return curr
#         if not head or not head.next:
#             return head
#         slow = head
#         fast = head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         head2 = slow.next
#         slow.next = None
#         head2 = reverseList(head2)
#         head1 = head
#         while head1 is not None and head2 is not None:
#             head1.next, head1 = head2, head1.next
#             head2.next, head2 = head1, head2.next
#         return head
#
#
#
