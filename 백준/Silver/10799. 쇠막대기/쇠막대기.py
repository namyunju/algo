import sys

input_str = sys.stdin.readline().strip()

stack_count = 0  
total_pieces = 0 

for i in range(len(input_str)):
    if input_str[i] == '(':
        stack_count += 1
    else: 
        stack_count -= 1
        if input_str[i-1] == '(': 
            total_pieces += stack_count
        else:
            total_pieces += 1

print(total_pieces)