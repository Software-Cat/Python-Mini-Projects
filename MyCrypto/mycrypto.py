"""
Application Creator: Bowen Wu

Application Function: To encrypt and decrypt non unicode text

Making the password: Due to the way encrypion functions work, the password have certain limitations:
                        1. The digits can be 1-9(not 0-9)
                        2. The number of digits may not be the number you want
                        3. Sometimes 1 can't come immediately after 7
                        4. Reversing(9) twice is equal to not reversing at all
                        5. Position swapping(7) with same parameters twice is equal to not swapping at all
                        6. Adding(1) then subtracting(2) with same parameters is equal to doing nothing and vice versa
                        7. Multiplying(3) then dividing(3) with same parameters is equal to doing nothing and vice versa
                        8. Powering(5) the rooting(6) with same parameters is equal to doing nothing and vice versa
                        9. The program can only handle characters on a standard US keybord, anything else will cause an error
                        10. Multiplying(3) by 1 is equal to doing nothing

How it works: 1. Encryption: The user's password is translated to some actions done to encrypt the file
              2. Decryption: The user's password is executed reversed in order to undo the encryptions
"""

def int_format(string):
    """
    Converts a string into a int format for encryption
    """
    intList = []
    for item in string:
        if item == '`':
            intList.append(1)
        elif item == '~':
            intList.append(2)
        elif item == '1':
            intList.append(3)
        elif item == '!':
            intList.append(4)
        elif item == '2':
            intList.append(5)
        elif item == '@':
            intList.append(6)
        elif item == '3':
            intList.append(7)
        elif item == '#':
            intList.append(8)
        elif item == '4':
            intList.append(9)
        elif item == '$':
            intList.append(10)
        elif item == '5':
            intList.append(11)
        elif item == '%':
            intList.append(12)
        elif item == '6':
            intList.append(13)
        elif item == '^':
            intList.append(14)
        elif item == '7':
            intList.append(15)
        elif item == '&':
            intList.append(16)
        elif item == '8':
            intList.append(17)
        elif item == '*':
            intList.append(18)
        elif item == '9':
            intList.append(19)
        elif item == '(':
            intList.append(20)
        elif item == '0':
            intList.append(21)
        elif item == ')':
            intList.append(22)
        elif item == '-':
            intList.append(23)
        elif item == '_':
            intList.append(24)
        elif item == '=':
            intList.append(25)
        elif item == '+':
            intList.append(26)
        elif item == 'q':
            intList.append(27)
        elif item == 'Q':
            intList.append(28)
        elif item == 'w':
            intList.append(29)
        elif item == 'W':
            intList.append(30)
        elif item == 'e':
            intList.append(31)
        elif item == 'E':
            intList.append(32)
        elif item == 'r':
            intList.append(33)
        elif item == 'R':
            intList.append(34)
        elif item == 't':
            intList.append(35)
        elif item == 'T':
            intList.append(36)
        elif item == 'y':
            intList.append(37)
        elif item == 'Y':
            intList.append(38)
        elif item == 'u':
            intList.append(39)
        elif item == 'U':
            intList.append(40)
        elif item == 'i':
            intList.append(41)
        elif item == 'I':
            intList.append(42)
        elif item == 'o':
            intList.append(43)
        elif item == 'O':
            intList.append(44)
        elif item == 'p':
            intList.append(45)
        elif item == 'P':
            intList.append(46)
        elif item == '[':
            intList.append(47)
        elif item == '{':
            intList.append(48)
        elif item == ']':
            intList.append(49)
        elif item == '}':
            intList.append(50)
        elif item == '\\':
            intList.append(51)
        elif item == '|':
            intList.append(52)
        elif item == 'a':
            intList.append(53)
        elif item == 'A':
            intList.append(54)
        elif item == 's':
            intList.append(55)
        elif item == 'S':
            intList.append(56)
        elif item == 'd':
            intList.append(57)
        elif item == 'D':
            intList.append(58)
        elif item == 'f':
            intList.append(59)
        elif item == 'F':
            intList.append(60)
        elif item == 'g':
            intList.append(61)
        elif item == 'G':
            intList.append(62)
        elif item == 'h':
            intList.append(63)
        elif item == 'H':
            intList.append(64)
        elif item == 'j':
            intList.append(65)
        elif item == 'J':
            intList.append(66)
        elif item == 'k':
            intList.append(67)
        elif item == 'K':
            intList.append(68)
        elif item == 'l':
            intList.append(69)
        elif item == 'L':
            intList.append(70)
        elif item == ';':
            intList.append(71)
        elif item == ':':
            intList.append(72)
        elif item == "'":
            intList.append(73)
        elif item == '"':
            intList.append(74)
        elif item == 'z':
            intList.append(75)
        elif item == 'Z':
            intList.append(76)
        elif item == 'x':
            intList.append(77)
        elif item == 'X':
            intList.append(78)
        elif item == 'c':
            intList.append(79)
        elif item == 'C':
            intList.append(80)
        elif item == 'v':
            intList.append(81)
        elif item == 'V':
            intList.append(82)
        elif item == 'b':
            intList.append(83)
        elif item == 'B':
            intList.append(84)
        elif item == 'n':
            intList.append(85)
        elif item == 'N':
            intList.append(86)
        elif item == 'm':
            intList.append(87)
        elif item == 'M':
            intList.append(88)
        elif item == ',':
            intList.append(89)
        elif item == '<':
            intList.append(90)
        elif item == '.':
            intList.append(91)
        elif item == '>':
            intList.append(92)
        elif item == '/':
            intList.append(93)
        elif item == '?':
            intList.append(94)
        elif item == ' ':
            intList.append(95)
        elif item == '\n':
            intList.append(96)
        elif item == '\r':
            intList.append(97)
        elif item == '\r\n':
            intList.append(98)
        elif item == '\v':
            intList.append(99)
        elif item == '\f':
            intList.append(100)
        elif item == '\x1c':
            intList.append(101)
        elif item == '\x1d':
            intList.append(102)
        elif item == '\x1e':
            intList.append(103)
        elif item == '\x85':
            intList.append(104)
        elif item == 'u\u2028':
            intList.append(105)
        elif item == 'u\u2029':
            intList.append(106)
        else:
            raise ValueError('Unconvertable character: ' + item)
    return intList

def str_format(intList):
    """
    Converts a intlist containing int format characters back to a string for decryption
    """
    strList = []
    for item in intList:
        if item == 1:
            strList.append('`')
        elif item == 2:
            strList.append('~')
        elif item == 3:
            strList.append('1')
        elif item == 4:
            strList.append('!')
        elif item == 5:
            strList.append('2')
        elif item == 6:
            strList.append('@')
        elif item == 7:
            strList.append('3')
        elif item == 8:
            strList.append('#')
        elif item == 9:
            strList.append('4')
        elif item == 10:
            strList.append('$')
        elif item == 11:
            strList.append('5')
        elif item == 12:
            strList.append('%')
        elif item == 13:
            strList.append('6')
        elif item == 14:
            strList.append('^')
        elif item == 15:
            strList.append('7')
        elif item == 16:
            strList.append('&')
        elif item == 17:
            strList.append('8')
        elif item == 18:
            strList.append('*')
        elif item == 19:
            strList.append('9')
        elif item == 20:
            strList.append('(')
        elif item == 21:
            strList.append('0')
        elif item == 22:
            strList.append(')')
        elif item == 23:
            strList.append('-')
        elif item == 24:
            strList.append('_')
        elif item == 25:
            strList.append('=')
        elif item == 26:
            strList.append('+')
        elif item == 27:
            strList.append('q')
        elif item == 28:
            strList.append('Q')
        elif item == 29:
            strList.append('w')
        elif item == 30:
            strList.append('W')
        elif item == 31:
            strList.append('e')
        elif item == 32:
            strList.append('E')
        elif item == 33:
            strList.append('r')
        elif item == 34:
            strList.append('R')
        elif item == 35:
            strList.append('t')
        elif item == 36:
            strList.append('T')
        elif item == 37:
            strList.append('y')
        elif item == 38:
            strList.append('Y')
        elif item == 39:
            strList.append('u')
        elif item == 40:
            strList.append('U')
        elif item == 41:
            strList.append('i')
        elif item == 42:
            strList.append('I')
        elif item == 43:
            strList.append('o')
        elif item == 44:
            strList.append('O')
        elif item == 45:
            strList.append('p')
        elif item == 46:
            strList.append('P')
        elif item == 47:
            strList.append('[')
        elif item == 48:
            strList.append('{')
        elif item == 49:
            strList.append(']')
        elif item == 50:
            strList.append('}')
        elif item == 51:
            strList.append('\\')
        elif item == 52:
            strList.append('|')
        elif item == 53:
            strList.append('a')
        elif item == 54:
            strList.append('A')
        elif item == 55:
            strList.append('s')
        elif item == 56:
            strList.append('S')
        elif item == 57:
            strList.append('d')
        elif item == 58:
            strList.append('D')
        elif item == 59:
            strList.append('f')
        elif item == 60:
            strList.append('F')
        elif item == 61:
            strList.append('g')
        elif item == 62:
            strList.append('G')
        elif item == 63:
            strList.append('h')
        elif item == 64:
            strList.append('H')
        elif item == 65:
            strList.append('j')
        elif item == 66:
            strList.append('J')
        elif item == 67:
            strList.append('k')
        elif item == 68:
            strList.append('K')
        elif item == 69:
            strList.append('l')
        elif item == 70:
            strList.append('L')
        elif item == 71:
            strList.append(';')
        elif item == 72:
            strList.append(':')
        elif item == 73:
            strList.append("'")
        elif item == 74:
            strList.append('"')
        elif item == 75:
            strList.append('z')
        elif item == 76:
            strList.append('Z')
        elif item == 77:
            strList.append('x')
        elif item == 78:
            strList.append('X')
        elif item == 79:
            strList.append('c')
        elif item == 80:
            strList.append('C')
        elif item == 81:
            strList.append('v')
        elif item == 82:
            strList.append('V')
        elif item == 83:
            strList.append('b')
        elif item == 84:
            strList.append('B')
        elif item == 85:
            strList.append('n')
        elif item == 86:
            strList.append('N')
        elif item == 87:
            strList.append('m')
        elif item == 88:
            strList.append('M')
        elif item == 89:
            strList.append(',')
        elif item == 90:
            strList.append('<')
        elif item == 91:
            strList.append('.')
        elif item == 92:
            strList.append('>')
        elif item == 93:
            strList.append('/')
        elif item == 94:
            strList.append('?')
        elif item == 95:
            strList.append(' ')
        elif item == 96:
            strList.append('\n')
        elif item == 97:
            strList.append('\r')
        elif item == 98:
            strList.append('\r\n')
        elif item == 99:
            strList.append('\v')
        elif item == 100:
            strList.append('\f')
        elif item == 101:
            strList.append('\x1c')
        elif item == 102:
            strList.append('\x1d')
        elif item == 103:
            strList.append('\x1e')
        elif item == 104:
            strList.append('\x85')
        elif item == 105:
            strList.append(u'\u2028')
        elif item == 106:
            strList.append(u'\u2029')
        else:
            #raise ValueError('Unconvertable character: ' + str(item))
            strList.append(str(item))
    return ''.join(strList)

def add(intList, num, step): #1
    """
    Performs addition to list items and num with index increasing by step

    """
    newIntList = []
    thingsToAdd = []
    for index in range(0, len(intList), step):
        thingsToAdd.append(index)
    for index, item in enumerate(intList):
        if index in thingsToAdd:
            newIntList.append(item + num)
        else:
            newIntList.append(item)
    return newIntList

def subtract(intList, num, step): #2
    """
    Performs subtraction to list items and num with index increasing by step

    """
    newIntList = []
    thingsToAdd = []
    for index in range(0, len(intList), step):
        thingsToAdd.append(index)
    for index, item in enumerate(intList):
        if index in thingsToAdd:
            newIntList.append(item - num)
        else:
            newIntList.append(item)
    return newIntList

def multiply(intList, num, step): #3
    """
    Performs multiplication to list items and num with index increasing by step

    """
    newIntList = []
    thingsToAdd = []
    for index in range(0, len(intList), step):
        thingsToAdd.append(index)
    for index, item in enumerate(intList):
        if index in thingsToAdd:
            newIntList.append(item * num)
        else:
            newIntList.append(item)
    return newIntList

def divide(intList, num, step): #4
    """
    Performs division to list items and num with index increasing by step

    """
    newIntList = []
    thingsToAdd = []
    for index in range(0, len(intList), step):
        thingsToAdd.append(index)
    for index, item in enumerate(intList):
        if index in thingsToAdd:
            newIntList.append(item / float(num))
        else:
            newIntList.append(item)
    return newIntList

def power(intList, num, step): #5
    """
    Performs the nth power to list items and num with index increasing by step

    """
    newIntList = []
    thingsToAdd = []
    for index in range(0, len(intList), step):
        thingsToAdd.append(index)
    for index, item in enumerate(intList):
        if index in thingsToAdd:
            newIntList.append(item ** num)
        else:
            newIntList.append(item)
    return newIntList

def root(intList, num, step): #6
    """
    Performs nth root to list items and num with index increasing by step
    """
    def single_root(int, n):
        """
        The function that performs the nth root to int
        """
        u, s = n, n+1
        while u < s:
            s = u
            t = (int-1) * s + n // pow(s, int-1)
            u = t // int
        return s

    newIntList = []
    thingsToAdd = []
    for index in range(0, len(intList), step):
        thingsToAdd.append(index)
    for index, item in enumerate(intList):
        if index in thingsToAdd:
            newIntList.append(single_root(item, num))
        else:
            newIntList.append(item)
    return newIntList

def swap_pos(intList, step): #7
    """
    Swap the character and the character after's positions with index increasing by step
    """
    if step < 2:
        raise ValueError('Parameter step cannot be smaller than 2')
    newIntList = []
    thingsToSwap = []
    for index in range(0, len(intList)-1, step):
        thingsToSwap.append(index)
    for index, item in enumerate(intList):
        if index in thingsToSwap:
            newIntList.append(intList[index + 1])
        elif index-1 in thingsToSwap:
            newIntList.append(intList[index - 1])
        else:
            newIntList.append(item)
    return newIntList

def fake_nums(intList, step): #8
    """
    Add fake numbers to intlist with index increasing by step (only used in encrytion)
    """
    from random import randint
    placeToInsertNum = []
    for index in range(0, len(intList), step):
        placeToInsertNum.append(index)
    newIntList = [item for item in intList]
    for index in reversed(placeToInsertNum):
        newIntList.insert(index, randint(1, 100))
    return newIntList

def del_fake_nums(intList, step): #8
    """
    Delete fake numbers added by the fake_nums function (only used in decryption)
    """
    placeToDelNum = []
    for index in range(0, len(intList), step+1):
        placeToDelNum.append(index)
    newIntList = [item for item in intList]
    for index in reversed(placeToDelNum):
        del newIntList[index]
    return newIntList

def reverse(intList): #9
    """
    Reverse the intList
    """
    return list(reversed(intList))

def password_to_process(password):
    """
    Translates the password to a list of processes to perform to encrypt the string
    """
    process = {}
    password = [int(item) for item in str(password)]
    index = 0
    action = 0
    while True:
        if index == len(password):
            break
        if password[index] == 1:
            process[action] = (add, password[index+1], password[index+2])
            index += 3
            action += 1
        elif password[index] == 2:
            process[action] = (subtract, password[index+1], password[index+2])
            index += 3
            action += 1
        elif password[index] == 3:
            process[action] = (multiply, password[index+1], password[index+2])
            index += 3
            action += 1
        elif password[index] == 4:
            process[action] = (divide, password[index+1], password[index+2])
            index += 3
            action += 1
        elif password[index] == 5:
            process[action] = (power, password[index+1], password[index+2])
            index += 3
            action += 1
        elif password[index] == 6:
            process[action] = (root, password[index+1], password[index+2])
            index += 3
            action += 1
        elif password[index] == 7:
            process[action] = (swap_pos, password[index+1])
            index += 2
            action += 1
        elif password[index] == 8:
            process[action] = (fake_nums, password[index+1])
            index += 2
            action += 1
        elif password[index] == 9:
            process[action] = reverse
            index += 1
            action += 1
        else:
            raise ValueError('Invalid password digit: ' + str(password[index]))
    return process

def process_to_decryption_processs(process):
    """
    reverse the process 
    """
    reversedProcess = {}
    decryptionProcess = {}
    for index, item in enumerate(reversed(process.values())):
        reversedProcess[index] = item
    for index in range(len(reversedProcess)):
        if reversedProcess[index] == reverse:
            decryptionProcess[index] = (reverse)
        elif reversedProcess[index][0] == add:
            decryptionProcess[index] = (subtract, reversedProcess[index][1], reversedProcess[index][2])
        elif reversedProcess[index][0] == subtract:
            decryptionProcess[index] = (add, reversedProcess[index][1], reversedProcess[index][2])
        elif reversedProcess[index][0] == multiply:
            decryptionProcess[index] = (divide, reversedProcess[index][1], reversedProcess[index][2])
        elif reversedProcess[index][0] == divide:
            decryptionProcess[index] = (multiply, reversedProcess[index][1], reversedProcess[index][2])
        elif reversedProcess[index][0] == power:
            decryptionProcess[index] = (root, reversedProcess[index][1], reversedProcess[index][2])
        elif reversedProcess[index][0] == root:
            decryptionProcess[index] = (power, reversedProcess[index][1], reversedProcess[index][2])
        elif reversedProcess[index][0] == swap_pos:
            decryptionProcess[index] = (swap_pos, reversedProcess[index][1])
        elif reversedProcess[index][0] == fake_nums:
            decryptionProcess[index] = (del_fake_nums, reversedProcess[index][1])
        else:
            raise ValueError('Invalid process: ' + str(reversedProcess[index]))
    return decryptionProcess

def run_through_process(intList, process):
    """
    Run through some processes to encrypt or decrypt an intlist
    """
    newIntList = intList
    for index in range(len(process)):
        if callable(process[index]):
            arguments = 1
        else:
            arguments = len(process[index])
        if arguments == 1:
            newIntList = process[index](newIntList)
        elif arguments == 2:
            newIntList = process[index][0](newIntList, process[index][1])
        elif arguments == 3:
            newIntList = process[index][0](newIntList, process[index][1], process[index][2])
        else:
            raise ValueError('Invalid number of arguments: ' + str(arguments))
        print('finished process: ' + str(process[index]))
    return newIntList

def encrypt(string, password):
    """
    Encrypts a string to an encrypted intList according to a password
    """
    process = password_to_process(password)
    intList = int_format(string)
    newIntList = run_through_process(intList, process)
    return newIntList

def decrypt(intList, password):
    """
    Decrypts an encrypted intList to a string according to a password
    """
    encryptionProcess = password_to_process(password)
    process = process_to_decryption_processs(encryptionProcess)
    newIntList = run_through_process(intList, process)
    string = str_format(newIntList)
    return string

def encrypt_file(fileName, password):
    """
    Encrypts a file and store it in a file with a extention name of .mycrypto
    """
    #Import os.path for checking if a file exists later
    from os import path
    #If the file the user wish to encrypt does not exist then raise an IO error
    if not path.isfile(fileName):
        raise IOError('Failed to find file with name: ' + fileName)
    #Read all text from the file
    with open(fileName, 'r') as f:
        fileText = f.read()
    #Encrypt all the text with a password
    encryptedText = str(encrypt(fileText, password))
    #Generate encrypted file's file name
    encryptedFileName = fileName.split('.')[0] + '.mycrypto'
    index = 2
    while path.isfile(encryptedFileName):
        #If a file with the same name already exists then change the name of the file
        encryptedFileName = fileName.split('.')[0]  + '(' + str(index) + ')' + '.mycrypto'
        index += 1
    del index
    #write the new file
    with open(encryptedFileName, 'w') as file:
        file.write(encryptedText)

def decrypt_file(fileName, password, printToScreenMode=False):
    """
    Decrypts a file with the extention name of .mycrypto
    """
    #Import os.path for checking if a file exists later
    from os import path
    #If the file the user wish to decrypt does not exist then raise an IO error
    if not path.isfile(fileName):
        raise IOError('Failed to find file with name: ' + fileName)
    if fileName.split('.')[1] != 'mycrypto':
        raise IOError('Cannot decrypt non .mycrypto files. Got file extention name: ' + fileName.split('.')[1])
    #Read all text from the file
    with open(fileName, 'r') as f:
        fileText = f.read()
    #Transform the file text into an intlist
    #Break the huge string down into small values
    strIntList = [item for item in fileText.split(',')]
    strIntList[0] = strIntList[0].lstrip('[')
    strIntList[len(strIntList)-1] = strIntList[len(strIntList)-1].rstrip(']')
    #Change the strings into a int list
    intList = []
    for item in strIntList:
        if '.' in item:
            intList.append(float(item))
        elif 'L' in item:
            intList.append(int(item))
        else:
            intList.append(int(item))
    #Delete some now useless names to save some memory
    del fileText
    del strIntList
    #Decrypt the intlist generated from the file
    decryptedText = decrypt(intList, password)
    #Print to screen and finish if in print to screen mode
    if printToScreenMode:
        print(decryptedText)
        return
    #Generate encrypted file's file name
    decryptedFileName = fileName.split('.')[0] + '(decrypted)' +'.txt'
    index = 2
    while path.isfile(decryptedFileName):
        #If a file with the same name already exists then change the name of the file
        decryptedFileName = fileName.split('.')[0] + '(decrypted)'  + '(' + str(index) + ')' + '.txt'
        index += 1
    del index
    #write the new file
    with open(decryptedFileName, 'w') as file:
        file.write(decryptedText)

if __name__ == '__main__':
    password = None
    #encrypt_file("C:\Users\Home-windows 2 in 1\Desktop\Python\Encryption and Decyption Algorithm\cipher_text.txt", password)
    #decrypt_file("C:\Users\Home-windows 2 in 1\Desktop\Python\Encryption and Decyption Algorithm\cipher_text.mycrypto", password, False)
