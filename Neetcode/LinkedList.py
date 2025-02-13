# https://neetcode.io/problems/singlyLinkedList

class ListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1

        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if i < index or not curr:
            return -1
        else:
            return curr.value

    def insertHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        
        if not self.head:
            self.head = new_tail
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_tail

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        i = 1
        curr = self.head
        while i < index and curr.next:
            i += 1
            curr = curr.next

        if i == index and curr.next:
            curr.next = curr.next.next
            return True
        else:
            return False 


    def getValues(self) -> list[int]:
        values = []

        curr = self.head
        while curr:
            values.append(curr.value)
            curr = curr.next

        return values
