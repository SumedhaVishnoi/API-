import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response)

# sending query parameters 
params = {
    "page":2
}

response = requests.get(
    url,
    params=params
)

# multiple query parameter 
params = {
    "city":"Delhi",
    "page":2
}

# for authentication sending hearders
headers = {
    "Authorization":"Bearer abc123"
}

response = requests.get(
    url,
    headers=headers
)

# POST request with data
payload = {
    "name":"Sumi",
    "city":"Delhi"
}

response = requests.post(
    url,
    json=payload
)

# PUT request - completely change the data 
payload = {
    "name":"Sumi Sharma",
    "city":"Mumbai"
}

response = requests.put(
    url,
    json=payload
)

# PATCH request - partially change the data
payload = {
    "city":"Mumbai"
}

response = requests.patch(
    url,
    json=payload
)

