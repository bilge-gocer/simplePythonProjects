def bubble_sort(alist1):
    for passnum in range(len(alist1) - 1, 0, -1):
        for i in range(passnum):
            if alist1[i] > alist1[i + 1]:
                temp = alist1[i]
                alist1[i] = alist1[i + 1]
                alist1[i + 1] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
print(alist)
