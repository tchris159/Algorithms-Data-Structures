def find_str(s, char):
    index = 0
    if (char==""):
        return 0

    elif char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:   # checks to see if char is equal to the segment in s
                    return index      #two conditions must be satisfied

            index += 1

    return -1    # no conditions are satisfied

print(find_str("finland", "land"))
print(find_str("sudan", "x"))
print(find_str("australia", "a"))
print(find_str("peru", "Peru"))
print(find_str("norway", "norway"))
print(find_str("laos", ""))