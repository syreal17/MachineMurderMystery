import requests

payload = {'action': 'get_client_sequence_number', 'email': 'cpaivw@syreal.cc'}
r = requests.get('http://projectdecember.net/novemberServer/server.php', params=payload)

print(r.text)