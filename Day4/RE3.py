"""Problem 3: Validate a Strong Password
Description:
Write a Python program to check if a password is strong based on these rules:

1. At least 8 characters long
2. Contains at least one uppercase letter (A-Z)
3. Contains at least one lowercase letter (a-z)
4. Contains at least one digit (0-9)
5. Contains at least one special character (@, $, !, %, *, ?, &)

Example Inputs & Outputs:
passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1",
"Secure#123"]
Expected Output:
WeakPass -> Invalid
Str0ng@Pass -> Valid
NoSpecial1 -> Invalid
short!1 -> Invalid
Secure#123 -> Valid"""

import re

#pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$"

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"


passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1", "Secure#123"]

for password in passwords:
    if re.match(pattern, password):
        print(f"{password} -> Valid")
    else:
        print(f"{password} -> Invalid")

