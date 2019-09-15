# Hackpacker
HackMIT 2019


This project is designed to take in an origin, destination, number of stops, start date and end date (YYYY-MM-DD). The origin and destination come in as an airport code to ensure that they are unique and can be matched up on the Amadeus flight API. The program then finds the cheapest way to visit different countries from the origin to the destination over the duration of your entered start and end dates. We used a greedy algorithm for the first iteration to make sure things were working, but would later update it to include more backtracking and dynamic price checking. Checks were implemented to ensure the trip ended in a proper location, keeping the user from flying to a destination that has no outbound flights on this API.

This app would be useful to automate the searching for cheap trips between two destinations over a given time frame.



2 example command line calls:

python3 graphCreator.py BOS LAX 3 2019-09-21 2019-09-30

python hackpacker.py BOS LAX LON 2019-10-10 2019-10-19
