from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next

def show_result(res: ListNode):
    while res:
        print(res.val)
        res = res.next
    else:
        print('--- End ---')

solution = Solution()
l1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 3, next = None)))
l2 = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(val = 4, next = None)))
res = solution.addTwoNumbers(l1, l2)
# print(res.val)
show_result(res)

l1 = ListNode(val = 0, next = None)
l2 = ListNode(val = 0, next = None)
res = solution.addTwoNumbers(l1, l2)
# print(res.val)
show_result(res)

l1 = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = None)))))))))
l2 = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = None))))))
res = solution.addTwoNumbers(l1, l2)
# print(res.val)
show_result(res)
