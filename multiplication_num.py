# write a function for multiplication of numbers or floats from a list


li = [1, 3.4, 5, 6.5, "this", "is"]


def nums_multiplication(ls):
    multi = 1
    for i in range(0, len(ls)):
        if type(ls[i]) == int or type(ls[i]) == float:
            multi = ls[i] * multi
    return multi


print(nums_multiplication(li))
