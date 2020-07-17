import turtle as t
import math

ITERATIONS = 100
ENLARGEMENT = 10
t.left(180)

for i in range(ITERATIONS):
    t.forward(math.sqrt(i) * ENLARGEMENT)
    t.left(90)
    t.forward(1 * ENLARGEMENT)
    t.goto(0, 0)

t.mainloop()
