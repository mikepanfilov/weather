import requests

offices = ['Лондон', 'Шереметьево', 'Череповец']

params = {
  '0':'',
  'n':'',
  'q':'',
  'm':'',
  'lang':'ru'
}
for office in offices:
  url = 'https://wttr.in//{}'.format(office)
  response = requests.get(url, params=params)
  response.raise_for_status()
  print(response.text)