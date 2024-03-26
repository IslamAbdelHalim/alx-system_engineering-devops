#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    username = user.get("username")

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user.get("id"): [
            {"task": task.get("title"),
             "completed": task.get("completed"),
             "username": username} for task in tasks]}, jsonfile)
