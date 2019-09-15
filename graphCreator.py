from graphDS import Edge, Node
import json
from datetime import timedelta, datetime, date
import sys

currentSites = ['ABQ', 'ABZ', 'ACA', 'ACC', 'ADD', 'ADL', 'AGP', 'AKL', 'ALB', 'ALC', 'ALG', 'AMD', 'AMM', 'AMS', 'ANC', 'ATH', 'ATL', 'AUA', 'AUH', 'AUS', 'AYT', 'BAQ', 'BBI', 'BCD', 'BCN', 'BDA', 'BEG', 'BER', 'BEY', 'BFS', 'BGI', 'BHM', 'BHX', 'BHZ', 'BIO', 'BJS', 'BJX', 'BKI', 'BKK', 'BLI', 'BLL', 'BLQ', 'BLR', 'BME', 'BNA', 'BNE', 'BOD', 'BOG', 'BOI', 'BOM', 'BOS', 'BRE', 'BRI', 'BRS', 'BRU', 'BSB', 'BTV', 'BUD', 'BUE', 'BUF', 'BUH', 'BWN', 'BZE', 'BZN', 'CAE', 'CAI', 'CAK', 'CAN', 'CCJ', 'CCS', 'CCU', 'CEB', 'CGN', 'CGQ', 'CHC', 'CHI', 'CHS', 'CJB', 'CKG', 'CLJ', 'CLO', 'CLT', 'CMB', 'CMH', 'CNS', 'CNX', 'COK', 'COS', 'CPH', 'CPT', 'CTA', 'CTG', 'CUL', 'CUN', 'CUR', 'CUZ', 'CVG', 'DAC', 'DAR', 'DAY', 'DBV', 'DEL', 'DEN', 'DFW', 'DLA', 'DLC', 'DPS', 'DSM', 'DTT', 'DUB', 'DUS', 'DXB', 'EAP', 'EAS', 'EBB', 'EDI', 'ELP', 'EUG', 'EVN', 'EYW', 'FAO', 'FAT', 'FLL', 'FLR', 'FNT', 'FPO', 'FRA', 'FSD', 'GCM', 'GDL', 'GDN', 'GEG', 'GES', 'GLA', 'GND', 'GOA', 'GOI', 'GOT', 'GRR', 'GSO', 'GSP', 'GUA', 'GVA', 'HAJ', 'HAM', 'HAN', 'HEL', 'HFD', 'HGH', 'HKD', 'HKG', 'HKT', 'HNL', 'HOU', 'HPN', 'HYD', 'IBZ', 'IND', 'IPC', 'ISP', 'IST', 'IXE', 'JAC', 'JAX', 'JED', 'JNB', 'JOG', 'JTR', 'KBV', 'KIV', 'KMG', 'KOA', 'KRK', 'KRR', 'KRT', 'KTM', 'KTW', 'KUL', 'KWI', 'LAS', 'LAX']
origins = set()
departures = set()
# converts the json file into a useable dictionary (including only startDate and endDate)
# startDate and endDate are both datetime objects of format YYYY-MM-DD
def jsonToDic(jsonGraph, startDate, endDate):
    finalDic = {}

    for flight in jsonGraph:
        d = datetime.strptime(flight['departureDate'], '%Y-%m-%d')
        if d >= startDate and d <= endDate:

            origins.add(flight['origin'])
            departures.add(flight['destination'])

            if flight['origin'] not in finalDic.keys():
                finalDic[flight['origin']] = {flight['destination']: [(d, flight['price']['total'])]}

            else:
                if flight['destination'] not in finalDic[flight['origin']].keys():
                    finalDic[flight['origin']][flight['destination']] = [(d, flight['price']['total'])]

                else:
                    finalDic[flight['origin']][flight['destination']].append((d, flight['price']['total']))
    return dict(finalDic)

# creates the graph that we want to traverse through
def initializeGraph(graphDictionary, inclusionSet):
    edgeLists = []
    for key, value in graphDictionary.items():
        if key in inclusionSet:
            for destination, prices in value.items():
                if destination in inclusionSet:
                    for day, price in prices:
                        edgeLists.append(Edge(price, Node(key), Node(destination), day))

    for edge in edgeLists:
        print(edge.toString())

    return edgeLists

# traverses the graph that we created, using an approximate algorithm (greedy)
def traverseGraph(edgeLists, start, end, maxNights, startDate, endDate, inclusionSet):
    # startDate = datetime.strptime(startDate, '%Y-%m-%d')
    # endDate = datetime.strptime(endDate, '%Y-%m-%d')
    current = [start]
    currentPrice = 0
    currentDate = startDate
    visited = set(current)
    for i in range((endDate - startDate).days-1):
        nextPlace, price, nights = findNextPlace(edgeLists, current[-1], end, visited, maxNights, currentDate, startDate, endDate, inclusionSet)
        print(nextPlace, price, nights)
        current.append(nextPlace)
        visited.add(nextPlace)
        currentDate = nights
        currentPrice += price
        print(nextPlace, currentDate)

        if currentDate >= endDate and nextPlace == end:
            break
    print(current, price)

# finds the next destination given our current location and where we want to go
def findNextPlace(edgeLists, start, end, visited, maxNights, currentDate, startDate, endDate, inclusionSet):
    if (endDate - currentDate).days >= maxNights:
        nextPlace = sorted([x for x in edgeLists if (x.getDay() >= startDate and x.getDay() <= startDate + timedelta(days=maxNights) and x.getStart().toString() == start and x.getEnd().toString() != end and (x.getEnd().toString() not in visited) and (x.getEnd().toString() in inclusionSet))], key = lambda x: float(x.getPrice()))[0]
    else:
        nextPlace = sorted([x for x in edgeLists if (x.getDay() == endDate and x.getStart().toString() == start and x.getEnd().toString() == end)], key = lambda x: float(x.getPrice()))[0]

    return (nextPlace.getEnd().toString(), float(nextPlace.getPrice()), nextPlace.getDay())

def updateDictionary(originalDic, newDic):
    for key, value in newDic.items():
        if key in originalDic.keys():
            originalDic[key].update(value)
        else:
            originalDic[key] = value
    return originalDic

# arguments should be "graphCreator.py startLoc endLoc numPlacesToVisit startDate endDate"
arguments = sys.argv

startDate = datetime.strptime(arguments[4], '%Y-%m-%d')
endDate = datetime.strptime(arguments[5], '%Y-%m-%d')
daysPer = (endDate - startDate).days // int(arguments[3])
# graphDictionary = jsonToDic(graphDictionary, '2019-09-20', '2019-09-30')

graphDictionary = dict()

with open('flight_data.json', 'r') as fil:
    for line in fil:
        # print(line)
        graphLine = json.loads(line)['data']
        graphDictionary = updateDictionary(graphDictionary, jsonToDic(graphLine, startDate, endDate))

print(graphDictionary)
inclusionSet = origins.intersection(departures)
print(inclusionSet)
edgeLists = initializeGraph(graphDictionary, inclusionSet)



# traverseGraph(edgeLists, 'MAD', 'LON', 10, '2019-09-20', '2019-09-30')
traverseGraph(edgeLists, arguments[1], arguments[2], daysPer, startDate, endDate, inclusionSet)

