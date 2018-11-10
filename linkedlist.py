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
        n = Node(data=data)
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

    # def isCyclic(self):




if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBeginning(data=50)
    ll.insertAtBeginning(data=40)
    ll.insertAtBeginning(data=30)
    ll.insertAtBeginning(data=20)
    ll.insertAtBeginning(data=10)
    ll.display()
    ll.removeFromBeginning()
    ll.removeFromBeginning()
    ll.display()




