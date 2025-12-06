def observed_items():
    # Read five observations from the user and store them in a list.
    observations = []
    for count in range(5):
        print("Please enter an observation:")
        observation = input()
        observations.append(observation)
    return observations

def remove_observations(observations):
    # Allow the user to remove observations from the list.
    is_running = True

    while is_running:
        print("Do you wish to remove an observation (yes/no)?")
        response = input().strip().lower()

        if response == "yes":
            print("What observation do you wish to remove?")
            observation = input()

            if observation in observations:
                observations.remove(observation)
                print("Done!")
            else:
                print("That observation is not in the list.")
        else:
            is_running = False

def run_task3():
    # Observe, optionally remove, then display sorted observation counts.
    observations = observed_items()
    remove_observations(observations)

    # Build a set of (observation, count) tuples
    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    # Display sorted results
    print("\nObservations:")
    for item, count in sorted(observations_set):
        print(f"{item} observed {count} times")

if __name__ == "__main__":
    run_task3()