from true_math import divide as true_divide
from fake_math import divide as fake_divide

print(true_divide(10, 2))
print(true_divide(10, 0))
print(fake_divide(25, 5))
print(fake_divide(25, 0))