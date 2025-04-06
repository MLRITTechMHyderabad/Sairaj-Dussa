# main.py
import json
import logging
from authorization import LaunchAuthorizationSystem
# Set up logging (console output only)
class Warhead:
    
 """Represents a nuclear warhead with specific payload
information."""

 def __init__(self, warhead_id, type, yield_kt):
 self.warhead_id = warhead_id
 self.type = type
 self.yield_kt = yield_kt # Yield in kilotons
 def get_info(self):

class Submarine:
 """Controls the nuclear missile launch sequence."""

 def __init__(self, name, warhead_data):
 self.name = name
 self.warheads = [Warhead(**w) for w in warhead_data]
 def authorize_launch(self, auth_code):
 """Attempts to authorize and launch a missile."""

 """Simulates launching a missile."""

# JSON Data (Simulating a warhead payload inventory)
warhead_json = '''
[
 {"warhead_id": "W001", "type": "Thermonuclear", "yield_kt": 1000},
 {"warhead_id": "W002", "type": "Tactical", "yield_kt": 300}
]
'''
# Load warhead data
warhead_data = json.loads(warhead_json)
# Initialize submarine
submarine = Submarine("USS Trident", warhead_data)
# 🚀 Try launching with an incorrect code
submarine.authorize_launch("INVALID-123")
# 🚀 Try launching with a valid code
submarine.authorize_launch("AUTH-XYZ123-4567-SECURE")
