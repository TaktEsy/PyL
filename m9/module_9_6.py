def all_variants(text):
    length = len(text)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]


g = all_variants('abc')
print(g)
for i in g:
    print(f'Значение генератора: {i}')
print()