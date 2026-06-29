import requests

url = "https://api.example.com/orders"

headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.HTTPError:
    print("HTTP Error")

except requests.exceptions.RequestException as e:
    print(f"API Request Failed: {e}")