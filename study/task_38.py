from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


solution = Solution()

head = None
for i in [1,2,3,4,5][::-1]:
    head = ListNode(i, head)
target = 2
expected = None
for i in [1,2,3,5][::-1]:
    expected = ListNode(i, expected)

result = solution.removeNthFromEnd(head, target)
while result is not None:
    print(result.val, expected.val)
    result = result.next
    expected = expected.next


head = None
for i in [1][::-1]:
    head = ListNode(i, head)
target = 1
expected = None
for i in [][::-1]:
    expected = ListNode(i, expected)

result = solution.removeNthFromEnd(head, target)
