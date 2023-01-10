"""Connection functions package."""

import requests


def get_token(url, user, password):
    data = {"user": user, "password": password}
    token = requests.get(f"{url}/login", json=data)
    return token
