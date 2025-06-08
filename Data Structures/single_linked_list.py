class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def print_linked_list(self):
        while self.head is not None:
            print(f"{self.head.data}")
            self.head = self.head.next

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def search(self, target):
        current = self.head
        position = 0

        while current:
            if current.data == target:
                return print(f"{target} found at position {position}")
            position += 1
            current = current.next
        return print(f"{target} not found")


llist = SingleLinkedList()
llist.insert_at_beginning("world")
llist.insert_at_beginning("Hello")
llist.insert_at_end("!")
llist.search("Hello")
