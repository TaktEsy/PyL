def is_prime(func):

    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        if s<2:
            print("Составное")
            return
        d = 2

        while d*d <= 5:
            if s%d == 0:
                print("Составное")
                return
            d+=1
        print("Простое")
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

res = sum_three(2, 3, 6)
print(res)


