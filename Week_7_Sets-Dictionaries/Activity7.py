import json

def read(file_path):
    #Read JSON data from the given file path and display the location,population and each bot's statistics.
    with open(file_path) as file:
        data = json.load(file)

    place_name = data["location"]
    print(f"Place Name: {place_name}")

    population_size = data["population"]
    print(f"Population Size: {population_size}")

    for bot in data["bots"]:
        name = bot["name"]
        stats = bot["stats"]
        print(f"{name} has the following stats: {stats}")

def run():
    # Wrapper function to read and display futurama.json.
    read("futurama.json")

if __name__ == "__main__":
    run()