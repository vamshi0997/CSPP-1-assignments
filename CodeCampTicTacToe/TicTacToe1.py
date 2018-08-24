
def decide(count1, count2):
    '''deciding which letter to print'''
    if count1 >= 2 or count2 >= 2 or (count1 == 1 and count2 == 1):
        print("invalid game")
        exit()
    elif count1 == 1:
        print("x")
        exit()
    elif count2 == 1:
        print("o")
        exit()
    else:
        print("draw")
        exit()

def game(check):
    '''enter into the game'''
    count1 = 0
    count2 = 0
    temp = []
    temp1 = []

    for i in range(3):
        for j in range(3):
            if i == j:
                temp = temp + [check[i][j]]
    num1 = temp.count('x')
    num2 = temp.count('o')
    if num1 == 3:
        count1 = 1
    elif num2 == 3:
        count2 = 1

    temp1 = temp1 + [check[0][2]] + [check[1][1]] + [check[2][0]]
    cou1 = temp1.count('x')
    cou2 = temp1.count('o')
    if cou1 == 3:
        count1 += 1
    elif cou2 == 3:
        count2 += 1
    i = 0
    j = 0
    while i < 3:
        temp = []
        for j in range(3):
            temp = temp + [check[i][j]]
        num1 = temp.count('x')
        num2 = temp.count('o')
        if num1 == 3:
            count1 += 1
        elif num2 == 3:
            count2 += 1
        i = i + 1

    i = 0
    j = 0
    while j < 3:
        temp = []
        for i in range(3):
            temp = temp + [check[i][j]]
        num1 = temp.count('x')
        num2 = temp.count('o')
        if num1 == 3:
            count1 += 1
        elif num2 == 3:
            count2 += 1
        j = j + 1

    decide(count1, count2)

def main():
    ''' take the input in for of list'''
    list2 = []
    for i in range(3):
        list1 = input().split(" ")
        for j in list1:
            if j not in 'xo.':
                print("invalid input")
                exit()
        list2 = list2 + [list1]
    game(list2)

if __name__ == '__main__':
    main()
