# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1=[]
        l2=[]
        i1=list1
        i2=list2
        while (i1 is not None):
            l1.append(i1.val)
            i1=i1.next
        while (i2 is not None):
            l2.append(i2.val)
            i2=i2.next
        l1.extend(l2)
        l1.sort()

        tail=None

        for i in range(len(l1)):
            node=ListNode(l1[i])
            if tail:
                tail.next=node
                tail=node
            else:
                tail=node
                head=node
        # print(l1,l2)


        return head