import copy

def main():
    number_string = input()
    is_additive = is_an_additive_sequence(number_string)
    print("YES" if is_additive else "NO")

def check_remaining_string(s, sequence_so_far):
    # Makes a copy to safely modify the sequence
    current_sequence = copy.deepcopy(sequence_so_far)
    
    while len(s) > 0:
        expected_sum = str(current_sequence[-2] + current_sequence[-1])
        
        if s.startswith(expected_sum):
            current_sequence.append(int(expected_sum))
            s = s[len(expected_sum):]
        else:
            return False
            
    return True

def is_an_additive_sequence(s):
    n = len(s)

    # Tries every possible first and second number
    for i in range(1, n):
        for j in range(1, n - i):
            num1_str = s[:i]
            num2_str = s[i : i+j]

            if (len(num2_str) > 1 and num2_str.startswith('0')):
                continue

            starting_pair = [int(num1_str), int(num2_str)]
            remaining_str = s[i+j:]

            if check_remaining_string(remaining_str, starting_pair):
                return True
    
    return False

if __name__ == "__main__":
    main()