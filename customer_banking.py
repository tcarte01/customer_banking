# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = input("Enter your current savings balance: ")
    savings_interest = input("Enter your interest Rate: ")
    savings_maturity = input("How Many Months Would You Like To Forecast?: ")


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(float(savings_balance), float(savings_interest), int(savings_maturity))

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("#" * 25)
    print(f'You will earn {interest_earned:,.2f} over the next {savings_maturity} months! Your updated savings account balance will be: {updated_savings_balance:,.2f}')
    print("#" * 25)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input("Enter your Current CD Balance: ")
    cd_interest = input("Enter your interest Rate: ")
    cd_maturity = input("How Many Months Would You Like to Forecast?: ")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(float(cd_balance), float(cd_interest), int(cd_maturity))

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("#" * 25)
    print(f'You will earn {interest_earned:,.2f} over the next {cd_maturity} months! Your updated CD Account balance will be: {updated_cd_balance:,.2f}')
    print("#" * 25)

if __name__ == "__main__":
    # Call the main function.
    main()
