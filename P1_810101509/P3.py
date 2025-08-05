input_string = input()

max_length = 0
# _start_index_ : the left boundary of our current substring
start_index = 0

for end_index in range(len(input_string)):
    current_window = input_string[start_index:end_index]
    current_char = input_string[end_index]

    if current_char in current_window:
        # If the char is repeated, move the start of the window forward
        repeated_char_index = current_window.find(current_char)
        start_index = start_index + repeated_char_index + 1

    current_length = end_index - start_index + 1
    if current_length > max_length:
        max_length = current_length

print(max_length)