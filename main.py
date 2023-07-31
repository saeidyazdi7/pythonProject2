# Define a string and a character
string = "Hello world"
character = "H"

# Use lambda function to check if the string starts with the character
result = lambda x, y: x.startswith(y)

# Print the result
print("The string", string, "starts with the character", character, ":", result(string, character))

# Output:
# The string Hello world starts with the character H : True