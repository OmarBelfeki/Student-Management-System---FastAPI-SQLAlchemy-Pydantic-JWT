import datetime
import sys
from rich import print
import requests

url = "http://127.0.0.1:8000"
try:
    _id = int(sys.argv[1])
    jab = True
except:
    jab = False
    _id = 0


def create():
    data = {
        "id": 0,
        "name": "string",
        "email": "user@example.com",
        "password": "string",
        "role": "Teacher"
    }
    response = requests.post(url=f"{url}/auth/register", json=data)

    if response.status_code == 201:
        print(f"[green]user created successfully with ID {data['id']} at {datetime.datetime.now()}[/green]")
    else:
        print(f"[red]Failed to create user. Status code: {response.status_code}\n{response.json()}[/red]")


def update(id_: int) -> None:
    if not jab:
        print(f"[white]should you write an id example '''python test.py 0'''[/white]")
        return
    data = {
        "id": 0,
        "name": "omar",
        "email": "user@example.com",
        "password": "string",
        "role": "Student",
        "created_at": "2025-01-31T13:31:40.702Z"
    }
    old_user = requests.get(url=f"{url}/auth/users/{id_}")
    if old_user.status_code == 404:
        print(f"[yellow]user Not Found [/yellow]")
        return

    response = requests.put(url=f"{url}/auth/users/{id_}", json=data)
    if response.status_code == 200:
        print(f"[green]user Updated successfully with ID {id_} at {datetime.datetime.now()}[/green]")
        print(f"[blue] ==>old user : {old_user.json()}[/blue]")
        print(f"[blue] ==>user : {response.json()}[/blue]")
    else:
        print(f"[red]Failed to update user. Status code: {response.status_code}\n{response.content}[/red]")

def get_by_id(id_: int):
    if not jab:
        print("[white]should you write an id example '''python test.py 0'''[/white]")
        return
    response = requests.get(url=f"{url}/auth/users/{id_}")
    if response.status_code == 404:
        print(f"[yellow]user Not Found [/yellow]")
        return
    if response.status_code == 200:
        print(f"[blue] ==>user : {response.json()}[/blue]")
    else:
        print(f"[red]Failed to get user. Status code: {response.status_code}\n{response.content}[/red]")


if __name__ == "__main__":
    print("[orange]=====create a user=====[/orange]")
    print("[black]==================================[/black]")
    create()
    print("[black]==================================[/black]")
    print("[orange]=====get a user by ID=====[/orange]")
    print("[black]==================================[/black]")
    get_by_id(_id)
    print("[black]==================================[/black]")
    print("[orange]=====update=====[/orange]")
    print("[black]==================================[/black]")
    update(_id)
    print("[black]==================================[/black]")

