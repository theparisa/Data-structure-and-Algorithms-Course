class Node:
    def __init__(self, value):
        self.value = value
        self.group = None
        self.neighbors = []

def main():
    graph_data = read_graph_input()
    
    is_possible, graph_nodes = solve_grouping(graph_data)
    
    if not is_possible:
        print(-1)
        return
    
    group_one = []
    for node_id in sorted(graph_nodes.keys()):
        if graph_nodes[node_id].group == 1:
            group_one.append(node_id)
            
    print(len(group_one))
    print(*group_one)

def solve_grouping(graph_data):
    nodes = build_graph(graph_data["vertex_count"], graph_data["edges"])
    
    # Assigns every node to a group
    for node_id in sorted(nodes.keys()):
        node = nodes[node_id]
        if node.group is None:
            
            # Greedily assign to group 1
            node.group = 1 
        
        opposite_group = 2 if node.group == 1 else 1
        
        for neighbor in node.neighbors:
            if neighbor.group is None:
                neighbor.group = opposite_group

            # Checks for conflict with neighbors
            elif neighbor.group == node.group:
                return False, nodes 
                
    return True, nodes

def build_graph(vertex_count, edges):
    
    # Creates nodes and links them together
    nodes = {i + 1: Node(i + 1) for i in range(vertex_count)}
    for u, v in edges:
        nodes[u].neighbors.append(nodes[v])
        nodes[v].neighbors.append(nodes[u])
    return nodes

def read_graph_input():
    data = {}
    data["vertex_count"], data["edge_count"] = map(int, input().split())

    data["edges"] = []
    for _ in range(data["edge_count"]):
        edge = list(map(int, input().split()))
        data["edges"].append(edge)
        
    return data
    
if __name__ == "__main__":
    main()