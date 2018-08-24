
def decide(count1, count2):
    if count1 >= 2 or count2 >= 2 or (count1 == 1 and count2 == 1):
        print("invalid game")
        exit()
    elif count1 == 1:
        print("x")
        exit()
    elif count2 == 1:
        print("o")
        exit()
    else :
        print("draw")
        exit()



def game(check):
    count1 = 0
    count2 = 0
    temp = []
    temp1 = []

    for i in range(3):
        for j in range(3):
            if i == j:
                temp = temp + [check[i][j]]
    n1 = temp.count('x')
    n2 = temp.count('o')
    if n1 == 3:
        count1 = 1
    elif n2 == 3:
        count2 = 1

    temp1 = temp1 + [check[0][2]] + [check[1][1]] + [check[2][0]]
    c1 = temp1.count('x')
    c2 = temp1.count('o')
    if c1 == 3:
        count1 += 1
    elif c2 == 3:
        count2 += 1 

    i =0
    j = 0
    while i < 3:
        temp = [] 
        for j in range(3):
            temp = temp + [check[i][j]]
        n1 = temp.count('x')
        n2 = temp.count('o')
        if n1 == 3:
            count1 += 1
        elif n2 == 3:
            count2 += 1
        i = i + 1

    i = 0
    j = 0
    while j < 3:
        temp = []
        for i in range(3):
            temp = temp + [check[i][j]]
        n1 = temp.count('x')
        n2 = temp.count('o')
        if n1 == 3:
            count1 += 1
        elif n2 == 3:
            count2 += 1
        j = j + 1

    decide(count1, count2)

        

def main():
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
