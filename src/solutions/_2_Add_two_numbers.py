# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = l1, l2
        result = ListNode()
        current = result
        while first or second:
            current_sum = (first.val if first else 0) + (second.val if second else 0)
            for_the_next_node = (current.val + current_sum) // 10
            current.val = current.val + current_sum - for_the_next_node * 10

            first = first.next if first and first.next else None
            second = second.next if second and second.next else None

            if first or second or for_the_next_node != 0:
                current.next = ListNode()
                current.next.val = for_the_next_node
                current = current.next

        return result


