def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]

str = str(input('Enter string to be reversed : '))
print('Reversed string is:', reverse_string(str))