def main():
    inputs = read_inputs()
    path_heights = inputs["path"]
    shoe_queries = inputs["shoes"]

    # Finds a max _jump_ length for each height
    precomputed_values = preprocess_path(path_heights)
    
    path_data = combine_data(precomputed_values, path_heights)
    
    results = answer_shoe_queries(shoe_queries, path_data)
    
    for r in results:
        print(r)

def answer_shoe_queries(shoes, path_data):
    sorted_shoes = sorted(shoes, key=lambda t: t[0])
    
    results = [0] * len(shoes)
    path_idx = 0

    for shoe_d, shoe_s, original_idx in sorted_shoes:
        while path_idx < len(path_data) and path_data[path_idx][0] <= shoe_d:
            path_idx += 1
            
        can_use_shoe = False
        if path_idx >= len(path_data):
            can_use_shoe = True
        elif shoe_s > path_data[path_idx][1]:
            can_use_shoe = True

        if can_use_shoe and shoe_s > 0:
            results[original_idx] = 1
            
    return results

def combine_data(values, path):
    sorted_path = sorted(path)
    combined = []
    for i in range(len(values)):
        combined.append([sorted_path[i], values[i]])
    return combined

def preprocess_path(path):
    path_len = len(path)
    left_smaller = find_prev_smaller(path, -1)
    
    right_smaller_rev = find_prev_smaller(list(reversed(path)), -1)
    for i in range(len(right_smaller_rev)):
        if right_smaller_rev[i] == -1:
            right_smaller_rev[i] = path_len
        else:
            right_smaller_rev[i] = path_len - 1 - right_smaller_rev[i]
    
    right_smaller = list(reversed(right_smaller_rev))

    lengths = []
    for i in range(path_len):
        lengths.append(right_smaller[i] - left_smaller[i] - 1)

    sorted_path_pairs = sorted([[path[i], i] for i in range(path_len)], key=lambda t: t[0]) 
    
    # Calculates a running maximum 
    max_val = -2
    output_values = []
    for i in range(path_len - 1, -1, -1):
        original_idx = sorted_path_pairs[i][1]
        max_val = max(max_val, lengths[original_idx])
        output_values.append(max_val)

    return list(reversed(output_values))

# Finds the index of the previous smaller element
def find_prev_smaller(items, default_val):
    results = []
    stack = []
    for i in range(len(items)):
        while True:
            if not stack:
                results.append(default_val)
                if i < len(items)-1 and items[i] < items[i+1]:
                    stack.append([items[i], i])
                break
            if stack[-1][0] < items[i]: 
                results.append(stack[-1][1])
                if i < len(items)-1 and items[i] < items[i+1]:
                    stack.append([items[i], i])
                break
            else:
                stack.pop()
    return results

def read_inputs():
    data = {}
    n, b = [int(i) for i in input().split(" ")]
    data["path"] = [int(i) for i in input().split(" ")]
    data["shoes"] = []
    for i in range(b):
        data["shoes"].append([*[int(i) for i in input().split(" ")], i])
    return data

if __name__ == "__main__":
    main()