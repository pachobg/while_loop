number_of_fails = int(input())

total_fail = False
number_of_task = 0
fail_count = 0
grade_sum = 0
last_task = ""

task_name = input()
while task_name != "Enough":
    grade = int(input())
    if grade <= 4:
        fail_count += 1
        if fail_count == number_of_fails:
            total_fail = True
            break
    grade_sum += grade
    number_of_task += 1
    last_task = task_name
    task_name = input()

average_grade = grade_sum / number_of_task

if total_fail:
    print(f"You need a break, {fail_count} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {number_of_task}")
    print(f"Last problem: {last_task}")

