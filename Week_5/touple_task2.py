def likelihood_min_max():
    #Tuple of likelihoods (immutable ordered collection same as task1)
    likelihoods = (50,38,27,99,4)
    return min(likelihoods), max(likelihoods)

def run_task2():
    #Unpack the return tuple into variables
    min_likelihood, max_likelihood = likelihood_min_max()
    #Display the results in the required format
    print(f"Min likelihood of falling is: {min_likelihood}%")
    print(f"Max likelihood of falling is: {max_likelihood}%")
    
#For activity 2 we call run task 2()
if __name__ == "__main__":
    run_task2()
