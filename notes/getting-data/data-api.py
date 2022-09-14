import requests, json

github_user = "alejoboga20"
endpoint = f"https://api.github.com/users/{github_user}/repos"

repos = json.loads(requests.get(endpoint).text)
print(repos)