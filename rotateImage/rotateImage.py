def rotateImage(a):
    i = 0
    lst2 = []
    while i < len(a):
        lst1 = [item[i] for item in a]
        lst1.reverse()
        lst2.append(lst1)
        i+=1
    return lst2
