# write a program which will find the length of the given string without using the len function

# print(len("sid"))


def find_length(s):
    count = 0
    for i in s:
        count = count + 1
    return count


string = input("enter the string : ")

print(find_length(string))

