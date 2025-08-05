n = int(input())
input_numbers = [int(i) for i in input().split(" ")]

# Maps each number to its original position in the list
positions = {}
for i in range(0, n):
    num = input_numbers[i]
    positions[num] = i

# Pre-calculate a _target position_ for each number
target_pos_map = {}
processing_stack = []

for i in range(n, 0, -1):
    current_pos = positions[i]
    while processing_stack and processing_stack[-1] >= current_pos:
        processing_stack.pop()
    
    if not processing_stack:
        target_pos_map[i] = -1
    else:
        target_pos_map[i] = processing_stack[-1]
    
    processing_stack.append(current_pos)


main_stack = []
print("0")

for i in range(1, n + 1):
    target_pos = target_pos_map[i]
    
    while True:
        if target_pos == -1:
            main_stack.clear()
            print(len(main_stack))
            break
        elif not main_stack:
            main_stack.append(positions[i])
            print(len(main_stack))
            break
        else:
            if main_stack[-1] == target_pos:
                print(len(main_stack))
                break
            elif main_stack[-1] < target_pos:
                main_stack.append(target_pos)
                print(len(main_stack))
                break
            else: 
                # main_stack[-1] > target_pos
                main_stack.pop()