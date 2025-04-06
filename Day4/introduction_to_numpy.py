import numpy as np

ar = np.array([[1,2],[3,4]])
print(ar)

ar2 = np.arange(0, 10, 1)
print(ar2)

ar3 = np.linspace(0, 1, 100)
print(ar3)

print(ar @ ar)

import re  # Import the regular expression module

AUTH_PATTERN = r"^AUTH-[A-Z0-9]+-[0-9]+-[A-Z]+$"
valid_code = "AUTH-XYZ123-4567-SECURE"
not_valid_code = "AUTH-SECURE"

# Validate the valid_code
if re.match(AUTH_PATTERN, valid_code):
    print("Access granted")
else:
    print("Access revoked")

# Validate the not_valid_code (just for demonstration)
if re.match(AUTH_PATTERN, not_valid_code):
    print("Access granted")
else:
    print("Access revoked")
