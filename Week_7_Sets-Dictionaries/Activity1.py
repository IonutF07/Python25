def observed():
    #Create a set of observed items (Duplicate values are automatically removed)
    observations = {"Car","Sky Scraper","Sky Scraper","Bike","House","House"}
    return observations

def run_task1():
    #Call observed() and display the resulting set.
    os = observed()
    print(os)

if __name__ == '__main__':
    run_task1()