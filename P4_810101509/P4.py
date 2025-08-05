from collections import deque

def main():
    problem_data = read_input()
    result = solve_path(problem_data)
    print(result)

# Uses a 0-1 BFS to find the shortest path
def solve_path(data):
    queue = deque([(0, data['start'])])
    active_cells = set(data['cells'])
    active_cells.add(data['start'])
    
    end_is_active = data['finish'] in active_cells
    
    while queue:
        cost, pos = queue.popleft()
        
        if pos not in active_cells:
            continue
        active_cells.remove(pos) 

        # Finds all reachable cells
        neighbors = find_all_neighbors(pos, active_cells)
        
        push_neighbors_to_queue(cost, neighbors, queue)
        
        is_done, final_cost = check_if_finished(cost, pos, data['finish'], end_is_active)
        if is_done:
            return final_cost

    return -1

def find_all_neighbors(pos, active_cells):
    # Cost-0 moves : to _close_ cells
    component = find_connected_component(pos, active_cells)
    
    # Cost-1 moves : to _far_ cells
    extended_neighbors = find_extended_neighbors(component + [pos], active_cells)
    
    return [(c, 0) for c in component] + [(c, 1) for c in extended_neighbors]

def find_connected_component(start_pos, active_cells):
    component = []
    q = [start_pos]
    visited_in_comp = {start_pos}

    while q:
        pos = q.pop(0)
        for cell in active_cells:
            if cell not in visited_in_comp and is_strict_diagonal(pos, cell):
                visited_in_comp.add(cell)
                q.append(cell)
                component.append(cell)
    return component

def find_extended_neighbors(component_cells, active_cells):
    extended = []
    for cell in active_cells:
        is_near_component = False
        for comp_cell in component_cells:
            if is_broadly_near(cell, comp_cell):
                is_near_component = True
                break
        if is_near_component:
            extended.append(cell)
    return extended

def is_strict_diagonal(p1, p2):
    return abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 1

def is_broadly_near(p1, p2):
    return abs(p1[0] - p2[0]) <= 2 or abs(p1[1] - p2[1]) <= 2

def is_king_move_adjacent(p1, p2):
    return abs(p1[0] - p2[0]) <= 1 and abs(p1[1] - p2[1]) <= 1

def check_if_finished(cost, pos, end_pos, end_is_active):
    if end_is_active:
        if pos == end_pos:
            return True, cost
    elif is_king_move_adjacent(pos, end_pos):
        return True, cost + 1
            
    return False, None

# Pushes new states to the deque for 0-1 BFS
def push_neighbors_to_queue(cost, neighbors, queue):
    for neighbor_pos, cost_increase in neighbors:
        if cost_increase == 0:
            queue.appendleft((cost, neighbor_pos))
        else:
            queue.append((cost + 1, neighbor_pos))

def read_input():
    n, m, k = map(int, input().split())
    cells = set()
    for _ in range(k):
        cells.add(tuple(int(p) - 1 for p in input().split()))
    if (0,0) in cells:
        cells.remove((0,0))
    return {
        'n': n, 'm': m, 'k': k,
        'cells': list(cells),
        'start': (0,0),
        'finish': (n-1, m-1)
    }

if __name__ == "__main__":
    main()