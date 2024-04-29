'''
Console based application to calculate the amount of student debt which
a student will owe on their statement at the end of tax year 2023-2024.

'''

# ---------------Functions---------------


def printline(symbol='-', num=79):
    '''
    Creates a line in the code, 79 characters long to break up the code.
    '''
    print(symbol * num)


def print_heading(title):
    '''
    Print title in the middle of the code.
    '''
    print((' '*(40-(len(title)//2))), title)


def debt_calculator(interest):
    '''
    Calculates the total debt by the end of 2023 - 2024 tax year.
    '''
    total = curr_debt * (1 + interest)
    printline()
    print(f"Your total student debt by the end of the 2023 - 2024 tax year will be: {total}")
    printline()


# ---------------Variables---------------

# Average student loan interest rate in Australia for 2023 - 2024.
a_interest = 0.071

# Average student loan interest rate in New Zealand (students who moved abroad after graduating)
# for 2023 - 2024.
nz_interest = 0.029

# Average student loan interest rate in Sweden for 2023 - 2024.
s_interest = 0.0123

# Average student loan interest rate in the uk for 2023 - 2024.
uk_interest = 0.077

# Average federal student loan interest rate in United States for
# 2023 - 2024 for undergraduates (loan type direct).
us_interest_one = 0.055

# Average federal student loan interest rate in United States for
# 2023 - 2024 for graduate & professional (loan type direct).
us_interest_two = 0.0705

# Average federal student loan interest rate in United States for
# 2023 - 2024 parent, graduate & professional (loan type PLUS).
us_interest_three = 0.0805

# ---------------Heading---------------

printline()
print_heading("Welcome to Student Finance Calculator!")
printline()

# ---------------Main Code---------------

while True:
    # Take input of student debt total and convert to float.
    try:
        curr_debt = float(input("Enter the total debt amount on your last student finance statement: "))
    except ValueError:
        # If input is not a numeric value for convert to a float, print error.
        printline()
        print("ERROR: Please enter a numeric value.")
        printline()
        # Re-ask user for input.
        curr_debt = float(input("Enter the total debt amount on your last student finance statement: "))
        pass

        # List of countries in this calculator.
    print("\nList of countries you can calculate:\n\
1 - Australia\n\
2 - New Zealand\n\
3 - Sweden\n\
4 - United Kingdom\n\
5 - United States\n")
    country = input("Enter the country where you took out your government backed student loan: ")

    # Calculation for Australia.
    if country == '1':
        while True:
            debt_calculator(a_interest)
            break

    # Calculation for New Zealand.
    elif country == '2':
        while True:
            nz_resident = input("\nHave you moved out of New Zealand since graduating? Y/N: ")
            nz_resident = nz_resident.lower()
            # Student loans only have interest for New Zealand citizens who
            # move abroad after graduating.
            if nz_resident == 'y':
                debt_calculator(nz_interest)
                break

            # Student loans are interest-free for New Zealand citizens who
            # don't move abroad after graduating.
            elif nz_resident == 'n':
                debt_calculator(0)
                break

            else:
                # Error Handling, repeats question if input out of range.
                print("\nERROR: Enter 'Y' or 'N'.")
                pass

    # Calculation for Sweden.
    elif country == '3':
        while True:
            debt_calculator(s_interest)
            break

    # Calculation for United Kingdom.
    elif country == '4':
        while True:
            debt_calculator(uk_interest)
            break

    # Calculation for United States.
    elif country == '5':   
        while True:
            us_loan_type = input("\nWas yor student loan a private loan or a federal loan?\n\
1 - Private\n\
2 - Federal\n\
Enter either '1' or '2': ")
            
            '''This calculator can only calculate student loans which
            are government backed, as private student loans interest
            rates vary much more and this would become a much bigger
            calculator if it also included private interest rates.'''
            if us_loan_type == '1':
                printline()
                print("ERROR: Rates vary dependant on Provider, unfortunately we can not calculate this.")
                printline()
                break

            elif us_loan_type == '2':
                while True:
                    fed_loan_type = input("\nIs your student loan type:\n\
1 - Undergraduate (loan type: direct)\n\
2 - Graduate & Professional (loan type: direct)\n\
3 - Parent, Graduate & Professional (loan type: PLUS)\n\
Enter either '1', '2', or '3': ")
        
                    # Calculation for United States undergraduate student loan.
                    if fed_loan_type == '1':
                        debt_calculator(us_interest_one)
                        exit()

                    # Calculation for United States graduate & professional
                    # student loan.
                    elif fed_loan_type == '2':
                        debt_calculator(us_interest_two)
                        exit()

                    # Calculation for United States parent, graduate &
                    # professional student loan.
                    elif fed_loan_type == '3':
                        debt_calculator(us_interest_three)
                        exit()

                    # Error Handling, repeats question if input out of range.
                    else:
                        print("\nERROR: Enter a number between 1-3.")

            # Error Handling, repeats question if input out of range. 
            else:
                print("\nERROR: Enter either '1' or '2'.")
                pass

    # Error Handling, repeats question if input out of range.
    else:
        print("\nERROR: Enter a country from the list.")
        continue
    
