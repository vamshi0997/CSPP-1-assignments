'''#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9]
#into [2, -3, 9, -8]'''


def inc(num):
    '''
    num: each list input
    '''
    return num+1

def apply_to_each(list2, fuc):
    '''adding function to every list element'''
    return list(map(fuc, list2))

def main():
    '''
    data:input can lbe any integer'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
