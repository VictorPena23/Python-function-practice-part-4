# Write a Python function called max_num() to find the maximum of three numbers.
def max_num(a,b,c):
    print(max(a,b,c))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i
    return print(prod)