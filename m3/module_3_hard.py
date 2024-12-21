data = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_len(*args):
    num_sum = 0

    for i in args:

        if isinstance(i, (list, tuple, set)):
            num_sum += sum_len(*i)

        elif isinstance(i, dict):
            num_sum += sum_len(*i.items())

        elif isinstance(i, (int, float)):
            num_sum += i

        elif isinstance(i, str):
            num_sum += len(i)

        elif i is None:
            pass

    return num_sum

print(sum_len(data))