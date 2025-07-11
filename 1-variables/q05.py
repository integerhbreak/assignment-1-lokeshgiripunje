# Task:
# Swap two variables using a temporary variable.

# Your code goes here
previous_location = 'UK'
current_location = 'India'
print(f'I was in {previous_location} and moved back to {current_location} 2 years ago.')


# Temporary variable
temp_variable = previous_location
previous_location = current_location
current_location = temp_variable
# Swap previous and current location using temporary variable temp_variable and print same print statement.
print(f'I was in {previous_location} and moved back to {current_location} 2 years ago.')