import requests

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("API Failed")
    
    
# if no internet connection

try:
    response = requests.get(url)
    print(response.status_code)

except Exception as e:
    print(e)
    
# raise for status 

try:
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

except requests.exceptions.HTTPError:
    print("HTTP Error")
    
# we use timeout to avoid waiting for too long for a response from the server
response = requests.get(
    url,
    timeout=10
)

# retry- when failed api -- we do retry bcz the pipeline can get failed if not run 
for attempt in range(3):

    try:

        response = requests.get(url)

        response.raise_for_status()

        break

    except:

        print("Retrying...")
        
        