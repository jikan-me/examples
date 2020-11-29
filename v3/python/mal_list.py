"""
This is not necessarily an example using Jikan,
but its a very common way to interact with a users list on MAL

On modern lists, you can use load.json with an offset to request
a users list. It accepts the same GET args as an animelist request

e.g.

https://myanimelist.net/animelist/Xinil?status=7

converts to

https://myanimelist.net/animelist/Xinil/load.json?offset=0&status=7
https://myanimelist.net/animelist/Xinil/load.json?offset=300&status=7
...

to request a users list in 300 entry chunks.

This is the same endpoint the /v3/user/ endpoint parses

You could similarly use any other status or parameter supported by modern lists on MAL
"""

# requires: pip3 install --user requests

# to request a users list, request 300 entry chunks till you dont receieve any more entries

import sys
import time

import requests


base_url = (
    "https://myanimelist.net/animelist/{username}/load.json?status=7&offset={offset}"
)


def request_chunk(username, offset):
    url = base_url.format(username=username, offset=offset)
    print("Requesting", url)
    resp = requests.get(url)
    if resp.status_code == 400:
        print("Could not get list for user {}".format(username), file=sys.stderr)
        print(resp.status_code, resp.text, file=sys.stderr)
        sys.exit(1)
    return resp.json()


def request_animelist(username):
    all_entries = []
    offset = 0
    while True:
        entries = request_chunk(username, offset)
        all_entries.extend(entries)
        # if the number of entries is less than 300, we've exhausted all paginations
        if len(entries) < 300:
            break
        time.sleep(3)
        offset += 300
    return all_entries


# example usage
if __name__ == "__main__":
    animelist = request_animelist("Xinil")
    print("Animelist Entry Count:", len(animelist))
    print("First Entry:", animelist[0]["anime_title"])
