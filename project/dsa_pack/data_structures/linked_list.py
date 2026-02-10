from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


class SinglyLinkedList(Generic[T]):
    """A small singly-linked list.

    Supports append, prepend, find, delete-first, and iteration.

    This is intentionally minimal and beginner-friendly.
    """

    def __init__(self, items: Optional[Iterable[T]] = None):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._len = 0

        if items is not None:
            for x in items:
                self.append(x)

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterator[T]:
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def prepend(self, value: T) -> None:
        node = Node(value=value, next=self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._len += 1

    def append(self, value: T) -> None:
        node = Node(value=value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._len += 1

    def find(self, value: T) -> Optional[Node[T]]:
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def delete_first(self, value: T) -> bool:
        """Delete the first node with matching value.

        Returns True if a node was deleted.
        """

        prev: Optional[Node[T]] = None
        cur = self.head

        while cur is not None:
            if cur.value == value:
                if prev is None:
                    # deleting head
                    self.head = cur.next
                else:
                    prev.next = cur.next

                if cur is self.tail:
                    self.tail = prev

                self._len -= 1
                if self._len == 0:
                    self.head = self.tail = None
                return True

            prev, cur = cur, cur.next

        return False
