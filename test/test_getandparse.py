import requests

session_test = requests.session()
response_of_session = session_test.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print("Tipo de dato:", type(response_of_session))
print("Tipo de dato:", type(response_of_session.json()))
print("Tipo de dato:", type(response_of_session.text))
print("\nBackend response in string below:\n ")
print(response_of_session.text)

print("\nBackend response in json below:\n ")
print(response_of_session.json())

print("\nget some parameter of json:\n ")
dict_of_json = response_of_session.json()["cookies"]
print(dict_of_json)

session_test.close()