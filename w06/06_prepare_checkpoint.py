print('Provide answers between 1 and 10 for each of these questions:')

loan_size = int(input('Between 1 and 10, how large is the loan? '))
credit_status = int(
    input('Between 1 and 10, how good is your credit history? '))
income = int(input('Between 1 and 10, how high is your income? '))
down_payment = int(input('Between 1 and 10, how large is your down payment? '))

should_loan = False

if (loan_size >= 5):
    if (credit_status >= 7 and income >= 7):
        should_loan = True
    elif (credit_status >= 7 or income >= 7):
        if (down_payment >= 5):
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if (credit_status < 4):
        should_loan = False
    elif (income >= 7 or down_payment >= 7):
        should_loan = True
    elif (income >= 4 and down_payment >= 4):
        should_loan = True
    else:
        should_loan = False

if should_loan:
    print("Decision: yes")
else:
    print("Decision: no")
