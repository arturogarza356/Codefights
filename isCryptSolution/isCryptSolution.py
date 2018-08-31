def isCryptSolution(crypt, solution):
    crypt1 = ""
    crypt2 = ""
    crypt3 = ""
    for letter in crypt[0]:
        i2 = 0
        while i2 < len(solution):
            if letter in solution[i2]:
                crypt1 += solution[i2][1]
                break
            i2 +=1
    for letter in crypt[1]:
        i2 = 0
        while i2 < len(solution):
            if letter in solution[i2]:
                crypt2 += solution[i2][1]
                break
            i2 +=1
    for letter in crypt[2]:
        i2 = 0
        while i2 < len(solution):
            if letter in solution[i2]:
                crypt3 += solution[i2][1]
                break
            i2 +=1
    number1 = int(crypt1)
    number2 = int(crypt2)
    number3 = number1 + number2
    finalCrypt = ""
    if crypt1[0] == "0" or crypt2[0] == "0":
        finalCrypt += "0"
    if number3 == 0:
        finalCrypt = "0"
    else:
        finalCrypt += str(number3)
    if finalCrypt == crypt3:
        return True
    else:
        return False
