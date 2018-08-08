'''#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given
#testList = [1, -4, 8, -9] into [1, 16, 64, 81]'''

def square(num):
    '''
    num: each list input
    '''
    return num**2

def apply_to_each(list2_, fuc):
    '''adding function to every list element'''
    return list(map(fuc, list2_))

def main():
    '''data: any integer'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
