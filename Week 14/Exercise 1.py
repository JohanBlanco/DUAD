class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data=data)
        if self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
        else:
            self.head = new_node

    def pop(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                current_node = self.head
                while current_node.next.next is not None:
                    current_node = current_node.next

                current_node.next = None

    def print_stack(self):
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
    stack = Stack()
    stack.print_stack()
    stack.push(1)
    stack.print_stack()
    stack.push(2)
    stack.print_stack()
    stack.push(3)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.pop()
    stack.print_stack()