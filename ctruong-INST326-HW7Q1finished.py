def histogram(grades):
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""

    for grade in grades:
        if grade >= 90:
            str1 += '*'
        if grade >= 80:
            str2 += '*'
        if grade >= 70:
            str3 += '*'
        else:
            str4 += '*'
    ans = ''
    ans += ("0-69", str4)
    ans += ("70-79", str3)
    ans += ("80-89", str2)
    ans += ("90+", str1)
    return ans

grades = ['100', '85', '54', '34', '89']

histogram(grades)
