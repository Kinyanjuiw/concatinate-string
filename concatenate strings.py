def create_email_address(first_name, last_name, domain):
    # Use the passed parameters first_name and last_name
    email = (first_name + "." + last_name).lower()
    # Return the full email address
    return email + "@" + domain

# Example usage
email = create_email_address("Kinyanjui", "Wanjiru", "example.com")
print(email)  # Output: "kinyanjui.wanjiru@example.com"

    
    