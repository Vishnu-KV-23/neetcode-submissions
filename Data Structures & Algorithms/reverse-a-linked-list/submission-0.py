# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        copy=[]
        while node is not None:
            copy.append(node.val)
            node=node.next

        print(copy)
        copy.reverse()
        
        tail= None
        head=None
        for i in range(len(copy)):
            node= ListNode(copy[i])
            if tail:
                tail.next=node
                tail=node
            else:
                head=node
                tail=node
        node = head
        # while node is not None:
        #     print(node.val,end="   ")           
        return head


            

        