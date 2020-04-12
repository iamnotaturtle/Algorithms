# Set Covering
statesNeeded = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {
    'k1': set(['id', 'nv', 'ut']),
    'k2': set(['id', 'wa', 'mt']),
    'k3': set(['or', 'nv', 'ca']),
    'k4': set(['nv', 'ut']),
    'k5': set(['ca', 'az']),
}

finalStations = set()

while statesNeeded:
    bestStation = None
    statesCovered = set()
    for station, statesForStation in stations.items():
        covered = statesNeeded & statesForStation
        if len(covered) > len(statesCovered):
            bestStation = station
            statesCovered = covered

    # Add station and remove covered states
    finalStations.add(bestStation)
    statesNeeded -= statesCovered

print(finalStations)
