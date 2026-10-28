# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head
        tl=0
        while(head!=None):
            tl=tl+1
            head=head.next
        tl=tl//2
        tl=tl+1
        head=l
        count=0
        while(head!=None):
            count=count+1
            if count==tl:
                return head
            head=head.next
        
        