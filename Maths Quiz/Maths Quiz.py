import random
#Question Generator
termNum = random.randint(1,10)
term1 = []
term2 = []
term3 = []
term4 = []
term5 = []
term6 = []
term7 = []
term8 = []
term9 = []
term10 = []
connectingOperators = []
for i in range(1,termNum):
    connectingOperators.append(random.choice(["+","-"]))
#T1
for i in range(random.randint(1,4)):
    if i != 0:
        term1.append(random.randint(1,100) * random.choice([-1,1]))
        term1.append(random.choice(["*","/",]))
term1.append(random.randint(1,100) * random.choice([-1,1]))
#T2
for i in range(random.randint(1,4)):
    if i != 0:
        term2.append(random.randint(1,100) * random.choice([-1,1]))
        term2.append(random.choice(["*","/",]))
term2.append(random.randint(1,100) * random.choice([-1,1]))
#T3
for i in range(random.randint(1,4)):
    if i != 0:
        term3.append(random.randint(1,100) * random.choice([-1,1]))
        term3.append(random.choice(["*","/",]))
term3.append(random.randint(1,100) * random.choice([-1,1]))
#T4
for i in range(random.randint(1,4)):
    if i != 0:
        term4.append(random.randint(1,100) * random.choice([-1,1]))
        term4.append(random.choice(["*","/",]))
term4.append(random.randint(1,100) * random.choice([-1,1]))
#T5
for i in range(random.randint(1,4)):
    if i != 0:
        term5.append(random.randint(1,100) * random.choice([-1,1]))
        term5.append(random.choice(["*","/",]))
term5.append(random.randint(1,100) * random.choice([-1,1]))
#T6
for i in range(random.randint(1,4)):
    if i != 0:
        term6.append(random.randint(1,100) * random.choice([-1,1]))
        term6.append(random.choice(["*","/",]))
term6.append(random.randint(1,100) * random.choice([-1,1]))
#T7
for i in range(random.randint(1,4)):
    if i != 0:
        term7.append(random.randint(1,100) * random.choice([-1,1]))
        term7.append(random.choice(["*","/",]))
term7.append(random.randint(1,100) * random.choice([-1,1]))
#T8
for i in range(random.randint(1,4)):
    if i != 0:
        term8.append(random.randint(1,100) * random.choice([-1,1]))
        term8.append(random.choice(["*","/",]))
term8.append(random.randint(1,100) * random.choice([-1,1]))
#T9
for i in range(random.randint(1,4)):
    if i != 0:
        term9.append(random.randint(1,100) * random.choice([-1,1]))
        term9.append(random.choice(["*","/",]))
term9.append(random.randint(1,100) * random.choice([-1,1]))
#T10
for i in range(random.randint(1,4)):
    if i != 0:
        term10.append(random.randint(1,100) * random.choice([-1,1]))
        term10.append(random.choice(["*","/",]))
term10.append(random.randint(1,100) * random.choice([-1,1]))

#Answer Calculation
t1Answer = 0
t2Answer = 0
t3Answer = 0
t4Answer = 0
t5Answer = 0
t6Answer = 0
t7Answer = 0
t8Answer = 0
t9Answer = 0
t10Answer = 0
#t1Answer
t1Answer += term1[0]
for i in range((len(term1) - 1) // 2):
    if term1[(i+1) * 2 - 1] == "*":
        t1Answer *= term1[(i+1) * 2]
    elif term1[(i+1) * 2 - 1] == "/":
        t1Answer /= float(term1[(i+1) * 2])
#t2Answer
t2Answer += term2[0]
for i in range((len(term2) - 1) // 2):
    if term2[(i+1) * 2 - 1] == "*":
        t2Answer *= term2[(i+1) * 2]
    elif term2[(i+1) * 2 - 1] == "/":
        t2Answer /= float(term2[(i+1) * 2])
#t3Answer
t3Answer += term3[0]
for i in range((len(term3) - 1) // 2):
    if term3[(i+1) * 2 - 1] == "*":
        t3Answer *= term3[(i+1) * 2]
    elif term3[(i+1) * 2 - 1] == "/":
        t3Answer /= float(term3[(i+1) * 2])
#t4Answer
t4Answer += term4[0]
for i in range((len(term4) - 1) // 2):
    if term4[(i+1) * 2 - 1] == "*":
        t4Answer *= term4[(i+1) * 2]
    elif term4[(i+1) * 2 - 1] == "/":
        t4Answer /= float(term4[(i+1) * 2])
#t5Answer
t5Answer += term5[0]
for i in range((len(term5) - 1) // 2):
    if term5[(i+1) * 2 - 1] == "*":
        t5Answer *= term5[(i+1) * 2]
    elif term5[(i+1) * 2 - 1] == "/":
        t5Answer /= float(term5[(i+1) * 2])
#t6Answer
t6Answer += term6[0]
for i in range((len(term6) - 1) // 2):
    if term6[(i+1) * 2 - 1] == "*":
        t6Answer *= term6[(i+1) * 2]
    elif term6[(i+1) * 2 - 1] == "/":
        t6Answer /= float(term6[(i+1) * 2])
#t7Answer
t7Answer += term7[0]
for i in range((len(term7) - 1) // 2):
    if term7[(i+1) * 2 - 1] == "*":
        t7Answer *= term7[(i+1) * 2]
    elif term7[(i+1) * 2 - 1] == "/":
        t7Answer /= float(term7[(i+1) * 2])
#t8Answer
t8Answer += term8[0]
for i in range((len(term8) - 1) // 2):
    if term8[(i+1) * 2 - 1] == "*":
        t8Answer *= term8[(i+1) * 2]
    elif term8[(i+1) * 2 - 1] == "/":
        t8Answer /= float(term8[(i+1) * 2])
#t9Answer
t9Answer += term9[0]
for i in range((len(term9) - 1) // 2):
    if term9[(i+1) * 2 - 1] == "*":
        t9Answer *= term9[(i+1) * 2]
    elif term9[(i+1) * 2 - 1] == "/":
        t9Answer /= float(term9[(i+1) * 2])
#t10Answer
t10Answer += term10[0]
for i in range((len(term10) - 1) // 2):
    if term10[(i+1) * 2 - 1] == "*":
        t10Answer *= term10[(i+1) * 2]
    elif term10[(i+1) * 2 - 1] == "/":
        t10Answer /= float(term10[(i+1) * 2])
#Whole experssion construction
expression = []
for i in range(1,termNum + 1):
    if i == 1:
        for currentThing in term1:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 2:
        for currentThing in term2:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 3:
        for currentThing in term3:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 4:
        for currentThing in term4:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 5:
        for currentThing in term5:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 6:
        for currentThing in term6:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 7:
        for currentThing in term7:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 8:
        for currentThing in term8:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 9:
        for currentThing in term9:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
    if i == 10:
        for currentThing in term10:
            expression.append(currentThing)
        if i != termNum:
            expression.append(connectingOperators[i - 1])
#Final answer calculation
finalAnswer = t1Answer
for i in range(2,termNum + 1):
    if i == 2:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t2Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t2Answer
    if i == 3:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t3Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t3Answer
    if i == 4:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t4Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t4Answer
    if i == 5:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t5Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t5Answer
    if i == 6:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t6Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t6Answer
    if i == 7:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t7Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t7Answer
    if i == 8:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t8Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t8Answer
    if i == 9:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t9Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t9Answer
    if i == 10:
        if connectingOperators[i - 2] == "+":
            finalAnswer += t10Answer
        elif connectingOperators[i - 2] == "-":
            finalAnswer -= t10Answer
print("what is the answer of", end=' ')
for i in expression:
    print(i, end=' ')
print("rounded to the nearest whole.")
playerAnswer = input("Answer: ")
if playerAnswer == round(finalAnswer):
    print("Good job, you got it right.")
else:
    print("You got it wrong, the answer is " + str(int(round(finalAnswer))) + ".")
    print("Better luck next time.")
