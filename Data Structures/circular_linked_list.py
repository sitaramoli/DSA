class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            node.next = self.head
        else:
            node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.head.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = node
        node.next = self.head
        return

    def insert_at_any_position(self, data, position):
        node = Node(data)
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head
            self.head = node
            return

        index = 0
        current = self.head
        while index < position and current.next != self.head:
            current = current.next
            index += 1
        if index < position - 1:
            print("Position out of range")
            return
        node.next = current.next
        current.next = node
        return

    def delete_at_beginning(self):
        if not self.head:
            print(f"List is empty")
            return
        elif self.head == self.head.next:
            self.head = None
            return
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head
        return

    def delete_at_any_position(self, position):
        if not self.head:
            print("List is empty")
            return
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        current = self.head
        index = 0
        while index < position - 1 and current.next != self.head:
            current = current.next
            index += 1

        if current.next == self.head or current.next.next == self.head and position > index + 1:
            print("Position out of range")
            return

        current.next = current.next.next

    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break


circular_list = CircularLinkedList()
circular_list.insert_at_end(3)
circular_list.insert_at_beginning(2)
circular_list.insert_at_any_position(1, 0)

circular_list.display()
