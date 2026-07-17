import sys

def solve():
    input_func = sys.stdin.readline
    
    try:
        first_line = input_func().strip()
        if not first_line:
            return
            
        n = int(first_line)
        start_times = list(map(int, input_func().split()))
        end_times = list(map(int, input_func().split()))
        meetings = list(zip(start_times, end_times))
        meetings.sort(key=lambda x: (x[1], x[0]))
        
        max_meetings = 1
        last_end_time = meetings[0][1]
        
        for i in range(1, n):
            if meetings[i][0] >= last_end_time:
                max_meetings += 1
                last_end_time = meetings[i][1]
                
        print(max_meetings)
        
    except Exception:
        pass

if __name__ == '__main__':
    solve()