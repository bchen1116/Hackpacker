# data structure for the graphs to traverse
# class Node:
#     def __init__(self, location, currentInfo = None):
#         self.location = location
#         self.currentInfo = currentInfo
    
#     def verifyNightsLeft(self):
#         if self.currentInfo[1] >= 1:
#             return True
#         return False

#     # adds flights to our data
#     def addCurrentInfoFlight(self, numSpotsVisited, price, flightListDic):
#         self.currentInfo[numSpotsVisited] = [price, flightListDic]

#     # replace the current flightList of dictionaries with the new list if the price is lower
#     def update_currentInfo_flight(self, numSpotsVisitedFromHere, price, flightList):
#         if self.currentInfo[numSpotsVisitedFromHere][0] > price:
#             self.currentInfo[numSpotsVisitedFromHere][1] = flightList
#             self.currentInfo[numSpotsVisitedFromHere][0] = price

#     def get_cheapest_flight_info(self, numSpotsSisited):
#         return self.currentInfo[numSpotsVisited]

#     def getAllCheapestFlights(self):
#         return self.currentInfo

#     def getLocation(self):
#         return location

# class Edge:
#     def __init__(self, startNode, endNode, price, daysSpent, departureDate, arrivalDate, spotsRemaining):
#         self.startNode = startNode
#         self.endNode = endNode
#         self.price = price
#         self.daysSpent = daysSpent
#         self.departureDate = departureDate
#         self.arrivalDate = arrivalDate
#         self.spotsRemaining = spotsRemaining
    
#     def setStartNode(self, startNode):
#         self.startNode = startNode

#     def setEndNode(self, endNode):
#         self.endNode = endNode
    
#     def setPrice(self, price):
#         self.price = price

#     def setdaysSpent(self, daysSpent):
#         self.daysSpent = daysSpent

#     def setDepartureDate(self, departureDate):
#         self.departureDate = departureDate

#     def setArrivalDate(self, arrivalDate):
#         self.arrivalDate = arrivalDate

#     def setSpotsRemaining(self, spotsRemaining):
#         self.spotsRemaining = spotsRemaining

#     def getStartNode(self):
#         return self.startNode

#     def getEndNode(self):
#         return self.endNode
    
#     def getPrice(self):
#         return self.price
    
#     def getdaysSpent(self):
#         return self.daysSpent

#     def getDepartureDate(self):
#         return self.departureDate

#     def getArrivalDate(self):
#         return self.arrivalDate

#     def getSpotsRemaining(self):
#         return self.spotsRemaining

#     def getFlightInfoDic(self):
#         flightInfo = {}
#         flightInfo['origin'] = self.startNode.getLocation()
#         flightInfo['destination'] = self.endNode.getLocation()
#         flightInfo['price'] = self.price
#         flightInfo['numNights'] = self.daysSpent
#         flightInfo['arrivalDate'] = self.arrivalDate
#         flightInfo['departureDate'] = self.departureDate
#         return flightInfo
        


class Node:
    def __init__(self, location):
        self.location = location

    def toString(self):
        return str(self.location)


class Edge:
    def __init__(self, price, start, end, day):
        self.price = price
        self.start = start
        self.end = end
        self.day = day

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getDay(self):
        return self.day

    def toString(self):
        return self.start.toString() + ", " + self.end.toString() + ", " + str(self.price) + ", " + str(self.day)