# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists) -> ListNode:
        if not lists:
            return None
        elif len(lists) == 1 and isInstance(lists[0], ListNode):
            return lists[0]

        while len(lists) > 1:
            merged = []
            # 1,2,3,4,5
            # 0,2,4
            for i in range(0, len(lists), 2):
                if i+1 <= len(lists):
                    result = self.mergeLists(lists[i], lists[i+1])
                else:
                    result = lists[i]
                merged.append(result)
            lists = merged
        return lists[0]

    def mergeLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

