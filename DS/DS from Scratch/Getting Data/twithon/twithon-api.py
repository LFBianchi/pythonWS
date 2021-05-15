# twithon-api.py

import json
from twython import Twython

with open(".credentials.json", "r") as credentials:
    tokens = json.load(credentials)

print(tokens["access-token"], tokens["access-token-secret"])
    
twitter = Twython(tokens["access-token"], tokens["access-token-secret"])
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode("utf-8")
    text = status["text"].encode("utf-8")
    print(user, ": ", text)