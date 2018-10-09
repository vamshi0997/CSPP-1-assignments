def cipher(text, key):
    str1 =''
    for i in text:
        if i.islower() == True:
            if i.isalpha() == True:
                n = ord(i) + key
                if n > 122:
                    n = 97 + (n-123)
                str1 = str1 + chr(n)
        elif i.isupper() == True:
            if i.isalpha() == True:
                n = ord(i) + key
                if n > 90:
                    n = 65 + (n-91)
                str1 = str1 + chr(n)
        else:
            str1 = str1 + i
    return str1

text = input("")
key = int(input(""))
print(cipher(text, key))