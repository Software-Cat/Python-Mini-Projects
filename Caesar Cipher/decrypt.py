message = 'LZW OSJ AK GNWJ. 3,500 MC EWJUZSFL KZAHK OWJW KMFC, SFV 25% GX LZWAJ UJWOK OWJW CADDWV'  # encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


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