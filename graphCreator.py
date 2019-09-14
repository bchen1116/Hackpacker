from graphDS import Edge, Node


def initializeGraph(graphDictionary):
    edgeLists = []
    for key, value in graphDictionary.items():
        for destination, prices in value.items():
            for day, price in enumerate(prices, start=1):
                edgeLists.append(Edge(price, Node(key), Node(destination), day))

    return edgeLists


def traverseGraph(edgeLists, start, end, maxNights = 2, duration = 4):
    current = [start]
    currentPrice = 0
    currentNights = 0
    visited = set(current)
    for i in range(duration):
        nextPlace, nights = findNextPlace(edgeLists, i + currentNights, current[-1], end, visited, duration, maxNights, currentNights)
        current.append(nextPlace)
        visited.add(nextPlace)
        currentNights += nights
        print(nextPlace, currentNights)
        if currentNights >= duration and nextPlace == end:
            break
    print(current)


def findNextPlace(edgeLists, day, start, end, visited, duration, maxNights, currentNights):
    if duration - currentNights > 1:
        nextPlace = sorted([x for x in edgeLists if (x.getDay() in range(day, day + maxNights) and x.getStart().toString() == start and x.getEnd().toString() != end) and x.getEnd().toString() not in visited], key = lambda x: x.getPrice())[0]
    else:
        nextPlace = sorted([x for x in edgeLists if (x.getDay() in range(day, day + maxNights) and x.getStart().toString() == start and x.getEnd().toString() == end) and x.getEnd().toString() not in visited], key = lambda x: x.getPrice())[0]
    # for i in nextPlace:
    #     print(i.toString())
    # print("\n")
    # return (0,0)
    return (nextPlace.getEnd().toString(), nextPlace.getDay() - currentNights)




graphDictionary = {
    "b": {
        # "b": [0, 0, 0, 0],
        "c": [6, 9, 17, 17],
        "d": [22, 16, 8, 12],
        "a": [25, 13, 6, 10],
    },
    "c": {
        "b": [10, 7, 10, 21],
        # "c": [0, 0, 0, 0],
        "d": [9, 16, 24, 24],
        "a": [11, 11, 17, 9],
    },
    "d": {
        "b": [8, 23, 11, 23],
        "c": [8, 20, 16, 11],
        # "d": [0, 0, 0, 0],
        "a": [8, 21, 17, 19],
    },
    "a": {
        "b": [16, 14, 25, 17],
        "c": [22, 25, 10, 14],
        "d": [18, 17, 9, 24],
        # "a": [0, 0, 0, 0],
    },
}
edgeLists = initializeGraph(graphDictionary)
traverseGraph(edgeLists, 'b', 'd', 2, 4)
