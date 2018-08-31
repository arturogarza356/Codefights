def createDictionary(keys, values):
    i = 0
    dictionary = {}
    for key in keys:
        if key not in dictionary:
            dictionary[key] = [values[i]]
        else:
            dictionary[key].append(values[i])
        i +=1
    return dictionary

def checkForMultipleValues(dictionary):
        for key in dictionary:
            l = len(set(dictionary[key]))
            if l > 1:
                return -1
        return 1

def areFollowingPatterns(strings, patterns):
    dictionary1 = createDictionary(strings, patterns)
    dictionary2 = createDictionary(patterns, strings)
    if checkForMultipleValues(dictionary1) != 1 or checkForMultipleValues(dictionary2) != 1:
        return False
    return True
