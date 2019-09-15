from graphDS import Edge, Node
import json
from datetime import timedelta, datetime, date
import sys

# converts the json file into a useable dictionary (including only startDate and endDate)
# startDate and endDate are both datetime objects of format YYYY-MM-DD
def jsonToDic(jsonGraph, startDate, endDate):
    finalDic = {}

    for flight in jsonGraph:
        d = datetime.strptime(flight['departureDate'], '%Y-%m-%d')
        if d >= startDate and d <= endDate:
            if flight['origin'] not in finalDic.keys():
                finalDic[flight['origin']] = {flight['destination']: [(d, flight['price']['total'])]}
            else:
                if flight['destination'] not in finalDic[flight['origin']].keys():
                    finalDic[flight['origin']][flight['destination']] = [(d, flight['price']['total'])]
                else:
                    finalDic[flight['origin']][flight['destination']].append((d, flight['price']['total']))
    return finalDic

# creates the graph that we want to traverse through
def initializeGraph(graphDictionary):
    edgeLists = []
    for key, value in graphDictionary.items():
        for destination, prices in value.items():
            for day, price in prices:
                edgeLists.append(Edge(price, Node(key), Node(destination), day))
    return edgeLists

# traverses the graph that we created, using an approximate algorithm (greedy)
def traverseGraph(edgeLists, start, end, maxNights, startDate, endDate):
    # startDate = datetime.strptime(startDate, '%Y-%m-%d')
    # endDate = datetime.strptime(endDate, '%Y-%m-%d')
    current = [start]
    currentPrice = 0
    currentDate = startDate
    visited = set(current)
    for i in range((endDate - startDate).days-1):
        nextPlace, price, nights = findNextPlace(edgeLists, current[-1], end, visited, maxNights, currentDate, startDate, endDate)
        
        current.append(nextPlace)
        visited.add(nextPlace)
        currentDate = nights
        currentPrice += price
        print(nextPlace, currentDate)

        if currentDate >= endDate and nextPlace == end:
            break
    print(current, price)

# finds the next destination given our current location and where we want to go
def findNextPlace(edgeLists, start, end, visited, maxNights, currentDate, startDate, endDate):
    if (endDate - currentDate).days > maxNights:
        nextPlace = sorted([x for x in edgeLists if (x.getDay() >= startDate and x.getDay() <= startDate + timedelta(days=maxNights) and x.getStart().toString() == start and x.getEnd().toString() != end) and x.getEnd().toString() not in visited], key = lambda x: float(x.getPrice()))[0]
    else:
        nextPlace = sorted([x for x in edgeLists if (x.getDay() == endDate and x.getStart().toString() == start and x.getEnd().toString() == end)], key = lambda x: float(x.getPrice()))[0]

    return (nextPlace.getEnd().toString(), float(nextPlace.getPrice()), nextPlace.getDay())


# arguments should be "graphCreator.py startLoc endLoc numPlacesToVisit startDate endDate"
arguments = sys.argv

startDate = datetime.strptime(arguments[4], '%Y-%m-%d')
endDate = datetime.strptime(arguments[5], '%Y-%m-%d')
daysPer = (endDate - startDate).days // int(arguments[3])
# graphDictionary = jsonToDic(graphDictionary, '2019-09-20', '2019-09-30')

graphDictionary = {}
with open('test.json', 'r') as fil:
    for line in fil:
        graphDictionary = json.load(fil)['data']
        graphDictionary.update(jsonToDic(graphDictionary, startDate, endDate))

edgeLists = initializeGraph(graphDictionary)



# traverseGraph(edgeLists, 'MAD', 'LON', 10, '2019-09-20', '2019-09-30')
traverseGraph(edgeLists, arguments[1], arguments[2], daysPer, startDate, endDate)

