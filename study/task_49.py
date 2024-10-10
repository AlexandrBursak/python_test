# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return
        if not head.next:
            return head
        
        new_head = None
        even_list = []
        odd_list = []
        i = 0
        while head:
            if i%2:
                even_list.append(head.val)
            else:
                odd_list.append(head.val)
            head = head.next
            i += 1
        
        for i in range(len(odd_list)-1, -1, -1):
            new_head = ListNode(odd_list[i], new_head)
            if i < len(even_list):
                new_head = ListNode(even_list[i], new_head)

        return new_head
