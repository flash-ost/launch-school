import json

LANGUAGE = 'en'

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang=LANGUAGE):
    return MESSAGES[lang][message]

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'data' contains the contents of the JSON file as a Python dictionary or list

prompt(messages('welcome'))

while True:
    # Ask the user for numbers and operation
    prompt(messages('first_number'))
    number1 = input()
    while invalid_number(number1):
        prompt(messages('invalid_number'))
        number1 = input()

    prompt(messages('second_number'))
    number2 = input()
    while invalid_number(number2):
        prompt(messages('invalid_number'))
        number2 = input()

    prompt(messages('operation'))
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt(messages('invalid_operation'))
        operation = input()

    # Perform operation and print result
    match operation:
        case'1':
            output = float(number1) + float(number2)
        case'2':
            output = float(number1) - float(number2)
        case'3':
            output = float(number1) * float(number2)
        case'4':
            output = float(number1) / float(number2)

    prompt(f'{messages('result')} {output}')

    prompt(messages('another'))
    answer = input()
    if answer != 'Y':
        break