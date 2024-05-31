from math import isnan
from os import system

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

# Prompt user for input
def prompt_input(message):
    prompt(message)
    number_str = input()
    while invalid_input(number_str):
        number_str = input()
    return number_str

# Prepare variables and calculate monthly payment
def calculate_monthly_payment(amount_input, apr_input, duration_input):
    amount = float(amount_input)
    mpr_fraction = float(apr_input) / MONTHS_IN_YEAR / 100
    duration = float(duration_input) * MONTHS_IN_YEAR
    return amount * (mpr_fraction / (1 - (1 + mpr_fraction) ** -duration))

def display_summary(loan_amount, apr, loan_duration, monthly_payment):
    prompt(f"""You entered
    - Loan amount: ${loan_amount}
    - APR: {apr}%
    - Loan duration: {loan_duration} years
    Your monthly payment is: ${round(monthly_payment, 2)}""")

# Ask user for another round
def another_round():
    prompt('Another calculation? (Y/N)')
    while True:
        try:
            answer = input().lower()
            if answer not in ['n', 'y', 'no', 'yes']:
                raise ValueError
            return answer not in ['n', 'no']
        except ValueError:
            prompt('Please enter a valid answer (Y for yes or N for no).')

prompt('Welcome to Mortgage Calculator!')
while True:
    # Prompt user for necessary input
    amount_str = prompt_input("""Enter the loan amount without currency sign.
    Example: 300000""")
    apr_str = prompt_input("""Enter the APR without percent sign.
    Example: 5""")
    duration_str = prompt_input("""Enter the loan duration in years.
    Example: 7.5""")

    # Calculate monthly payment and display summary
    payment = calculate_monthly_payment(amount_str, apr_str, duration_str)
    display_summary(amount_str, apr_str, duration_str, payment)

    # Ask for another round
    if not another_round():
        break
    system('clear')  