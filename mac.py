import requests
import sys


def get_company():
    mac_address = sys.argv[1]
    response = requests.get('https://api.macaddress.io/v1?apiKey=at_s7EEtgqYsYJqvHbjQLAepGOVKQSHZ&output=json&search={0}'.format(mac_address))
    dict_response = response.json()
    company = dict_response['vendorDetails']['companyName']
    print(company)


get_company()
