from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import count
from typing import Generic, Iterable, Optional, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class ListNode(Generic[T]):
    val: T
    next: Optional[ListNode[T]] = None


def from_list(values: Iterable[T]) -> Optional[ListNode[T]]:
    head: Optional[ListNode[T]] = None
    tail: Optional[ListNode[T]] = None
    for v in values:
        node: ListNode[T] = ListNode(v)
        if head is None:
            head = tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node
    return head


def to_list(head: Optional[ListNode[T]]) -> list[T]:
    out: list[T] = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out


def merge_k_lists(lists: list[Optional[ListNode[T]]]) -> Optional[ListNode[T]]:
    """Merge k sorted linked lists into one sorted list.

    Time:  O(N log k) where N is total nodes.
    Space: O(k) for heap.
    """

    # Tie-breaker counter avoids needing ListNode comparability.
    seq = count()
    heap: list[tuple[T, int, ListNode[T]]] = []

    for node in lists:
        if node is not None:
            heappush(heap, (node.val, next(seq), node))

    dummy: ListNode[T] = ListNode(val=0)  # type: ignore[arg-type]
    tail = dummy

    while heap:
        _, _, node = heappop(heap)
        tail.next = node
        tail = node

        nxt = node.next
        # Detach to avoid accidentally keeping old chains when reusing nodes.
        node.next = None

        if nxt is not None:
            heappush(heap, (nxt.val, next(seq), nxt))

    return dummy.next
