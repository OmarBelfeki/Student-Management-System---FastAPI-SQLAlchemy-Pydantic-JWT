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
        "id": 6,
        "user_id": 0,
        "dob": "2025-01-31",
        "class_id": 0,
        "create_at": "2025-01-31T12:28:57.198Z"
    }
    response = requests.post(url=f"{url}/students", json=data)

    if response.status_code == 201:
        print(f"[green]Student created successfully with ID {data['id']} at {datetime.datetime.now()}[/green]")
    else:
        print(f"[red]Failed to create student. Status code: {response.status_code}\n{response.json()}[/red]")


def update(id_: int) -> None:
    if not jab:
        print("[white]should you write an id example '''python test.py 0'''[/white]")
        return
    data = {
        "user_id": 0,
        "dob": "2025-05-02",
        "class_id": 0,
        "create_at": "2025-01-31T12:46:04.455Z"
    }
    old_student = requests.get(url=f"{url}/students/{id_}")
    if old_student.status_code == 404:
        print(f"[yellow]Student Not Found [/yellow]")
        return

    response = requests.put(url=f"{url}/students/{id_}", json=data)
    if response.status_code == 200:
        print(f"[green]Student Updated successfully with ID {id_} at {datetime.datetime.now()}[/green]")
        print(f"[blue] ==>old student : {old_student.json()}[/blue]")
        print(f"[blue] ==>student : {response.json()}[/blue]")
    else:
        print(f"[red]Failed to update student. Status code: {response.status_code}\n{response.content}[/red]")

def get_by_id(id_: int):
    if not jab:
        print("[white]should you write an id example '''python test.py 0'''[/white]")
        return
    response = requests.get(url=f"{url}/students/{id_}")
    if response.status_code == 404:
        print(f"[yellow]Student Not Found [/yellow]")
        return
    if response.status_code == 200:
        print(f"[blue] ==>student : {response.json()}[/blue]")
    else:
        print(f"[red]Failed to get student. Status code: {response.status_code}\n{response.content}[/red]")


def get():
    response = requests.get(url=f"{url}/students/")
    if response.status_code == 404:
        print(f"[yellow]Student Not Found [/yellow]")
        return
    if response.status_code == 200:
        print(f"[blue] ==> students : {response.json()}[/blue]")
    else:
        print(f"[red]Failed to get student. Status code: {response.status_code}\n{response.content}[/red]")


def delete(id_: int):
    if not jab:
        print("[white]should you write an id example '''python test.py 0'''[/white]")
        return
    response = requests.delete(url=f"{url}/students/{id_}")
    if response.status_code == 404:
        print(f"[yellow]Student Not Found [/yellow]")
        return
    if response.status_code == 200:
        print(f"[blue] ==>{response.json()}[/blue]")
    else:
        print(f"[red]Failed to get student. Status code: {response.status_code}\n{response.content}[/red]")


if __name__ == "__main__":
    print("[orange]=====create a student=====[/orange]")
    print("[black]==================================[/black]")
    create()
    print("[black]==================================[/black]")
    print("[orange]=====get all student=====[/orange]")
    print("[black]==================================[/black]")
    get()
    print("[black]==================================[/black]")
    print("[orange]=====get a student by ID=====[/orange]")
    print("[black]==================================[/black]")
    get_by_id(_id)
    print("[black]==================================[/black]")
    print("[orange]=====update=====[/orange]")
    print("[black]==================================[/black]")
    update(_id)
    print("[black]==================================[/black]")
    print("[orange]=====delete=====[/orange]")
    print("[black]==================================[/black]")
    delete(_id)
    print("[black]==================================[/black]")
