from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif len(self.storage) < self.capacity:
            self.current.insert_after(item)
            self.storage.length += 1
            if len(self.storage) == self.capacity:
                self.current = self.storage.head
            else:
                self.current = self.current.next

        else:
            self.current.insert_after(item)
            if self.current == self.storage.head:
                self.storage.head = self.current.next
            self.current = self.current.next
            self.storage.delete(self.current.prev)
            self.storage.length += 1

            if self.current.next is None:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        pointer = self.storage.head
        while pointer:
            list_buffer_contents.append(pointer.value)
            pointer = pointer.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
