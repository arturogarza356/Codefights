def firstNotRepeatingCharacter(s):
    res = "_"
    for letter in s:
        if s.count(letter) == 1:
            res = letter
            break
    return res
