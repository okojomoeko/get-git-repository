import requests
import os
import sys
import json
import re
from pathlib2 import Path


def get_repository(username, accesstoken, visibility="all", page="1"):

    params = (
        ('per_page', '100'),
        ('visibility', visibility),
        ('page', page),
    )
    
    response = requests.get('https://api.github.com/user/repos', params=params, auth=(username, accesstoken))
    return response.json()


def main():
    _path = Path(input("Path to clone: "))
    if not _path.is_absolute():
        if str(_path) == ".":
            path = str(Path.cwd())
        elif re.match("^~/*", str(_path)):
            path = str(_path).replace("~", str(Path.home()))
            
        else:
            print("Input correct directory")
            return
    else:
        path = str(_path)

    print("Your path: {0}\n".format(path))
    if not Path(path).exists():
        res = input("Choose directory is not exist. Create directory?[y/n]: ").lower()
        if res == "y":
            os.mkdir(path)
        elif res == "n":
            print("Input correct directory")
            return

    username = input("Username: ")
    accesstoken = input("Accesstoken: ")

    idx = 1
    _data = []
    while True:
        temp = get_repository(username, accesstoken, page=idx)
        if temp == []:
            break
        else:
            _data.append(temp)
        idx += 1
    
    repos = os.listdir(path)

    os.chdir(path)
    result = "\n\n"
    print("-----Start Cloning-----\n")
    for data in _data:
        for d in data:
            if d not in repos:
                os.system("git clone "+d["clone_url"])
                result += "Cloned repository: {0}\n".format(d["name"])

    print(result)

if __name__ == "__main__":    
    main()