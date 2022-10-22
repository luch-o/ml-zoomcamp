import requests

host = ""
url = f"http://{host}/predict"

client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

r = requests.post(url, json=client)
print(r.json())
