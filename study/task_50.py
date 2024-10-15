from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

# My algo, easy and readeable
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        list_of_nodes = []
        k_list = []
        i = 0

        while head:
            k_list.append(head.val)
            head = head.next
            i += 1
            if i % k == 0:
                list_of_nodes.extend(k_list[::-1])
                k_list = []

        if k_list:
            list_of_nodes.extend(k_list)

        for i in range(len(list_of_nodes) - 1, -1, -1):
            head = ListNode(list_of_nodes[i], head)

        return head

# Not my algo, a little bit faster than my
#     def reverseList(self, head, k):
#         prev = None
#         curr = head
        
#         for _ in range(k):
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node
        
#         return prev, curr # Return new head and the next node after k elements

#     def reverseKGroup(self, head, k):
#         dummy = ListNode(0)
#         dummy.next = head
#         ptr = dummy
        
#         while ptr is not None:
#             tracker = ptr
            
#             # Check if there are k nodes to reverse
#             for _ in range(k):
#                 tracker = tracker.next
#                 if tracker is None:
#                     return dummy.next # If fewer than k nodes, return result
            
#             # Reverse k nodes
#             prev, curr = self.reverseList(ptr.next, k)
            
#             last_node_of_reversed_group = ptr.next
#             last_node_of_reversed_group.next = curr
#             ptr.next = prev
            
#             ptr = last_node_of_reversed_group # Move ptr forward
        
#         return dummy.next