import sys

min_num = sys.maxsize

num = input()
while num != "Stop":
    current_num = int(num)
    if current_num < min_num:
        min_num = current_num
    num = input()
print(min_num)