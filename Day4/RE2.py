"""Problem 2: Extract Hashtags from a Tweet
Description:
Write a Python program to extract all hashtags (#hashtag) from a given text.
- A hashtag: - Starts with # - Followed by letters, numbers, or underscores (_) - Cannot
contain spaces or special characters (@, !, $, etc.)
Example Input:
tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"
Expected Output:
['#Python', '#coding', '#100DaysOfCode', '#Regex_Challenge']"""


import re

expression = r"#[a-zA-Z0-9_]+[a-zA-Z0-9]"

tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"

condition = re.findall(expression, tweet)

for hashtags in condition:
    if re.match(expression, hashtags):
        print(hashtags)
    else:
        print("no hashtags found!!!")
