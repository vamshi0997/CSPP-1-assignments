'''# Assignment-2 - Paying Debt off in a Year
# Now write a program that calculates the minimum fixed monthly
#payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month,
#but instead is a constant amount that will be
# paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# The program should print out one line:
# Lowest Payment: 180

# Assume that the interest is compounded monthly according to the balance at the end of the month.
# The monthly payment must be a multiple of $10 and is the same for all months.
#Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay. A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance = (Monthly unpaid balance) +(Monthly interest rate x Monthly unpaid balance)'''


def payingdebtoffinayear_(balance_, annualinterestrate_):
    ''' in function'''
    if balance_ < 0:
        return 0
    pay1_ = 10
    while True:
        bc_ = balance_
        for i in range(12):
            i = i+1
            unpaid_ = bc_ - pay1_
            bc_ = unpaid_ + ((annualinterestrate_*unpaid_/12))
        if bc_ <= 0.05:
            return pay1_
        pay1_ += 10 

def main():
    ''' missing doc function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", payingdebtoffinayear_(data[0], data[1]))

if __name__ == "__main__":
    main()
