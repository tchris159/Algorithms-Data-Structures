def assignLetters(grades):
    ans = {}
    ans['A'] = 0
    ans['B'] = 0
    ans['C'] = 0
    ans['D'] = 0
    ans['F'] = 0

    for grade in grades:
        if grade >= 90:
            ans['A'] += 1
        elif grade >= 80:
            ans['B'] += 1
        elif grade >= 75:
            ans['C'] += 1
        elif grade >= 66:
            ans['D'] += 1
        else:
            ans['F'] += 1
    return ans
