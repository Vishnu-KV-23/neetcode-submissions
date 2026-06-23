class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:   # guard clause first
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node   # maintain prev pointer
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail   # maintain prev pointer
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:     # strictly greater — don't insert
            return
        if index <= 0:              # treat negative index as 0
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return

        # Walk to the node currently AT `index`
        curr = self.head
        for _ in range(index):
            curr = curr.next

        # Insert new node before curr
        node = Node(val)
        node.next = curr
        node.prev = curr.prev
        curr.prev.next = node
        curr.prev = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        # Special cases for head/tail
        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            # Stitch neighbours together
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self.length -= 1