import requests

from getpass import getpass


token = getpass()
headers = {
    "Authorization": f"Bearer {token}",
    "Content-type": "application/json"
}


# GET request example
res = requests.get(url="http://localhost:8000/get", headers=headers)

if res.ok:
    print(res.content.decode())


# POST request example
payload = {"msg": "This is a test payload."}
res = requests.post(
    url="http://localhost:8000/post",
    json=payload,
    headers=headers
)
if res.ok:
    print(res.content.decode())
