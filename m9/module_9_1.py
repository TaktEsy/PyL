def apply_all_func(int_list, *func):
    res = dict()
    for f in func:
        if (f.__name__ == 'max'):
            res.update({'max': max(int_list)})
            continue
        elif (f.__name__ == 'min'):
            res.update({'min': min(int_list)})
            continue
        elif (f.__name__ == 'len'):
            res.update({'len': len(int_list)})
            continue
        elif (f.__name__ == 'sum'):
            res.update({'sum': sum(int_list)})
            continue
        elif (f.__name__ == 'sorted'):
            res.update({'sorted': sorted(int_list)})
    return res

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print()