# str = str(input('Enter any word to check for palindrome : '))
def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True

print(isPalindrome('racecar'))
print(isPalindrome('thor'))