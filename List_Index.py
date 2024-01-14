# write a function that will be able to print the index of list without using an index function

li = [1, 2, 3, 5, "this", "is"]


def list_index(list):
    for i in range(0, len(list)):
        print(" index of ", list[i], " is : ", i)


list_index(li)
