# using Loop 
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result  # put each char in front
    return result
print(reverse_string("hello"))  # Output: "olleh"
