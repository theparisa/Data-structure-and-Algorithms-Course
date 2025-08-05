class PathTree:
    class Node:
        def __init__(self, value, parent_node):
            self.value = value
            self.parent = parent_node
            self.children = []

            # Stores each node's full path from the root
            if parent_node is None:
                self.path_from_root = [value]
            else:
                self.path_from_root = [value] + parent_node.path_from_root

    def __init__(self):
        self.root = None

        # For fast lookup, maps a node value to its Node object 
        self.node_map = {}

    def add_node(self, value, parent_value=None):
        if parent_value is None:
            new_node = self.Node(value, None)
            self.root = new_node
            self.node_map[value] = new_node
            return
        
        parent_node = self.node_map[parent_value]
        new_node = self.Node(value, parent_node)
        parent_node.children.append(new_node)
        self.node_map[value] = new_node

def main():
    edges, visit_order, node_count = read_problem_input()
    
    tree = build_tree(edges)
    final_path = find_tour(tree, visit_order, node_count)
    
    if final_path == -1:
        print(-1)
    else:
        print(*final_path)

def find_tour(tree, visit_order, node_count):

    tour_path = []
    for i in range(len(visit_order) - 1):
        start_node = visit_order[i]
        end_node = visit_order[i+1]
        
        path_segment = find_path_between_nodes(tree, start_node, end_node)
        
        if i == 0:
            tour_path = path_segment
        else:
            tour_path.extend(path_segment[1:])

        if len(tour_path) > 2 * node_count - 1:
            return -1
    
    if tour_path:
        tour_path.pop() 
    return tour_path

def find_path_between_nodes(tree, start_val, end_val):
    path_a = tree.node_map[start_val].path_from_root
    path_b = tree.node_map[end_val].path_from_root
    
    lca_val = find_lca(path_a, path_b)
    
    way_to_lca_a = get_path_to_ancestor(lca_val, path_a)
    way_to_lca_b = get_path_to_ancestor(lca_val, path_b)

    return way_to_lca_a + [lca_val] + list(reversed(way_to_lca_b))

def get_path_to_ancestor(ancestor_val, child_path):
    for i in range(len(child_path)):
        if ancestor_val == child_path[i]:
            return child_path[:i]

def find_lca(path_a, path_b):
    
    # Finds the lowest common ancestor from two paths
    len_a, len_b = len(path_a), len(path_b)
    for i in range(1, min(len_a, len_b) + 1):
        if path_a[-i] != path_b[-i]:
            return path_a[-i + 1]
            
    return path_a[0] if len_a < len_b else path_b[0]

def build_tree(edges):
    tree = PathTree()
    for u, v in edges:
        if tree.root is None:
            tree.add_node(u)
        tree.add_node(v, u)
    return tree

def read_problem_input():
    
    # The tour starts and ends at the node 1
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    query_path = [1] + list(map(int, input().split())) + [1]
    return edges, query_path, n
    
if __name__ == "__main__":
    main()