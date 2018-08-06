''' Docstring
using bisection '''


def payingdebtoffinayear(balance, annualinterestrate):
    ''' in function'''
    epsilon_ = 0.000001
    min1 = balance/12
    max1 = balance * ((1+(annualinterestrate/12))**12)/12
    pay1_ = (min1+max1)/2
    while True:
        bc_ = balance
        for i in range(12):
            i = i+1
            ub_ = bc_ - pay1_
            bc_ = ub_ + (annualinterestrate * ub_ / 12)
        if bc_ > 0 and bc_ > epsilon_:
            min1 = pay1_
        elif bc_ < 0 and bc_ < -1*epsilon_:
            max1 = pay1_
        else:
            return (round(pay1_, 2))
        pay1_ = (min1+max1)/2




def main():
    ''' you are in main '''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", payingdebtoffinayear(data[0],data[1]))
    
if __name__ == "__main__":
    main()

