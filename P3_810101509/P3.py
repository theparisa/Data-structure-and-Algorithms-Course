from heapq import heappop, heappush

def main():
    total_days, teacher_list = read_data()
    
    teacher_list.sort(key=lambda t: t["start"])
    
    priority_queue = []
    teacher_index = 0
    
    for day in range(1, total_days + 1):
        while teacher_index < len(teacher_list) and teacher_list[teacher_index]["start"] <= day:
            teacher = teacher_list[teacher_index]
            
            # Uses negative anger to simulate a max-heap
            heappush(priority_queue, [-teacher["anger"], teacher["lectures"]])
            teacher_index += 1
        
        if not priority_queue:
            continue
        
        # Assigns one lecture to the _angriest_ one
        priority_queue[0][1] -= 1
        
        if priority_queue[0][1] == 0:
            heappop(priority_queue)
        
    remaining_anger = 0
    for anger_val, lectures_left in priority_queue:
        remaining_anger += -anger_val * lectures_left
    
    print(remaining_anger)
        
def read_data():
    count, days = [int(i) for i in input().split(' ')]
    
    teachers = []
    for _ in range(count):
        new_teacher_data = input().split(' ')
        teachers.append({
            "start" : int(new_teacher_data[0]),
            "lectures" : int(new_teacher_data[1]),
            "anger" : int(new_teacher_data[2]),
        })

    return days, teachers

if __name__ == "__main__":
    main()