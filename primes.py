"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def calculate(num):
    x = 2
    divisible = False
    
    #if the number is 2, it is automatically a prime
    if num == 2:
        divisible = False
    #Check if it is prime:
    else:
        for i in range(2,num):
            #Means it is not prime
            if (num % i) == 0:
                divisible = True
    
    return divisible


def primes(number_of_primes):
    list = []
    #number is the variable that stores what can be added to the list
    number = 1
    #For loop makes sure there is enough numbers added to the list
    for i in range(0,number_of_primes):
        added = False
        while added == False:
            if calculate(number) == False:
                list.append(number)
                added = True
            #Increment the number variable
            number = number + 1

    return list

#Create a function for calculating prime numbers
#Use function
    
print(primes(10))
