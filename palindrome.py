

def palindrome():
    str = input("please input the word:")
    reversedstr = ''
    lowstr = str.lower()

    for index in range(len(lowstr)-1,-1,-1):
        #print(lowstr[index])
        reversedstr = reversedstr +  lowstr[index]

    if (reversedstr == lowstr):
        return "the word is palindrome"
    else:
        return "the word is not plindrome"


print(palindrome())
