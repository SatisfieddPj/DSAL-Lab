import json

def find_stations(stations_dict, locations, station_order):
    needed = set(locations)
    selected_stations = []

    # Keep searching as long as there are cities we still need
    while needed:
        best_station = None
        # We store the cities covered by the best station found so far
        best_covered = set()

        # Iterate through names in the EXACT order they were input
        for name in station_order:
            # Get the set of cities for this station
            current_cities = set(stations_dict[name])
            
            # Find the intersection (cities this station has that we still NEED)
            covered = needed.intersection(current_cities)
            
            if len(covered) > len(best_covered):
                best_station = name
                best_covered = covered

        # If we went through all stations and couldn't cover anything new, stop.
        if best_station is None or len(best_covered) == 0:
            break

        # Subtract the cities we just covered from the 'needed' set
        needed -= best_covered
        # Add the station name to our results
        selected_stations.append(best_station)

    return selected_stations

def main():
    # Read the list of target locations
    line1 = input().strip()
    if not line1: 
        return
    locations = json.loads(line1)

    # Read the number of stations
    line2 = input().strip()
    if not line2: 
        return
    num_stations = int(line2)

    # Read each station and store it
    station_dict = {}
    station_order = [] 
    
    for _ in range(num_stations):
        line = input().strip()
        if not line:
            continue
        data = json.loads(line)
        name = data["Name"]
        cities = data["Cities"]
        
        station_dict[name] = cities
        station_order.append(name)

    # Calculate which stations to use
    result = find_stations(station_dict, locations, station_order)

    # Requirement: Output the list of names sorted alphabetically
    result.sort()
    print(result)

main()