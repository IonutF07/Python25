def summ(a,b):
    total = a+b
    average = total/2
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