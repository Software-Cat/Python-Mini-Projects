from collections import deque

def validate_polygon(edgeList, perimeter):
    for edge in edgeList:
        if sum(edgeList) - edge > edge and sum(edgeList) == perimeter:
            continue
        return False
    return True


def shiftEdgeList(edgeList, shift):
    newList = deque(edgeList)
    newList.rotate(shift)
    return tuple(newList)


def reverseEdgeList(edgeList):
    newList = []
    for edge in reversed(edgeList):
        newList.append(edge)
    return tuple(newList)


hepts = []
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            if validate_polygon((a, b, c, d, e, f, g), 9):
                                hepts.append((a, b, c, d, e, f, g))

# Remove repeated hepts
newHepts = []
for hept in hepts:
    for shift in range(1, 7):
        if shiftEdgeList(hept, shift) in newHepts:
            break
        elif reverseEdgeList(shiftEdgeList(hept, shift)) in newHepts:
            break
    else:
        newHepts.append(hept)


print(newHepts)
