# streaming-twython.py

import json
from twython import TwythonStreamer

tweets = []

with open(".credentials.json", "r") as credentials:
    tokens = json.load(credentials)

class MyStreamer(TwythonStreamer):
    """A subclass of the twython streamer that interacts with data our own way."""
    def on_success(self, data):
        if data["lang"] == "en":
            tweets.append(data)
        
        if len(tweets) > 1000:
            self.disconnect()
            
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconect()
        
stream = MyStreamer(tokens["access-token"], tokens["access-token-secret"])
stream.statuses.filter(track="data")