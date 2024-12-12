def is_palindrome(number):
    # Convert number to string
    number_str = str(number)
    # Check if the string is equal to its reverse
    if number_str == number_str[::-1]:
        return True
    else:
        return False


result = is_palindrome(12321)
print(result)  # Expected output: True

result = is_palindrome(12345)
print(result)  # Expected output: False

result = is_palindrome(1001)
print(result)  # Expected output: True

result = is_palindrome(1)
print(result)  # Expected output: True

"""
To complete this exercise:
--------------------------
Implement the 'is_palindrome' function to check if a number is a palindrome.


Exercise Breakdown:
-------------------
To reverse the string the `[::-1]` slice can be used.  
"""