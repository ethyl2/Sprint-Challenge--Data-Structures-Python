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
        self.capacity = capacity
        self.current = None
        self.storage = [None for i in range(0, capacity)]

    def append(self, item):
        print(self.storage)
        if self.current is None:
            self.storage[0] = item
            self.current = 1
        else:
            self.storage[self.current] = item
            self.current += 1
            if self.current == self.capacity:
                self.current = 0
        print(self.storage)
        print('\n')

    def get(self):
        list_buffer_contents = []
        for item in self.storage:
            if item is not None:
                list_buffer_contents.append(item)
        return list_buffer_contents
