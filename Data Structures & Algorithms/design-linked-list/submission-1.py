class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class MyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def get(self,index):
        if index<0 or index>=self.size:
            return -1
        i=0
        node=self.head
        while node is not None:
            if i==index:
                return node.val
            node=node.next
            i+=1

    def addAtHead(self,val):
        node=Node(val)
        if self.head:
            self.head.prev=node
            node.next=self.head
            self.head=node
            self.size+=1
        else:
            self.head=node
            self.tail=node
            self.size+=1

    def addAtTail(self,val):
        node=Node(val)
        if self.tail:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
            self.size+=1
        else:
            self.head=node  
            self.tail=node
            self.size+=1
    def addAtIndex(self,index,val):
        if index <0 or index > self.size :
            return 
        iterator=self.head
        node=Node(val)
        i=0

        if index==0:
            self.addAtHead(val)
            return
        if index==self.size:
            self.addAtTail(val)
            return
        
        while iterator is not None:
            if i==index-1:
                node.prev=iterator
                node.next=iterator.next
                iterator.next.prev=node
                iterator.next=node
                self.size+=1
                break
            iterator=iterator.next
            i=i+1

    def getValues(self):
        op=[]
        node=self.head
        while node!=None:
            op.append(node.val)
            node=node.next        
        return op

    def deleteAtIndex(self,index):
        if index<0 or index>=self.size:
            return
        if index==0:
            self.head=self.head.next
            if self.head:
                self.head.prev= None
            else:
                self.tail=None
            self.size-=1
            return
        if index==self.size-1:
            self.tail=self.tail.prev
            self.tail.next=None
            self.size-=1
            return 

        iterator=self.head
        i=0
        while iterator is not None:
            if i==index-1:
                iterator.next=iterator.next.next
                iterator.next.prev=iterator
                self.size-=1
                break
            iterator=iterator.next
            i+=1

















