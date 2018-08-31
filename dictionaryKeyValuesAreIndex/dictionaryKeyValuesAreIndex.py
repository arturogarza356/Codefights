def dictionaryKeyValuesAreIndex(keys):
    i = 0
    dictionary = {}
    for key in keys:
        if key not in dictionary:
            dictionary[key] = [i]
        else:
            dictionary[key].append(i)
        i +=1
    return dictionary

def checkForDiference(dictionary, k):
        for key in dictionary:
            l = len(dictionary[key])
            if l > 1:
                i = 0
                lowestValue = abs(dictionary[key][i] - dictionary[key][i+1])
                while i < len(dictionary[key]) -1:
                    if lowestValue > abs(dictionary[key][i] - dictionary[key][i+1]):
                        lowestValue = abs(dictionary[key][i] - dictionary[key][i+1])
                    if lowestValue <= k:
                        return 1
                    i+=1


        return -1
def containsCloseNums(nums, k):
    dictionary = dictionaryKeyValuesAreIndex(nums)
    if checkForDiference(dictionary, k) == 1:
        return True
    return False
