#Nested function
def summ(a,b):
    #inner function
    def find_total (x, y):
        return x + y
    #inner function calculate average
    def find_average (t):
        return t / 2
    #calling the inner function
    total = find_total(a, b)
    average = find_average(total)
    return total, average
#the main program
print ("Value of A")
val1=float(input())
print("Value of B")
val2=float(input())
#call the function
total, average = summ(val1,val2)
#Display the results
print("Sum=", total)
print("Average=", average)
