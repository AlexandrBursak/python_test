# Definition for singly-linked list.
from typing import List, Optional
from math import inf
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # My logic (works)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        len_lists = len(lists)
        strike = 0

        current_val = float(inf)
        if not lists:
            return

        def nodeLoop(lists, current_val, strike):
            result = None
            temp_list = {}
            for i in range(len_lists):
                if not lists[i]:
                    continue
                if lists[i].val < current_val:
                    temp_list = {}
                    temp_list[i] = lists[i]
                    current_val = lists[i].val
                elif lists[i].val == current_val:
                    temp_list[i] = lists[i]
            
            if temp_list:
                for j in temp_list.keys():
                    lists[j] = lists[j].next
                    if lists[j] is None:
                        strike += 1

                if strike != len_lists:
                    current_val = float(inf)
                    result = nodeLoop(lists, current_val, strike)
            
                for j in temp_list.keys():
                    result = ListNode(temp_list[j].val, result)

            return result

        return nodeLoop(lists, current_val, strike)