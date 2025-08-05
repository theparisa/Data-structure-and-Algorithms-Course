# Toggles the parity bit for a given character
def update_parity_map(parity_map, character):
    char_index = ord(character) - ord('a')
    parity_map[char_index] ^= 1
    return parity_map

source_string = input()

palindrome_substring_count = 0
current_char_parity = [0] * 10

# Stores the frequency of each parity pattern
parity_map_frequencies = {}

for char in source_string:
    current_char_parity = update_parity_map(current_char_parity, char)
    current_parity_tuple = tuple(current_char_parity)

    if current_parity_tuple.count(1) <= 1:
        palindrome_substring_count += 1

    # Count substrings based on previous matching parity maps
    if current_parity_tuple in parity_map_frequencies:
        palindrome_substring_count += parity_map_frequencies[current_parity_tuple]
        parity_map_frequencies[current_parity_tuple] += 1
    else:
        parity_map_frequencies[current_parity_tuple] = 1

    for i in range(len(current_parity_tuple)):
        flipped_list = list(current_parity_tuple)
        flipped_list[i] ^= 1
        flipped_tuple = tuple(flipped_list)

        if flipped_tuple in parity_map_frequencies:
            palindrome_substring_count += parity_map_frequencies[flipped_tuple]

print(palindrome_substring_count)