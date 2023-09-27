# ElevatorSim
A script to simulate an elevator.
- This script assumes that the travel time should be minimized, so the elevator always moves to the nearest floor
  
Takes an input .json file of the form:
```
{
  "trips": [
    {
      "currentFloor": 5,
      "floorsToVisit": [
        10,
        20,
        15,
        25,
        30
      ]
    },
    ...
  ]
}
```

And outputs a .json file of the form:
```
{
  trips": [
    {
        "startingFloor": 5,
        "floorsToVisit": [
            10,
            20,
            15,
            25,
            30
        ],
        "totalTravelTime": 250,
        "visitedFloors": [
            5,
            10,
            15,
            20,
            25,
            30
        ]
    },
  ...
}
```
