import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not list:
            return None
        dummy = ListNode(-1)
        point = dummy
        queue = list()
        for i, l in enumerate(lists):
            if lists[i]:
                heapq.heappush(queue, (l.val, i, l))

        while len(queue) > 0:
            val, idx, node = heapq.heappop(queue)
            newNode = ListNode(val)
            point.next = newNode
            point = point.next # move forward the new list pointer
            node = node.next # move forward the pointer in the list whose node is accessed
            if node: # if pointer is not none then push it to the heapq else skip
                heapq.heappush(queue, (node.val, idx, node))
        return dummy.next
