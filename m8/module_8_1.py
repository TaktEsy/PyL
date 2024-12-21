
def add_everything_up(a,b):
    try:
        s = a + b
    except TypeError:
        a = str(a)
        b = str(b)
        return a+b
    else:
        return a+b

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
