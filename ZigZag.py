def zigzag(a): # a being a list
    i = 0
    currentZigzag = 0
    longestZigzag = 1

    while i < len(a) -1:

        if i == 0:
            if len(a) > 1 and (a[i] > a[i+1] or a[i] > a[i+1]):
                currentZigzag = 2
            else:
                currentZigzag = 1

        elif (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
            if currentZigzag > 2:
                currentZigzag += 1
            else:
                currentZigzag += 2
        else:
            currentZigzag = 1
        if currentZigzag > longestZigzag:
            longestZigzag = currentZigzag

        i +=1

    return longestZigzag

    return longestZigzag
