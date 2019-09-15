import os
import sys
import copy
import json
from string import Template
from datetime import datetime
from datetime import timedelta


def find_cheapest(flights):
    print("list passed is: ")
    print(flights)
    result_price = None
    result = None
    for x in flights:
        print("x price is:")
        print(x['price']['total'])
        if(result_price == None or float(x['price']['total']) < float(result_price)):
            result = x
            result_price = float(x['price']['total'])
    print("cheapest result is")
    print(result)
    return result


def print_final_list(final_list):
    print(final_list[0]['origin'])
    for i in range(1, len(final_list)):
        print(' -> ' + final_list[i]['origin'])


if(len(sys.argv) < 2 or len(sys.argv) > 9):
    print("Script takes in 1-6 airport codes (starting at 1) you want to visit in this format: ")
    print("python hackpacker <country_1> <country_2> <...> <start_date> (YYYY-MM-DD) <end_date>")

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
        print("searching for trip between %s and %s" %(i, j))
        print("current origin = " + origin)
        if(j in visited or j == origin):
            print("CONTINUING")
            continue
        start_date = datetime.strptime(travel_dates[-1], '%Y-%m-%d')
        end_date = start_date + timedelta(days=avg_time)
        start = start_date.strftime('%Y-%m-%d')
        end = end_date.strftime('%Y-%m-%d')
        q_s = query_string.substitute(access_token= access_data, origin= origin, destination= j, start = start, end = end)
        flight_data = json.loads(os.popen(q_s).read())
        try:
            best_flight = flight_data['data'][0]
            print("best flight:")
            print(best_flight)
            next_leg.append(best_flight)
        except:
            continue
    print("next leg options: ")
    print(next_leg)
    if(next_leg != []):
        trip = find_cheapest(next_leg)
        origin = trip['destination']
        visited.append(trip['origin'])
        result.append(trip)
        new_date = datetime.strptime(trip['departureDate'], '%Y-%m-%d') + timedelta(days=avg_time)
        new = new_date.strftime('%Y-%m-%d')
        travel_dates.append(new)

print("final list:")
print(result)
print_final_list(result)

        
        

