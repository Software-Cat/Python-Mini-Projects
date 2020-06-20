message = 'vyv gri kbo iye cdsvv nomynsxq drsc mszrob iye kbo tecd gkcdsxq iyeb dswo vyv hnnnn'  # encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = message.upper()

def decrypt(message, LETTERS):
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Hacking key #{}: {}'.format(key, translated))

decrypt(message, LETTERS)