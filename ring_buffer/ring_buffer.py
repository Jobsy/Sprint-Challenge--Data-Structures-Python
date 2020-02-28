from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if key in self.storage:
        if self.storage.length >= 0 and self.storage.length < self.capacity:
            # node = self.storage[key]
            # node.value = (key, value)
            # self.storage.move_to_end(item)
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            # return

        # if self.current_num_of_node == self.limit:
        # elif self.storage.length == self.capacity:
        elif self.current == self.storage.tail:
            # del self.storage[self.key_value_entries.head.value[0]]
            # self.key_value_entries.remove_from_head()
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head

            # self.current_num_of_node -= 1
        else:
            # self.key_value_entries.add_to_tail((key, value))
            self.current.insert_after(item)
            # self.storage[key] = self.key_value_entries.tail
            # self.current_num_of_node += 1
            self.storage.length += 1
            self.current = self.current.next
            self.storage.delete(self.current.next)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head

        while current != None:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
