cursor = None

while True:

    response = requests.get(url, params={
        "cursor": cursor,
        "limit": 100
    })

    data = response.json()

    process(data["orders"])

    cursor = data["next_cursor"]

    if cursor is None:
        break