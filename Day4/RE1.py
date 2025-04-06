"""Problem 1: Extract Valid Email Addresses
Description:
Write a Python program to extract all valid email addresses from a given text.
An email is considered valid if it follows this pattern: - Starts with alphanumeric
characters ([a-zA-Z0-9]) - May contain periods (.), underscores (_), or hyphens (-)
before the @ - Must contain an @ symbol - Domain name contains alphanumeric
characters, possibly hyphens (-) - Ends with a valid top-level domain (e.g., .com, .org,
.net, .edu, etc.)
Example Input:
text = "Contact us at support@example.com, john.doe123@company.org, or
invalid-email@com. Also, try jane_doe@domain.co.uk."
Expected Output:
['support@example.com', 'john.doe123@company.org', 'jane_doe@domain.co.uk']"""

import re

valid_email = r"^[a-z0-9._]+@[a-z0-9.]+\.[a-z]{2,}$"

emails = "Contact us at support@example.com, john.doe123@company.org, invalid-email@com. Also, try jane_doe@domain.co.uk"

valid_emails_are = re.findall(r"[a-z0-9._%]+@[a-z0-9.]+\.[a-z]{2,}", emails)

for email in valid_emails_are:
    if re.match(valid_email, email):
        print(email)
    else:
        print("no mails found")

