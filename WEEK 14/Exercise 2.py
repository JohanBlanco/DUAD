class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class DoubleEndedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data=data)
        if self.head is not None:
            new_node.next = self.head
            new_node.next.previous = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = self.head

    def push_right(self, data):
        new_node = Node(data=data)
        if self.tail is not None:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = self.head

    def pop_left(self):
        if self.head is not None:
            self.head = self.head.next

    def pop_right(self):
        if self.tail is not None:
            self.tail = self.tail.previous
            self.tail.next = None

    def print_structure(self):
        string = '['
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                string += f'{current_node.data}, '
                current_node = current_node.next

            string = string[:-2]
            string += ']'
            print(string)
        else:
            print('[]')
            

if __name__ == '__main__':
    queue = DoubleEndedQueue()
    queue.print_structure()
    queue.push_left(3)
    queue.print_structure()
    queue.push_left(2)
    queue.print_structure()
    queue.push_left(1)
    queue.print_structure()
    queue.push_right(4)
    queue.print_structure()
    queue.push_right(5)
    queue.print_structure()
    queue.push_right(6)
    queue.print_structure()
    queue.pop_left()
    queue.print_structure()
    queue.pop_right()
    queue.print_structure()
    queue.pop_left()
    queue.print_structure()
    queue.pop_left()
    queue.print_structure()
    queue.pop_right()
    queue.print_structure()
    queue.pop_left()
    queue.print_structure()
    queue.pop_right()
    queue.pop_left()