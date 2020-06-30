numbers = []

# Going up first
for digit1 in range(1, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
            for digit4 in range(0, 10):
                if digit2 > digit1 and digit3 < digit2 and digit4 > digit3:
                    numbers.append(str(digit1) + str(digit2) +
                                   str(digit3) + str(digit4))

# Going down first
for digit1 in range(1, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
            for digit4 in range(0, 10):
                if digit2 < digit1 and digit3 > digit2 and digit4 < digit3:
                    numbers.append(str(digit1) + str(digit2) +
                                   str(digit3) + str(digit4))

satisfyCount = 0
for n in numbers:
    if n.count("1") == 1 and n.count("2") == 1 and n.count("3") == 1 and n.count("4") == 1:
        print(n)
        satisfyCount += 1
        
print(f"{satisfyCount} numbers satisfy criteria")