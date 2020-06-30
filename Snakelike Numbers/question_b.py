numbers = []

# Going up first (1st digit cannot be 0)
for digit1 in range(1, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
            if digit2 > digit1 and digit3 < digit2:
                numbers.append(str(digit1) + str(digit2) + str(digit3))

# Going down first
for digit1 in range(1, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
                if digit2 < digit1 and digit3 > digit2:
                    numbers.append(str(digit1) + str(digit2) + str(digit3))

satisfyCount = 0
for n in numbers:
    if n[1] == "6":
        print(n)
        satisfyCount += 1

print(f"{satisfyCount} numbers satisfy criteria")
