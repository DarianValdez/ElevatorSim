import json

inputFile = "input.json"
outputFile = "output.json"
timePerFloor = 10


def processTrip(currentFloor, floorsToVisit):
    totalTravelTime = 0
    orderOfFloorsVisited = []

    sortedFloors = sorted(floorsToVisit)
    orderOfFloorsVisited.append(currentFloor)

    while sortedFloors:
        closestFloor = min(sortedFloors, key=lambda x: abs(x - currentFloor))
        travelTime = abs(closestFloor - currentFloor) * timePerFloor
        totalTravelTime += travelTime
        currentFloor = closestFloor
        orderOfFloorsVisited.append(currentFloor)
        sortedFloors.remove(currentFloor)

    return totalTravelTime, orderOfFloorsVisited


def simulateElevator(inputFile, outputFile):
    with open(inputFile, 'r') as infile:
        data = json.load(infile)

    trips = []

    for trip in data["trips"]:
        currentFloor = trip["currentFloor"]
        floorsToVisit = trip["floorsToVisit"]

        totalTravelTime, visitedFloors = processTrip(
            currentFloor, floorsToVisit)

        tripResult = {
            "startingFloor": currentFloor,
            "floorsToVisit": floorsToVisit,
            "totalTravelTime": totalTravelTime,
            "visitedFloors": visitedFloors,
        }

        trips.append(tripResult)
        print(
            f"Starting floor and floors to visit: {currentFloor}, {floorsToVisit}")
        print(f"Total travel: {totalTravelTime}")
        print(f"Order visited floors: {visitedFloors}")
        print("")

    outputData = {"trips": trips}

    with open(outputFile, 'w') as outfile:
        json.dump(outputData, outfile, indent=4)


simulateElevator(inputFile, outputFile)
