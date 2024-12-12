def is_subscriber_matching(subscriber_name, actual_name):
    if str.lower(subscriber_name) == str.lower(actual_name):
        return True
    else:
        return False


result = is_subscriber_matching("John Doe", "john doe")
print(result)  # Expected output: True

result = is_subscriber_matching("Jane Smith", "JANE SMITH")
print(result)  # Expected output: True

result = is_subscriber_matching("Charlie Brown", "Charlie Pink")
print(result)  # Expected output: False

"""
To complete this exercise:
--------------------------
Implement the 'is_subscriber_matching' function to check if a subscriber's name matches the actual name without considering their case. 


Exercise Breakdown:
-------------------
The `str.lower()` method in Python converts all characters in a string to lowercase. 
"""
