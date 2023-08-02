def is_palindrome(str):
    startIndex = 0
    endIndex = len(str)-1
    for x in str:
        if str[startIndex] == str[endIndex]:
            return True
    return False


print(is_palindrome('racecars'))
