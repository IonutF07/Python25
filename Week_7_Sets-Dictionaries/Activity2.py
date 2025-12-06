#Set from other data structures

def observed_items():
    #Read observations from user and store them into a list:
    observations = []
    for n in range (7):
        print("Please enter an observation:")
        ob = input()
        observations.append(ob)
    return observations

def run_task2():
    #Count how many times each observation occurs is using a set of (item, count) tuples.
    print("Counting observations...")
    observations = observed_items()

    #Use a set to store (observation, count) pair
    observations_set = set()

    for ob in observations:
        data = (ob,observations.count(ob))
        observations_set.add(data)

    #Display the counts
    for item,count in observations_set:
        print(f"{item} observed {count} times.")

if __name__ == '__main__':
    run_task2()