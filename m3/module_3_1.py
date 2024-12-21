calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string="Default"):
    count_calls()

    lg = string.__len__()
    up = string.upper()
    low = string.lower()

    return lg, up, low
def is_contains(string, list_to_search):
    count_calls()

    for i in list_to_search:
        if string.lower() in i.lower():
            return True


print(string_info(string="Новая строка",))
print(is_contains("Ban", ['ban', 'BaNaN', 'urBAN']))
print(calls)
