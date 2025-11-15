#Simple touple- - find safest step
def likelihood(): #Define a function called likelihood.
    #create a touple of steps with their safety likelihood
    likelihoods = (50,38,27,99,4) #safety likelihoods for each step in percentage
#find minimum value using built in min() function
    lowest = min(likelihoods)
    return lowest #return the lowest likelihood value
def run_task1():
#Call the likelihood function and display reusult in user firendly message.
#Call the likelihood function and store the returned minimum value
    min_likelihood = likelihood()
#Display the message in the required format
    print(f"Minimum likelihood of safety is: {min_likelihood}%")
#Ensure task1 runs when this script is executed
if __name__ == "__main__":
    run_task1()
    