def bubble_sort(to_sort):
    it = 0
    while it < len(to_sort):
        for i in range(len(to_sort) - it - 1):
            if to_sort[i] > to_sort[i+1]:
                to_sort[i],to_sort[i+1] = to_sort[i+1],to_sort[i]
                yield to_sort
        
        it = it + 1