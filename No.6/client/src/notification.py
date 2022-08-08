import requests

def discord(content):
    URL = "https://discord.com/api/webhooks/1006111410733977650/RvfguKrfU3qgFRUkEt0Rn4mjtUnOuf87tRKbl5-pXEIFmhYUXPONNEzEbLH3LFOxg8nz"
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        'content': content
    }

    return requests.post(URL, headers=header, json=data)