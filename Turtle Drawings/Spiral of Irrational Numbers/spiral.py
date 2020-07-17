import turtle as t
import math

NUM_OF_TRIANGLES = 100
ENLARGEMENT = 10
t.left(180)

for i in range(1, NUM_OF_TRIANGLES):
    t.forward(math.sqrt(i) * ENLARGEMENT)
    t.left(90)
    t.forward(1 * ENLARGEMENT)
    t.left(math.degrees(math.atan(math.sqrt(i)/1)))
    t.goto(0, 0)
    t.left(180)

t.mainloop()
