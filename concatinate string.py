def reverse_full_name(first_name, last_name):
    # Concatenate the last_name and first_name with a comma and space
    full_name = last_name + ", " + first_name
    # Reverse the concatenated string
    reversed_name = full_name[::-1]
    # Return the reversed string
    return reversed_name

# Example usage
result = reverse_full_name("Kinyanjui", "Wanjiru")
print(result)  # Output: "urijnaW ,yraM"
