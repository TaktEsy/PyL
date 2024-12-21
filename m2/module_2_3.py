my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0


while i < my_list.__len__():
    if my_list[i] >= 1:
        print(my_list[i])
    elif my_list[i] < 0 and my_list[i] != 0:
        break
    i += 1

