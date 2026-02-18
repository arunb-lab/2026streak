"""DSA - Linked List: Reverse Linked List

Problem:
Given the head of a singly linked list, reverse the list and return the new head.

Approach (iterative):
- Walk the list once, reversing pointers as we go.

Time: O(n)
Space: O(1)
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ListNode:
    val: int
    next: "ListNode | None" = None


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev: ListNode | None = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def to_list(head: ListNode | None) -> list[int]:
    out: list[int] = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out


def from_list(values: list[int]) -> ListNode | None:
    head: ListNode | None = None
    for x in reversed(values):
        head = ListNode(x, head)
    return head


if __name__ == "__main__":
    head = from_list([1, 2, 3, 4, 5])
    rev = reverse_list(head)
    assert to_list(rev) == [5, 4, 3, 2, 1]

    assert reverse_list(None) is None
    assert to_list(reverse_list(from_list([42]))) == [42]
    print("ok")
