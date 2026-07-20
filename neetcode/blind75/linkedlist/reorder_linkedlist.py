class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        _list = f"{self.val}"
        cur = self
        while cur.next:
            _list += f" -> {cur.next.val}"
            cur = cur.next
        return _list


class Solution():

    def __reverse(self, head: ListNode):
        previous = None
        current = head
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        print(f"reversed: {previous}")
        return previous


    def reorderList(self, head: ListNode) -> None:

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        print(f"first: {head}")
        print(f"second: {second_head}")

        # reverse second half
        second_half = self.__reverse(second_head)

        # merge
        while second_half:
            firstNext = head.next #4
            secondNext = second_half.next #6
            head.next = second_half #2->8
            second_half.next = firstNext #2->8>4
            head = firstNext
            second_half = secondNext
        print(f"head: {head}")
