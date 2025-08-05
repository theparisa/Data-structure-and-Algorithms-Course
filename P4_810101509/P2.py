from itertools import permutations

def main():
    num_elements, num_queries, query_list = read_inputs()
    
    # Calculates all distances using BFS
    all_distances = precompute_all_distances(num_elements)
    
    for query in query_list:
        print(all_distances[query])

def precompute_all_distances(n):
    distances = initialize_distance_map(n)
    
    sorted_permutation = tuple(range(n))
    distances[sorted_permutation] = 0
    
    queue = [sorted_permutation]
    run_bfs(queue, n, distances)
    
    return distances

def run_bfs(queue, n, distances):
    while len(queue) > 0:
        current_perm = queue.pop(0)
        
        for i in range(n + 1):
            for j in range(i + 2, n + 1):
                
                new_perm = reverse_sub_permutation(current_perm, i, j)
                
                if distances[new_perm] == -1:
                    distances[new_perm] = distances[current_perm] + 1
                    queue.append(new_perm)

def reverse_sub_permutation(p_tuple, start, end):
    p_list = list(p_tuple)
    sub_list = p_list[start:end]
    sub_list.reverse()
    p_list[start:end] = sub_list
    return tuple(p_list)
    
def initialize_distance_map(n):
    # Generates all possible permutation states
    elements = range(n)
    return {p: -1 for p in permutations(elements)}
        
def read_inputs():
    n = int(input())
    t = int(input())
    
    queries = []
    for _ in range(t):
        start_str, end_str = input().split()
        query_tuple = standardize_permutation(n, start_str, end_str)
        queries.append(query_tuple)
    
    return n, t, queries

def standardize_permutation(n, start_str, end_str):
    
    # Convert character permutations to an integer tuple
    char_to_pos = {end_str[i]: i for i in range(n)}
    return tuple(char_to_pos[char] for char in start_str)

if __name__ == "__main__":
    main()