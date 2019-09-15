import os
import sys
import copy
import json
from string import Template
from datetime import datetime
from datetime import timedelta


def find_cheapest(flights):
    result_price = None
    result = None
    for x in flights:
        if(result_price == None or float(x['price']['total']) < float(result_price)):
            result = x
            result_price = float(x['price']['total'])
    return result


    for i in range(1, len(final_list)):


if(len(sys.argv) < 2 or len(sys.argv) > 9):

country_list = sys.argv[1:(len(sys.argv)-2)]
dates = sys.argv[len(sys.argv)-2:]

travel_dates = [dates[0]]
visited = []
result = []
origin = country_list[0]


avg_time = (datetime.strptime(dates[1], '%Y-%m-%d') - datetime.strptime(dates[0], '%Y-%m-%d')).days / (len(country_list))
next_leg = []

#add string to get access token automatically
access_string = "curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" https://test.api.amadeus.com/v1/security/oauth2/token -d \"grant_type=client_credentials&client_id=AHNK4Z09Y1liwy9Y8HMkIL29bU3IHIKD&client_secret=kuLF1ihHaO9tldsb\""
access_data = json.loads(os.popen(access_string).read())['access_token']
query_string = Template("curl -X GET -H 'Authorization: Bearer $access_token' \"https://test.api.amadeus.com/v1/shopping/flight-dates?origin=$origin&destination=$destination&oneWay=true&departureDate=$start,$end\"")


#need to fix:
    # shifting dates over so flights line up
    # moving from one country to next correctly

for i in country_list:
    if(i in visited):
        continue
    next_leg = []
    for j in country_list:
        if(j in visited or j == origin):
            continue
        start_date = datetime.strptime(travel_dates[-1], '%Y-%m-%d')
        end_date = start_date + timedelta(days=avg_time)
        start = start_date.strftime('%Y-%m-%d')
        end = end_date.strftime('%Y-%m-%d')
        q_s = query_string.substitute(access_token= access_data, origin= origin, destination= j, start = start, end = end)
        flight_data = json.loads(os.popen(q_s).read())
        try:
            best_flight = flight_data['data'][0]
            next_leg.append(best_flight)
        except:
            continue
    if(next_leg != []):
        trip = find_cheapest(next_leg)
        origin = trip['destination']
        visited.append(trip['origin'])
        result.append(trip)
        new_date = datetime.strptime(trip['departureDate'], '%Y-%m-%d') + timedelta(days=avg_time)
        new = new_date.strftime('%Y-%m-%d')
        travel_dates.append(new)


        
        

