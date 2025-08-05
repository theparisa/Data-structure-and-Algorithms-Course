def main():
    inputs = read_inputs()
    colors = inputs["list"]
    
    color_spans = get_color_spans(colors)
    
    max_depth = calculate_depth(colors, color_spans)
    print(max_depth)

def calculate_depth(colors, spans):
    stack = []
    open_ranges = 0
    nesting_level = 0

    for i, color in enumerate(colors):

        # A '0' cannot be inside another color's range
        if color == 0 and len(stack) != 0:
            return -1
        elif color == 0:
            continue

        start_pos, end_pos = spans[color]

        if start_pos == end_pos:           # A single-block 
            if open_ranges == nesting_level:
                nesting_level += 1
        elif i == end_pos:                 # End 
            open_ranges -= 1
            is_valid = pop_and_validate(stack, start_pos, color)
            if not is_valid:
                return -1
        elif i == start_pos:               # Start 
            stack.append((color, i))
            if open_ranges == nesting_level:
                nesting_level += 1
            open_ranges += 1
        else:                              # Middle 
            stack.append((color, i))

    return nesting_level

def pop_and_validate(stack, start_index, current_color):
    while True:
        if not stack:
            return True 
        
        top_item = stack[-1]

        if top_item[1] == start_index:
            stack.pop()
            return True
        
        # Checks if inner blocks are of the same color
        if top_item[0] != current_color:
            return False
        
        stack.pop()
            
def get_color_spans(colors):
    spans = {}
    for i, color_val in enumerate(colors):
        if color_val == 0:
            continue
        if color_val not in spans:
            spans[color_val] = [i, i]
        else:
            spans[color_val][1] = i
    return spans

def read_inputs():
    data = {}
    data["count"] = int(input())
    data["list"] = []
    for _ in range(data["count"]):
        data["list"].append(int(input()))
    return data

if __name__ == "__main__":
    main()