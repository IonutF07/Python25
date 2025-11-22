#Nested tuples
def steps():
    #Create a return a list of tuples
    #Each contains: step name (str), likelihood of falling (int)
    likelihoods = [("step 1", 50),("step 2",38),("step 3",27),("step 4",99),("step 5",4)]
    return likelihoods
def run_task3():
    #classify steps as good or bad depending on their likelihood
    tile_steps = steps()
    good_steps = []
    bad_steps = []
    #Loop through each (step_name, likelihood) touple
    for step_name, likelihood_value in tile_steps:
        if likelihood_value < 50:
            bad_steps.append((step_name,likelihood_value))
        else:
            good_steps.append((step_name,likelihood_value))
        #Display summary message
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")
if __name__ == "__main__":
    run_task3()
