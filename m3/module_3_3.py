def print_params(a=1, b="Default", c=True):
    print(a, b, c)
print_params("New")
print_params()
print_params(b="New STR")
print_params(c=[1,2,3])

values_list = ["Unpacked", 3.14, "List"]
values_dict = {'a':9.1, 'b':"Unpacked", 'c':"DICT",}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [9, 0.75]
print_params(*values_list_2, 42)