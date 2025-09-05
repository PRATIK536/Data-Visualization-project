import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1,
    
}
headers = {
    'Content-type': 'application/json; charset=utf-8'
}
response = requests.post(url, headers=headers, json=data)

