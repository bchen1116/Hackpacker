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
        if(result_price == None or x['price'] < result_price):
            result = x
            result_price = x['price']
    return result


if(len(sys.argv) < 2 or len(sys.argv > 9)):
    print("Script takes in 1-6 airport codes (starting at 1) you want to visit in this format: ")
    print("python hackpacker <country_1> <country_2> <...> <start_date> (YYYY-MM-DD) <end_date>")

country_list = sys.argv[1:(len(sys.argv)-2)]
dates = sys.argv[len(sys.argv)-2:]

travel_dates = [dates[0]]
visited = []


avg_time = (datetime.strptime(dates[1], '%Y-%m-%d') - datetime.strptime(dates[0], '%Y-%m-%d')).days / (len(sys.argv) - 3)
next_leg = []

# query_string = Template("curl -X GET -H 'Authorization: Bearer f6qJzeKNKaSz3GrfHebt1MHMLwGA' \"https://test.api.amadeus.com/v1/shopping/flight-dates?origin=$origin&destination=$destination&oneWay=true&departureDate=$start,$end\"")


query_string = Template("curl -X GET -H 'Authorization: Bearer jRAhGHf7Ck6w4I4zDJweRPWT3uyM' \"https://test.api.amadeus.com/v1/shopping/flight-dates?origin=$origin&destination=$destination&oneWay=true&departureDate=$start,$end\"")


print(country_list)
print(visited)

for i in country_list:
    print("i is: " + i)
    if(i in visited):
        continue
    next_leg = []
    for j in country_list:
        print("j is: " + j)
        if(j in visited or i == j):
            continue
        start_date = datetime.strptime(travel_dates[-1], '%Y-%m-%d')
        end_date = start_date + timedelta(days=avg_time)
        start = start_date.strftime('%Y-%m-%d')
        end = end_date.strftime('%Y-%m-%d')
        q_s = query_string.substitute(origin= i, destination= j, start = start, end = end)
        print(q_s)
        flight_data = json.loads(os.popen(q_s).read())
        print(flight_data['data'][0])
        try:
            best_flight = flight_data['data'][0]
            next_leg.append(best_flight)

            print(visited)
            print(next_leg)
        except:
            continue
    trip = find_cheapest(next_leg)
    visited.append(trip['origin'])
        
        

