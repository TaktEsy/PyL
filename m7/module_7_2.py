def custom_write(name, strs=None):
    lstr = []
    pstr = []
    with open(name, 'w', encoding='utf-8') as file:
        stroka = 0
        for s in strs:
            stroka += 1
            byte = file.tell()
            f = (stroka, byte)
            pstr.append(f)
            file.write(s + '\n')
            lstr.append(s)
        file.close()

    strings_positions = dict(zip(pstr, lstr))

    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

print(custom_write('text1_7_3.txt', strs=info))

print()