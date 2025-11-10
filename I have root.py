def have_root(array):

    for i in range(1, len(array) - 1):
        if array[i] * array[i] != array[i + 1]:
            return False
    
    return True

array = eval(input())
print(have_root(array))