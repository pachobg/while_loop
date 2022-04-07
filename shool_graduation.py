name = input()

fails = 0
grade_sum = 0
stage = 1
is_expelled = False
while stage <= 12:
    grade = float(input())

    if grade < 4:
        fails += 1
        if fails > 1:
            is_expelled = True
            break
    else:
        stage += 1
        grade_sum += grade

if is_expelled:
    print(f"{name} has been excluded at {stage} grade")
else:
    average = grade_sum / 12
    print(f"{name} graduated. Average grade: {average:.2f}")