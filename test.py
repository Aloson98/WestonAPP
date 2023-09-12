import requests

head = {
    "Authorization": "Token 2d0925cb1f6cb4b7cd4e6933bef0022613c063c4359f891a5009e65e54ebda90"
}

register = {
    "username": "mwaisaka",
    "password": "afya1234",
    "ward": "male medical"
}

urls = {
    'register': 'http://127.0.0.1:8000/roster/registration/',
    'login': 'http://127.0.0.1:8000/roster/login/',
    'ward-list': 'http://127.0.0.1:8000/roster/wards/',
}

data = {
    'username': 'mwaisaka',
    'password': 'afya1234'
}
req = requests.get(urls['ward-list'], headers=head )
print(req.text)
print(req.status_code)