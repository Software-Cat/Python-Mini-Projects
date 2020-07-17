import random as r

wins = 0
iterations = 1000
items = ['g', 'g', 'c']
swap = True

for i in range(iterations):
    items = ['g', 'g', 'c']
    r.shuffle(items)

    # Your guess
    guess = r.randint(0, 2)
    
    # Reveal a goat
    revealing = [0, 1, 2]
    revealing.remove(guess)
    try:
        revealing.remove(items.index('c'))
    except:
        pass
    items[r.choice(revealing)] = 'revealed g'

    # Do you swap
    choices = [0, 1, 2]
    choices.remove(items.index('revealed g'))
    if swap:
        choices.remove(guess)
        guess = choices[0]
    else:
        pass

    if items[guess] == 'c':
        wins += 1
    else:
        pass

print(f'Total wins: {wins}')
print(f'Win percentage: {wins / iterations * 100}%')
