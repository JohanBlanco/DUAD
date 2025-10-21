class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self,data):
        new_node = Node(data=data)
        if self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
        else:
            self.head = new_node

    def dequeue(self):
        if self.head is not None:
            self.head = self.head.next

    def print_queue(self):
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
    queue = Queue()
    queue.print_queue()
    queue.enqueue(1)
    queue.print_queue()
    queue.enqueue(2)
    queue.print_queue()
    queue.enqueue(3)
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()