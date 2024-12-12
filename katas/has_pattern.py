def has_pattern(text):
    onlyfirst = text[0:3]
    if onlyfirst == 'abc':
        return True
    else:
        return False





print(has_pattern("abcdef"))  # True, "abc" is at the start
print(has_pattern("abxyz"))   # True, "abc" is at the start
print(has_pattern("zabcdef")) # False, "abc" is not at the start
print(has_pattern("xyz"))     # False, "abc" is not at the start


"""
To complete this exercise:
--------------------------
Implement the 'has_pattern' function to check if the text starts with the pattern "abc".

Exercise Breakdown:
-------------------
Use slicing to extract the first three characters of the text and compare them to "abc". 

"""
