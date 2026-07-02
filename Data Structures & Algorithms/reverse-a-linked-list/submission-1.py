# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        rev=[]
        if head is None:
            return None
        while node is not None:
            rev.append(node.val)
            node=node.next
        print(rev)
        rev.reverse()
        print(rev)

        new_head=ListNode(rev[0])
        tail=new_head

        for i in range(1,len(rev)):
            tail.next=ListNode(rev[i])
            tail=tail.next


        
        return new_head