import requests
import csv
import os
import sys

API_KEY = sys.argv[1] if len(sys.argv) > 1 else None

url = f'https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount?AccountAPIKey={API_KEY}'

response = requests.get(url)

data = []

if response.status_code == 200:
    data = response.json()
else:
    print('Error: ', response.status_code)

with open('facility_count.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    row = []
    for facility in data:
        # append location name, last updated date and time, total capacity, and last count
        row.append(facility['LocationName'])
        row.append(facility['LastUpdatedDateAndTime'])
        row.append(facility['TotalCapacity'])
        row.append(facility['LastCount'])
    writer.writerow(row)