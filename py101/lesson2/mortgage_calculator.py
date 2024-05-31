from math import isnan

MONTHS_IN_YEAR = 12

# Print a formatted message
def prompt(message):
    print(f'==> {message}')

# Check user's input
def invalid_input(number_str):
    try:
        number = float(number_str)
        # Discard non-positive and NaN values
        if number <= 0 or isnan(number):
            raise ValueError
        return False

    except ValueError:
        prompt('Please enter a positive number.')
        return True

prompt('Welcome to Mortgage Calculator!')
while True:
    prompt('------------------------------------------------------------')
    # Prompt user for loan amount
    prompt('Enter the loan amount without currency sign. Example: 300000')
    amount_str = input()
    while invalid_input(amount_str):
        amount_str = input()

    # Prompt user for APR
    prompt('Enter the APR without percent sign. Example: 5')
    apr_str = input()
    while invalid_input(apr_str):
        apr_str = input()

    # Prompt user for loan duration
    prompt('Enter the loan duration in months. Example: 60')
    duration_str = input()
    while invalid_input(duration_str):
        duration_str = input()

    # Calculate and display monthly payment
    amount = float(amount_str)
    mpr_fraction = float(apr_str) / MONTHS_IN_YEAR / 100
    duration = float(duration_str)
    payment = amount * (mpr_fraction / (1 - (1 + mpr_fraction) ** -duration))
    prompt(f'Your monthly payment is: ${round(payment, 2)}')

    # Ask for another round
    prompt('Another calculation? (Y/N)')
    while True:
        answer = input()
        if answer not in ['N', 'Y', 'n', 'y']:
            prompt('Please enter a valid answer (Y for yes or N for no).')
        else:
            break

    if answer in ['N', 'n']:
        break      