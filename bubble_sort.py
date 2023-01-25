def bubble_sort(list):
    it = 0
    while it < len(list):
        for i in range(len(list) - it - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                yield list

        it = it + 1
