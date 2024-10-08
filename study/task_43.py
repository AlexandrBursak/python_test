from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def wrapper(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            result = None
            if list1 and list2:
                if list1.val < list2.val:
                    result = ListNode(list1.val)
                    # print('Result from list1:', list1.val, result)
                    result.next = wrapper(list1.next, list2)
                else: 
                    result = ListNode(list2.val)
                    # print('Result from list2:', list2.val, result)
                    result.next = wrapper(list1, list2.next)
            elif list1:
                result = ListNode(list1.val)
                # print('Result from list1:', list1.val, result)
                result.next = wrapper(list1.next, list2)
            elif list2:
                result = ListNode(list2.val)
                # print('Result from list2:', list2.val, result)
                result.next = wrapper(list1, list2.next)
            
            return result
        
        result = ListNode(0)
        result.next = wrapper(list1, list2)

        return result.next

    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     result = ListNode(0)

    #     def wrapper(list1: Optional[ListNode], list2: Optional[ListNode], result: Optional[ListNode]) -> Optional[ListNode]:

    #         if list1 and list2:
    #             if list1.val < list2.val:
    #                 result = list1
    #                 # print('Result from list1:', list1.val, result)
    #                 result.next = wrapper(list1.next, list2, result.next)
    #             else: 
    #                 result = list2
    #                 # print('Result from list2:', list2.val, result)
    #                 result.next = wrapper(list1, list2.next, result.next)
    #         elif list1:
    #             result = list1
    #             # print('Result from list1:', list1.val, result)
    #             result.next = wrapper(list1.next, list2, result.next)
    #         elif list2:
    #             result = list2
    #             # print('Result from list2:', list2.val, result)
    #             result.next = wrapper(list1, list2.next, result.next)
            
    #         return result
        
    #     result.next = wrapper(list1, list2, result.next)

    #     return result.next

solution = Solution()

head1 = None
for i in [1,2,4][::-1]:
    head1 = ListNode(i, head1)
head2 = None
for i in [1,2,3][::-1]:
    head2 = ListNode(i, head2)
expected = None
for i in [1,1,2,2,3,4][::-1]:
    expected = ListNode(i, expected)

result = solution.mergeTwoLists(head1, head2)
while result is not None:
    print(result.val, expected.val)
    result = result.next
    expected = expected.next


# head = None
# for i in [1][::-1]:
#     head = ListNode(i, head)
# target = 1
# expected = None
# for i in [][::-1]:
#     expected = ListNode(i, expected)

# result = solution.removeNthFromEnd(head, target)
