import sys

# Implements a min-heap data structure using a list
class MinHeap:
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def sift_up(self, index):
        if not isinstance(index, int): raise Exception("invalid index")
        if not 0 <= index < self.size: raise Exception("out of range index")
        if self.size == 0: raise Exception("empty")
        
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap_list[index] < self.heap_list[parent_index]:
                self.heap_list[index], self.heap_list[parent_index] = self.heap_list[parent_index], self.heap_list[index]
                index = parent_index
            else:
                break

    def sift_down(self, index):
        if not isinstance(index, int): raise Exception("invalid index")
        if not 0 <= index < self.size: raise Exception("out of range index")
        if self.size == 0: raise Exception("empty")

        while (2 * index + 1) < self.size:
            left_child_idx = 2 * index + 1
            right_child_idx = 2 * index + 2
            min_child_idx = left_child_idx

            if right_child_idx < self.size and self.heap_list[right_child_idx] < self.heap_list[left_child_idx]:
                min_child_idx = right_child_idx
            
            if self.heap_list[index] > self.heap_list[min_child_idx]:
                self.heap_list[index], self.heap_list[min_child_idx] = self.heap_list[min_child_idx], self.heap_list[index]
                index = min_child_idx
            else:
                break

    def push(self, value):
        self.heap_list.append(value)
        self.size += 1
        self.sift_up(self.size - 1)
    
    def pop(self):
        if self.size == 0: raise Exception("empty")
        
        self.heap_list[0], self.heap_list[self.size - 1] = self.heap_list[self.size - 1], self.heap_list[0]
        min_val = self.heap_list.pop()
        self.size -= 1
        
        if self.size > 0:
            self.sift_down(0)
        return min_val
        
    def heapify(self, *args):
        for val in args:
            self.push(val)

# Builds a Huffman Tree for character encoding
class HuffmanTree:
    class Node:
        def __init__(self, freq, char=None, parent=None, left=None, right=None):
            self.freq = freq
            self.char = char
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.letters = []
        self.frequencies = []
        self.codes = {}
        self.root = None

    def set_letters(self, *args):
        self.letters.extend(list(args))

    def set_repetitions(self, *args):
        self.frequencies.extend(list(args))

    def build_tree(self):
        char_freq_pairs = sorted(zip(self.letters, self.frequencies), key=lambda x: x[1], reverse=True)
        nodes = [self.Node(freq, char) for char, freq in char_freq_pairs]
        
        while len(nodes) > 1:
            left_node = nodes.pop()
            right_node = nodes.pop()
            
            new_node = self.Node(left_node.freq + right_node.freq, left=left_node, right=right_node)
            left_node.parent = right_node.parent = new_node
            
            # Keeps the list sorted
            is_inserted = False
            for i in range(len(nodes)):
                if nodes[i].freq < new_node.freq:
                    nodes.insert(i, new_node)
                    is_inserted = True
                    break
            if not is_inserted:
                nodes.append(new_node)
        
        self.root = nodes[0] if nodes else None
        self._generate_codes_recursive(self.root)

    def _generate_codes_recursive(self, node, current_code=""):
        if node is None: return
        if node.char is not None:
            self.codes[node.char] = current_code
            return
        self._generate_codes_recursive(node.left, current_code + "0")
        self._generate_codes_recursive(node.right, current_code + "1")

    def get_huffman_code_cost(self):
        total_cost = 0
        char_freq_map = dict(zip(self.letters, self.frequencies))
        for char, code in self.codes.items():
            total_cost += char_freq_map[char] * len(code)
        return total_cost

# Implements a basic Binary Search Tree
class Bst:
    class Node:
        def __init__(self, value, parent=None):
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.print_buffer = ""

    def insert(self, key, current_node=None, parent_node=None, is_first_call=True):
        if is_first_call:
            current_node = self.root

        if self.root is None:
            self.root = self.Node(key)
            return

        if current_node is None:
            new_node = self.Node(key, parent_node)
            if key < parent_node.value:
                parent_node.left = new_node
            else:
                parent_node.right = new_node
            return

        if key < current_node.value:
            self.insert(key, current_node.left, current_node, False)
        else:
            self.insert(key, current_node.right, current_node, False)

    def inorder(self, current_node=None, is_first_call=True):
        if is_first_call:
            self.print_buffer = ""
            current_node = self.root
        
        if current_node is None:
            return
        
        self.inorder(current_node.left, False)
        self.print_buffer += str(current_node.value) + ' '
        self.inorder(current_node.right, False)
        
        if is_first_call:
            print(self.print_buffer.strip())

# This class reads and executes commands on the data structures
class CommandRunner:
    DS_CLASSES = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}

    def __init__(self, input_source):
        self.commands = input_source
        self.instances = {}

    def run(self):
        for line in self.commands:
            line = line.strip()
            parts = line.partition(' ')
            command, params = parts[0], parts[2]
            
            if command == "make":
                self.make_instance(params)
            elif command == "call":
                self.call_method(params)

    def make_instance(self, params):
        item_type, item_name = params.split()
        self.instances[item_name] = self.DS_CLASSES[item_type]()

    def call_method(self, params):
        # Parse the _object.method(args)_ command
        obj_name, rest = params.split('.', 1)
        method_name, args_part = rest.split('(', 1)
        args_str = args_part[:-1]

        raw_args = args_str.split(',') if args_str else []
        final_args = []
        for arg in raw_args:
            arg = arg.strip()
            if (arg.startswith('"') and arg.endswith('"')) or \
               (arg.startswith("'") and arg.endswith("'")):
                final_args.append(arg[1:-1])
            else:
                final_args.append(int(arg))
        
        instance = self.instances[obj_name]
        method = getattr(instance, method_name)
        try:
            result = method(*final_args)
            if result is not None:
                print(result)
        except Exception as e:
            print(e)

def main():
    runner = CommandRunner(sys.stdin)
    runner.run()

if __name__ == "__main__":
    main()