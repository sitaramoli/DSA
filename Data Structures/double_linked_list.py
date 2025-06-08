class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        if not self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            node.prev = temp

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None
            current.prev = None

    def search(self, target):
        current_node = self.head
        current_position = 0
        while current_node:
            if current_node.data == target:
                print(f"{target} found at position {current_position}")
                return
            current_node = current_node.next
            current_position += 1
        print(f"{target} not found")
        return

    def __str__(self):
        node = self.head
        linked_list = ""
        while node:
            linked_list += f"{node.data}"
            node = node.next
        return linked_list


llist = DoubleLinkedList()
llist.insert_at_end("!")
llist.insert_at_beginning("World")
llist.delete_at_end()
llist.insert_at_beginning("Hello")
llist.insert_at_beginning("!")
llist.delete_at_beginning()
llist.delete_at_end()

print(llist)
