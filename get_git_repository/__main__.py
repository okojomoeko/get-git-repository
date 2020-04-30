import requests
import os
import re
from pathlib import Path
from getpass import getpass


def get_repository(username, accesstoken, visibility="all", page=1):

    params = (
        ('visibility', visibility),
        ('page', page),
        ('per_page', '100'),
    )

    response = requests.get('https://api.github.com/user/repos',
                            params=params, auth=(username, accesstoken))
    return response


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
        res = input(
            "Choose directory is not exist. Create directory?[y/n]: ").lower()
        if res == "y":
            os.mkdir(path)
        elif res == "n":
            print("Input correct directory")
            return

    username = input("Username: ")
    accesstoken = getpass("Accesstoken: ")

    idx = 1
    _data = []
    while True:
        response = get_repository(username, accesstoken, page=idx)
        status_code = response.status_code
        if status_code != requests.codes.ok:
            print("Error: {}".format(response.headers["status"]))
            return
        temp = response.json()
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
                result += "Cloned repository: {}\n".format(d["name"])

    print(result)


if __name__ == "__main__":
    main()
