class PathTrackingBST:
    class Node:
        def __init__(self, value, parent, insert_id):
            self.value = value
            self.parent = parent
            self.insert_id = insert_id
            self.left = None
            self.right = None
            
            # Stores each node's full path from the root
            if parent is None:
                self.path_from_root = [(value, insert_id)]
            else:
                self.path_from_root = [(value, insert_id)] + parent.path_from_root

    def __init__(self):
        self.node_counter = 0
        self.root = None

    def add(self, value, current=None, parent=None, is_first_call=True):
        if is_first_call:
            current = self.root
            
        if self.root is None:
            self.node_counter += 1
            self.root = self.Node(value, None, self.node_counter)
            return self.root.path_from_root

        if current is None:
            self.node_counter += 1
            new_node = self.Node(value, parent, self.node_counter)
            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
            return new_node.path_from_root
        
        if value < current.value:
            return self.add(value, current.left, current, False)
        else:
            return self.add(value, current.right, current, False)
        
def main():
    tree = PathTrackingBST()
    problem_data = read_problem_data()
    
    all_node_paths = []
    for val in problem_data["bst_values"]:
        path = tree.add(val)
        all_node_paths.append(path)
    
    # Prints the parent of each new node
    parent_values_to_print = []
    for i in range(1, len(all_node_paths)):
        parent_info = all_node_paths[i][1]
        parent_values_to_print.append(str(parent_info[0]))
    print(" ".join(parent_values_to_print))
            
    # Finds the lowest common ancestor
    node1_idx = problem_data["query_indices"][0] - 1
    node2_idx = problem_data["query_indices"][1] - 1
    
    path_a = set(all_node_paths[node1_idx])
    path_b = set(all_node_paths[node2_idx])
    
    common_ancestors = list(path_a.intersection(path_b))
    common_ancestors.sort(key=lambda item: item[1])
    
    lca_node = common_ancestors[-1]
    print(lca_node[1])
            
def read_problem_data():
    data = {}
    # Skip the first line
    input() 
    data["bst_values"] = [int(i) for i in input().split()]
    data["query_indices"] = [int(i) for i in input().split()]
    return data
    
if __name__ == "__main__":
    main()