import json
import os
from string import Template
data_file = open('start_end_points.txt', 'r')
access_string = "curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" https://test.api.amadeus.com/v1/security/oauth2/token -d \"grant_type=client_credentials&client_id=AHNK4Z09Y1liwy9Y8HMkIL29bU3IHIKD&client_secret=kuLF1ihHaO9tldsb\""
access_data = json.loads(os.popen(access_string).read())['access_token']
query_string = Template("curl -X GET -H 'Authorization: Bearer $access_token' \"https://test.api.amadeus.com/v1/shopping/flight-dates?origin=$origin&destination=$destination&oneWay=true&departureDate=$start,$end\"")
start = "2019-09-20"
end = "2019-10-10"

f = open('flight_data.json', 'a+')

with open('start_end_points.txt', 'r') as data_file:
    line = data_file.readline()
    while line:
        print(line)
        points = line.split()
        q_s = query_string.substitute(access_token= access_data, origin= points[0], destination= points[1], start = start, end = end)
        flight_data = os.popen(q_s).read()
        f.write(flight_data)
        line = data_file.readline()

data_file.close()
f.close()












