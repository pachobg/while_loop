width = int(input())
length = int(input())

cake_peaces = width * length
cake_is_over = False
command = input()
while command != "STOP":
    current_number_peaces = int(command)
    cake_peaces -= current_number_peaces
    if cake_peaces < 0:
        cake_is_over = True
        break
    command = input()

if cake_is_over:
    print(f"No more cake left! You need {abs(cake_peaces)} pieces more.")
else:
    print(f"{cake_peaces} pieces are left.")



