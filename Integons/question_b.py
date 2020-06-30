tris = []

def validate_tri(a, b, c):
    if a+b > c and a+c > b and b+c > a and a+b+c == 7:
        return True
    else:
        return False

for a in range(1, 8):
    for b in range(1, 8):
        for c in range(1, 8):
            if validate_tri(a, b, c):
                print(f"Testing {a}, {b}, {c}")
                tris.append((a, b, c))

print(tris)