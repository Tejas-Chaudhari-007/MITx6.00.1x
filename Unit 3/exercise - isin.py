def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if len(aStr) <= 1:
        return char == aStr
    else:
        mid_idx = len(aStr) // 2
        return isIn(char, aStr[:mid_idx]) if char < aStr[mid_idx] else isIn(char, aStr[mid_idx:])


print(isIn('g', 'abcdef'))
