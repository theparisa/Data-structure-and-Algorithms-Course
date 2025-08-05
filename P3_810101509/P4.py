def main():
    tree_data = read_input_data()
    
    for query in tree_data["queries"]:
        result = process_query(tree_data, query)
        print(result)

def process_query(tree_data, query_nodes):
    # Sums nodes and their children
    total_score = 0
    parent_map = tree_data["parent_map"]
    
    parents_of_queried_nodes = {}
    for node in query_nodes:
        parent = parent_map.get(node)
        if parent is not None:
            parents_of_queried_nodes[parent] = 0

    for node in query_nodes:
        total_score += tree_data["child_counts"][node] + 1
        parent = parent_map.get(node)
        if parent in parents_of_queried_nodes:
            parents_of_queried_nodes[parent] += 1

    for node in set(query_nodes).intersection(parents_of_queried_nodes.keys()):
        total_score -= 2 * parents_of_queried_nodes[node]
        
    return total_score
  
def read_input_data():
    data = {}
    num_nodes, num_queries = map(int, input().split())
    parent_list = list(map(int, input().split()))
    
    # Maps each node to its parent
    parent_map = {i + 2: parent_list[i] for i in range(num_nodes - 1)}
    parent_map[1] = 0 
    
    child_counts = {i + 1: 0 for i in range(num_nodes)}
    for parent in parent_map.values():
        if parent != 0:
            child_counts[parent] += 1
        
    queries = []
    for _ in range(num_queries):
        queries.append(list(map(int, input().split()))[1:])
    
    data["parent_map"] = parent_map
    data["child_counts"] = child_counts
    data["queries"] = queries
    return data

if __name__ == "__main__":
    main()