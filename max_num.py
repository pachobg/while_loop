import sys

max_number = -sys.maxsize

num = input()
while num != "Stop":
    current = int(num)
    if current > max_number:
        max_number = current
    num = input()
print(max_number)
