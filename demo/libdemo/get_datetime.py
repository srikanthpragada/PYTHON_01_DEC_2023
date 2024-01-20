import requests

resp = requests.get("https://worldtimeapi.org/api/timezone/asia/kolkata")
details = resp.json() # Convert JSON to dict
print('Kolkata : ', details['datetime'])

resp = requests.get("https://worldtimeapi.org/api/timezone/europe/rome")
details = resp.json() # Convert JSON to dict
print('Rome : ', details['datetime'])

