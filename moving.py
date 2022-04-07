width = int(input())
length = int(input())
height = int(input())

all_place = width * length * height

used_place = 0
house_is_full = False

command = input()

while command != "Done":
    current_boxes = int(command)
    used_place += current_boxes
    if used_place > all_place:
        house_is_full = True
        break
    command = input()

difference = abs(all_place - used_place)
if house_is_full:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")