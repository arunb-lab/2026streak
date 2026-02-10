import unittest

from project.dsa_pack.data_structures.linked_list import SinglyLinkedList
from project.dsa_pack.data_structures.queue import Queue
from project.dsa_pack.data_structures.stack import Stack


class TestDataStructures(unittest.TestCase):
    def test_stack(self):
        s = Stack.from_iterable([1, 2, 3])
        self.assertEqual(len(s), 3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertIsNone(s.peek())
        with self.assertRaises(IndexError):
            s.pop()

    def test_queue(self):
        q = Queue.from_iterable(["a", "b"]) 
        self.assertEqual(q.peek(), "a")
        self.assertEqual(q.dequeue(), "a")
        q.enqueue("c")
        self.assertEqual(list(q), ["b", "c"])
        self.assertEqual(q.dequeue(), "b")
        self.assertEqual(q.dequeue(), "c")
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_linked_list(self):
        ll = SinglyLinkedList([1, 2, 3])
        self.assertEqual(list(ll), [1, 2, 3])
        ll.prepend(0)
        self.assertEqual(list(ll), [0, 1, 2, 3])
        self.assertTrue(ll.delete_first(2))
        self.assertEqual(list(ll), [0, 1, 3])
        self.assertFalse(ll.delete_first(999))
        self.assertEqual(len(ll), 3)


if __name__ == "__main__":
    unittest.main()
