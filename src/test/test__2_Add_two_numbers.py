import pytest

from _2_Add_two_numbers import AddTwoNumbers, ListNode

testdata = [
    (ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))), [7, 0, 8]),
    (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))), [8, 9, 9, 9, 0, 0, 0, 1])
]


@pytest.mark.parametrize("l1, l2, expected", testdata)
def test_add_two_numbers(l1:ListNode, l2:ListNode, expected):
    actual_node = AddTwoNumbers.addTwoNumbers(l1, l2)
    actual = [actual_node.val]
    while actual_node.next:
        actual_node = actual_node.next
        actual = actual + [actual_node.val]

    assert actual == expected
