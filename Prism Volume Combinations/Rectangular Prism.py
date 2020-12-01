"""
I know it's so much easier to use factors of the volume to figure it out but I'm not bothered.
"""

VOLUME = 47

combinations = []

# Loop through all possible combinations
for x in range(1, VOLUME + 1):
    for y in range(1, VOLUME + 1):
        for z in range(1, VOLUME + 1):
            if x * y * z == VOLUME:
                combinations.append([x, y, z])

# Deduplicate combinations
deduplicateCombinations = []

for comb in combinations:
    isDuplicate = False
    for item in deduplicateCombinations:
        item.sort()
        comb.sort()
        if item == comb:
            isDuplicate = True
    if not isDuplicate:
        deduplicateCombinations.append(comb)

print(deduplicateCombinations)
