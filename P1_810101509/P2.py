# Converts time string to total minutes
def convert_time_to_minutes(time_str: str) -> int:
    time_part, meridiem = time_str.split(" ")
    hour_str, minute_str = time_part.split(":")
    
    hour = int(hour_str)
    minute = int(minute_str)
    
    meridiem_offset = 12 * 60 if meridiem == "PM" else 0
    
    # Normalizes 12 o'clock hours
    if hour == 12:
        hour = 0
        
    return (hour * 60) + minute + meridiem_offset

def is_in_range(reference: int, start: int, end: int) -> bool:
    return start <= reference <= end

def main():
    try:
        num_test_cases = int(input())
    except (ValueError, EOFError):
        return

    full_output = ""
    for _ in range(num_test_cases):
        reference_time = convert_time_to_minutes(input())
        num_ranges_to_check = int(input())
        
        result_line = ""
        for _ in range(num_ranges_to_check):
            time_range = input()
            start_time = convert_time_to_minutes(time_range[:8])
            end_time = convert_time_to_minutes(time_range[9:])
            
            if is_in_range(reference_time, start_time, end_time):
                result_line += "1"
            else:
                result_line += "0"
        
        full_output += result_line + "\n"

    print(full_output, end="")

if __name__ == "__main__":
    main()