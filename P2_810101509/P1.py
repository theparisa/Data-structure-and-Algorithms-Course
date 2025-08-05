import sys

class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def add(self, value):
        self.items.append(value)

    def remove(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.size() == 0

    def to_string(self):
        return " ".join(str(item) for item in self.items)

# A basic array-based stack with a fixed initial size
class Stack:
    def __init__(self, size=10):
        self.storage = [0] * size
        self.top = -1

    def is_empty(self):
        return self.top < 0

    def push(self, value):
        if self.top + 1 >= len(self.storage):
            self.expand()
        self.top += 1
        self.storage[self.top] = value

    def pop(self):
        val = self.storage[self.top]
        self.top -= 1
        return val

    def peek(self):
        return self.storage[self.top]

    def expand(self):
        self.storage.extend([0] * len(self.storage))

    def to_string(self):
        if self.is_empty():
            return ""
        return " ".join(str(self.storage[i]) for i in range(self.top + 1))

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_string(self):
        output = ""
        current = self.head
        while current is not None:
            output += str(current.val) + " "
            current = current.next
        return output.strip()

    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node

# This class reads and runs commands on the data structures
class CommandRunner:
    DS_CLASSES = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}

    def __init__(self, command_source):
        self.commands = command_source
        self.instances = {}

    def process_commands(self):
        for line in self.commands:
            line = line.strip()
            parts = line.split(' ', 1)
            command = parts[0]
            params = parts[1] if len(parts) > 1 else ""

            if command == "make":
                self.create_ds(params)
            elif command == "call":
                self.execute_call(params)

    def create_ds(self, params):
        ds_type, instance_name = params.split()
        self.instances[instance_name] = self.DS_CLASSES[ds_type]()

    def execute_call(self, params):
        # Parses the _object.method(args)_
        obj_name, method_call = params.split('.', 1)
        method_name, args_part = method_call.split('(', 1)
        args_str = args_part[:-1]

        args = []
        if args_str:
            args = args_str.split(',')

        instance = self.instances[obj_name]
        method_to_call = getattr(instance, method_name)
        
        result = method_to_call(*args)
        if result is not None:
            print(result)

def main():
    runner = CommandRunner(sys.stdin)
    runner.process_commands()

if __name__ == "__main__":
    main()