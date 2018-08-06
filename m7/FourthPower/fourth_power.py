'''# Exercise: fourth power

# Write a Python function, fourthPower, that takes in one number
  and returns that value raised to the fourth power.

# You should use the square procedure that you defined in an earlier exercise
(you don't need to redefine square in this box;

# This function takes in one number and returns one number.'''

def fourthpower(x1_):
    '''
    x1_: int or float.
    '''
    return x1_**4


def main():
    ''' giving input to get its fourth power'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthpower(int(float(str(data)))))
    else:
        print(fourthpower(data))

if __name__ == "__main__":
    main()
