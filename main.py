import requests

# make a https POST request to  https://dulcespalabras.com/api/user/mia-data
# add Authorization: Bearer 2c320649-f50c-4cab-b091-036a7184b5f2


url = 'https://dulcespalabras.com/api/user/mia-data'

headers = {
    'Authorization': 'Bearer 2bc15e99-6b57-41d4-babe-d5085a6cf22d'
}

response = requests.post(url, headers=headers)

# print the response

print(response.text)
