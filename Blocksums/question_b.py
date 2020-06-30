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
for a in [1, 3, 5, 7, 9]:
    for b in [2, 4, 6, 8]:
        for c in [1, 3, 5, 7, 9]:
            for d in [2, 4, 6, 8]:
                    for f in [2, 4, 6, 8]:
                        for g in [1, 3, 5, 7, 9]:
                            for h in [2, 4, 6, 8]:
                                for i in [1, 3, 5, 7, 9]:
                                    e = 5
                                    grids.append(Grid([[a, b, c], [d, e, f], [g, h, i]]))

grids = [grid for grid in grids if 
    grid.count(1) == 1 and 
    grid.count(2) == 1 and 
    grid.count(3) == 1 and 
    grid.count(4) == 1 and 
    grid.count(5) == 1 and
    grid.count(6) == 1 and
    grid.count(7) == 1 and
    grid.count(8) == 1 and
    grid.count(9) == 1
]

for grid in grids:
    blocksum = grid.blocksums()
    if blocksum[0] == blocksum[1] and blocksum[1] == blocksum[2] and blocksum[2] == blocksum[3]:
        print("This grid has a blocksum of {}".format(blocksum[0]))
        print(grid)
