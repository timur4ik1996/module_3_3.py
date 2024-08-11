def print_params(a=1, b="строка", c=True):
    print(a, b, c)
    print(a, b)
    print()
    print(a, c)
    print()
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
def print_params(a=1, b="строка", c=True):
    print(a,b,c)
values_list = [3, "name", False]
print_params(*values_list)
def print_params(a=1, b="строка", c=True):
    print(a,b,c)
values_dict = {'a':1, 'b': 'строка', 'c':True}
print_params(**values_dict)
def print_params(a=1, b="строка", c=True):
    print(a, b, c)
values_list2 = [54.32, "Строка"]
print_params(*values_list2, 42)
