# data structure for the graphs to traverse
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