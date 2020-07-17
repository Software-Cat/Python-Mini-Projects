import tkinter as tk
from tkinter import simpledialog, messagebox
import random


def read_from_file():  # Read the information in 'cleverbot_data.txt'
    global dialogue_parts
    with open("CleverBot/cleverbot_data.txt") as file:
        for line in file:
            line = line.rstrip("\n")
            part1, part2 = line.split("|")
            part2_list = [part2]
            if part1 in dialogue_parts:
                dialogue_parts[part1].append(part2)
            else:
                dialogue_parts[part1] = part2_list


def write_to_file(part1, part2):  # Write new data in the form of Q&A in to the language storage
    with open("CleverBot/new_cleverbot_data.txt", "a") as file:
        file.write('\n' + part1 + '|' + part2)
    
    # Optional write to dialogue parts dictionary as well as well (could disable)
    if part1 in dialogue_parts:
        dialogue_parts[part1].append(part2)
    else:
        dialogue_parts[part1] = [part2]


def second_personalize(string):  # Replace 'cleverbot' with 'you'
    new_string = string.replace('CleverBot', 'you')
    new_string = new_string.replace('Cleverbot', 'you')
    new_string = new_string.replace('cleverbot', 'you')
    new_string = new_string.replace('Clever Bot', 'you')
    new_string = new_string.replace('Clever bot', 'you')
    new_string = new_string.replace('clever bot', 'you')
    return new_string


def resolve_unknown_response(witty_response_percentage):
    global part2
    global user_defined_association_words
    global old_part1
    global part1
    global recording_differently

    if random.randint(1, 100) >= witty_response_percentage:
        part2 = random.choice(user_defined_association_words)

        # Store the last user input to build an association with the new one
        old_part1 = second_personalize(part1)
        # Because the programme is not building an association with user defined association words such as 'What would you say if you were me?' it need to record differently
        recording_differently = True
    else:
        witty_resolve_unknown_response()


def witty_resolve_unknown_response():
    global part1
    global part2
    global dialogue_parts

    if random.randint(1, 3) == 1:
        # Reverse the question so the program is asking the user what the user asked the program
        part2 = second_personalize(part1)
    elif random.randint(1, 2) == 1:
        # Randomly pick one association key. Although not related to the input, it gathers multiple outputs for that key.
        dialogueKeys = list(dialogue_parts.keys())
        part2 = random.choice(dialogueKeys)
    else:
        # Randomly pick one response to a random key. Although not related to the input, it gathers responses for that response.
        dialogueKeys = list(dialogue_parts.keys())
        part2 = random.choice(
            dialogue_parts[random.choice(dialogueKeys)])

def witty_response(part1):
    global dialogue_parts

    if random.randint(1, 3) == 1:
        # Reverse the question so the program is asking the user what the user asked the program
        part2 = second_personalize(part1)
    elif random.randint(1, 2) == 1:
        # Randomly pick one association key. Although not related to the input, it gathers multiple outputs for that key.
        dialogueKeys = list(dialogue_parts.keys())
        part2 = random.choice(dialogueKeys)
    else:
        # Randomly pick one response to a random key. Although not related to the input, it gathers responses for that response.
        dialogueKeys = list(dialogue_parts.keys())
        part2 = random.choice(
            dialogue_parts[random.choice(dialogueKeys)])
    return part2

def close():
    # Close
    root.destroy()
    quit()


# Variables
# The dictionary that contain all language information (associations)
dialogue_parts = {}
# Things asked for unknowns (could modify this)
user_defined_association_words = [
    'What would you say if you were me?', 'How do you want me to respond to this?']
is_first_sentence = True
recording_differently = False
recording_differently_last_turn = False
old_part1 = ''
part1 = ''
part2 = ''

# Read everything from cleverbot_data.txt into memory
read_from_file()

def respond(arg=None):
    global is_first_sentence
    global recording_differently
    global recording_differently_last_turn
    global part1
    global part2
    global old_part1
    global dialogue_parts

    part1 = ''
    # Get user input
    part1 = entry.get()
    # Uniformisation
    # Lowecase the input
    part1 = part1.lower()
    # Delete full stops
    part1 = part1.rstrip('.')
    # Delete exclamation marks
    part1 = part1.rstrip('!')
    # Swap '|'(special seperation mark) for '/' (not used for anything special)
    part1 = part1.replace('|', '/')
    # Remove excess spaces (preceding, in between and trailing)
    part1 = ' '.join([word for word in part1.split(' ') if word != ''])

    # Loop break (quit)
    if part1 == 'bye' or part1 == 'goodbye':  # Quit if input is 'goodbye'
        close()

    # Record and update
    # If this is not the first time run and the program is not recording differently
    if not is_first_sentence and not recording_differently:
        # Build an association(Answer) with the previous sentence
        write_to_file(part2, second_personalize(part1))
    elif recording_differently:
        # Build an association with the last user input as the program was asking 'what would you say if you were me'
        write_to_file(old_part1, part1)
        recording_differently = False
        recording_differently_last_turn = True
    else:
        # Make it so that this program is not ran the first time any more
        is_first_sentence = False

    # Response
    if part1 in dialogue_parts:  # If the program already have a string associated with what the user typed
        # There is a chance that the user is still asked with user defined association words, this is to gather many responses for each question
        if random.randint(1, 10) == 1:
            resolve_unknown_response(75)
        else:
            # choose a random string associated with the user input
            part2 = random.choice(dialogue_parts[part1])
    # If after swapping 'CleverBot' with 'you' the input is associated
    elif second_personalize(part1) in dialogue_parts:
        # This could happen because the program is storing the sentence with 'CleverBot' --> 'you'
        if random.randint(1, 10) == 1:  # <--- This is to gather multiple answers
            resolve_unknown_response(75)
        else:
            part2 = random.choice(dialogue_parts[second_personalize(part1)])
    else:
        if not recording_differently_last_turn:
            resolve_unknown_response(50)
        else:
            witty_resolve_unknown_response()

    # Easter egg commands
    if part1 == '/kill':
        close()
    elif part1 == '/clear':
        dialogue_parts = {}
    elif part1 == '/jumble':
        for key in dialogue_parts.keys():
            dialogue_parts[key] = random.choice([val for val in dialogue_parts.values()])
    elif part1[:5] == '/set ':
        params = part1.split(' ')
        dialogue_parts[parts[1]] = [val for val in params[2].split(',')]
        del params
    elif part1[:8] == '/append ':
        params = part1.split(' ')
        for val in params[2].split(','):
            dialogue_parts[params[1]].append(val)
        del params
    elif part1[:14] == '/appendglobal ':
        params = part1.split(' ')
        for val in params[2].split(','):
            dialogue_parts[params[1]].append(val)
            write_to_file(params[1], val)
        del params
    elif part1[:5] == '/get ':
        params = part1.split(' ')
        part2 = str(dialogue_parts[params[1]])
        del params
    elif part1[:7] == '/witty ':
        part2 = witty_response(part1[7:])
        print(part1[7:])

    # Display
    cleverbotResponse['text'] = part2.capitalize()

    # Update
    if recording_differently_last_turn:
        recording_differently_last_turn = False
    
    # Clear entry
    entry.delete(0, 'end')

# Tk objects
root = tk.Tk(className=' CleverBot')

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

title = tk.Label(root, text='CleverBot')
title.config(font=('helvetica', 14))
canvas.create_window(200, 50, window=title)

tip = tk.Label(root, text='Type your Response here:')
tip.config(font=('helvetica', 10))
canvas.create_window(200, 100, window=tip)

entry = tk.Entry(root, width=50)
canvas.create_window(200, 140, window=entry)
entry.bind('<Return>', respond)

cleverbotResponse = tk.Label(root, text='')
canvas.create_window(200, 230, window=cleverbotResponse)

button = tk.Button(text='Get Response', command=respond, bg='darkgreen', fg='white', font=('helvetica', 9, 'bold'))
canvas.create_window(200, 180, window=button)

# Mainloop
tk.mainloop()
