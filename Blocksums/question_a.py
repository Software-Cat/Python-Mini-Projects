class Grid:
    def __init__(self, matrix=None):
        if (matrix):
            self.matrix = matrix
        else:
            self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __str__(self):
        return str(str(self.matrix[0][0]) + str(self.matrix[1][0]) + str(self.matrix[2][0]) + "\n" + 
                   str(self.matrix[0][1]) + str(self.matrix[1][1]) + str(self.matrix[2][1]) + "\n" + 
                   str(self.matrix[0][2]) + str(self.matrix[1][2]) + str(self.matrix[2][2])
        )


    def get_pos(self, x, y):
        return self.matrix[x][y]

    def set_pos(self, x, y, number):
        self.matrix[x][y] = number

    def blocksums(self):
        return (
            self.matrix[0][0] + self.matrix[1][0] +
            self.matrix[0][1] + self.matrix[1][1],
            self.matrix[1][0] + self.matrix[2][0] +
            self.matrix[1][1] + self.matrix[2][1],
            self.matrix[0][1] + self.matrix[1][1] +
            self.matrix[0][2] + self.matrix[1][2],
            self.matrix[1][1] + self.matrix[2][1] +
            self.matrix[1][2] + self.matrix[2][2]
        )

    def count(self, number):
        count = 0
        for x in range(0, 3):
            for y in range(0, 3):
                if(self.matrix[x][y] == number):
                    count += 1
        return count


grids = []
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                for e in range(0, 2):
                    for f in range(0, 2):
                        for g in range(0, 2):
                            for h in range(0, 2):
                                for i in range(0, 2):
                                    grids.append(
                                        Grid([[a, b, c], [d, e, f], [g, h, i]]))

print("Blocksums are 3")
for grid in grids:
    if grid.blocksums() == (3, 3, 3, 3) and grid.count(1) == 5 and grid.count(0) == 4:
        print(grid)

print("Blocksums are 2")
for grid in grids:
    if grid.blocksums() == (2, 2, 2, 2) and grid.count(1) == 5 and grid.count(0) == 4:
        print(grid)
