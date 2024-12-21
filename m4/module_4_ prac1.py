nums = [35, 6, 8, 9, 10, 21, 1]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) -1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True

def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]

selection_sort(nums)
print(nums)
