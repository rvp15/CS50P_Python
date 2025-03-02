#####################

distances ={
    "voyager 1": "162",
    "voyager 2": "132",
    "Pioneer 10": "145",
    "New Horizon":"986",
    "Victor":"503"
}
def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from earth")

    for distance in distances.values():
        print(f" {distance} AU is {int(distance)*7} in meters")


main()