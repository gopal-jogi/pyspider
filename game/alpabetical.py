# Input string
input_string = "gopal"

# Convert the string to a list of characters
chars_list = list(input_string)

# Bubble sort implementation
n = len(chars_list)
for i in range(n):
    for j in range(0, n-i-1):
        if chars_list[j] > chars_list[j+1]:
            chars_list[j], chars_list[j+1] = chars_list[j+1], chars_list[j]

# Join the sorted characters back into a string
sorted_string = ''.join(chars_list)

# Print the sorted string
print(sorted_string)
