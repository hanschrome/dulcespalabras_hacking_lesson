import requests

# make a https POST request to  https://dulcespalabras.com/api/user/mia-data
# add Authorization: Bearer 2c320649-f50c-4cab-b091-036a7184b5f2


url = 'https://dulcespalabras.com/api/user/mia-data'

headers = {
    'Authorization': 'Bearer ee4d4a28-4aa3-4058-93a7-c9150fa39a0c'
}

response = requests.post(url, headers=headers)

# print the response

print(response.text)
