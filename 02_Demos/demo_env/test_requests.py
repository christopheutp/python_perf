import requests

# faire une requete FET sur une API public
response = requests.get("https://api.github.com")

print("Status code : ",response.status_code)
print("Content-Type :",response.headers.get("Content-Type"))

data = response.json()
print("Cles principales du JSON: ",list(data.keys()))