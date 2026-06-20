class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None
     
        # count+=1        

    
    def get(self, index):
        i=0
        node=self.head
        while node is not None:
            if i==index:
                return node.val
            node=node.next
            i=i+1
        return -1
        
        

    def insertHead(self, val):
        node=Node(val)
        if self.head:
            node.next=self.head
            self.head=node

        else:
            self.head=node
            self.tail=node


        

    def insertTail(self, val):
        node=Node(val)
        if self.tail:
            self.tail.next=node
            self.tail=node
        else:
            self.head=node
            self.tail=node        
        
    def remove(self, index):
        if self.head is None:
            return False
        node=self.head
        i=0
        if self.head is self.tail and index==0:
            self.head=None
            self.tail=None
            
            return True
        if index==0:
            self.head=self.head.next
            return True
        
        while node is not None:
            
            if i==index-1:
                if node.next is self.tail:
                    self.tail=node
                    self.tail.next=None
                    return True
                    
                else:    
                    node.next=node.next.next
                    return True
            node=node.next
            i=i+1
        return False
                

        

    def getValues(self):
        op=[]
        node=self.head
        while node!=None:
            op.append(node.val)
            node=node.next        
        return op
ll=LinkedList()

# ip= input().split()
# print(ip)
# for i in range(len(ip)):
#     if i=="insertHead":
#         ll.insertHead(int(ip[i+1]))
#     elif i=="insertTail":
#         ll.insertTail(int(ip[i+1]))
#     elif i=="remove":
#         ll.remove(int(ip[i+1]))
#     elif "get":
#         ll.get(int(ip[i+1]))
#     elif "getValues":
#         ll.getValues()
#     else:
#         pass
    