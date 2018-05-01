import urllib.parse
import requests


main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Address: ')

    if address == 'quit' or address == 'q':
        break
    url = main_api + urllib.parse.urlencode({'address':address}) #don't let blank spaces

    json_data = requests.get(url).json()

    json_status = json_data['status']
    print('API status: ' + json_status + '\n')

    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])
        formatted_address = json_data['results'][0]['formatted_address']
        print(formatted_address)
