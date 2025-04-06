import re
import json
import logging
import re
# Set up logging (console output only)
class LaunchAuthorizationSystem:
    AUTH_PATTERN = r"^AUTH-[A-Z0-9]+-[0-9]+-[A-Z]+$"
    valid_code = "AUTH-XYZ123-4567-SECURE"
    not_valid_code = "AUTH-SECURE"

    if valid_code == AUTH_PATTERN
        print("access granted")
    else:
        print("access revoked")
    



 ””# Regex for security code validation
 @staticmethod
 def validate_code(code):
 """Validates the launch authorization code."""
     
