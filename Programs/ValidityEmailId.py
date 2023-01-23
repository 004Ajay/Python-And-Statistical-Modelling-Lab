# PYTHON PROGRAM TO CHECK THE VALIDITY OF AN EMAIL BY VERIFYING IT'S FORMAT

def check_email(email):
    # example@gmail.com → example: username, gmail: vendor, com: domain
    if '@' not in email: return False

    username, partTwo = email.split('@') # Split the email into username & partTwo (gmail.com, icloud.com)
    vendor, domain = partTwo.split('.') # Splits the partTwo into vendor & domain

    invalid_chars = set(" !#$%^&*()+={}[]|\;'\"<>,?/")  # Check for invalid characters in username
    valid_vendors = ['gmail', 'yahoo', 'icloud'] # These are some samples, can have other too...
    valid_doamins = ['com', 'edu', 'gov', 'org']

    if any(each_letter in invalid_chars for each_letter in username): return False
    # if any(char in invalid_chars for char in username): return False
    if vendor not in valid_vendors: return False # Check for invalid vendors
    if domain not in valid_doamins: return False # Check for invalid doamins
    return True # if all cases are true

# Testing
print(check_email("example@gmail.com")) # True
print(check_email("invalid.email")) # False