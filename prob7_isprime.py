import numpy as np
def isprime(x):
    """
    This function returns True if x is prime
    """
    check = True
    if x==1: 
    	check=False
    elif x<4:
    	check=True   
    elif x%2==0:
        check=False
    elif x<9:
    	check=True
    elif x%3==0:
    	check=False
    else:
    	ii = 5
    	while ii<=int(np.sqrt(x)):
        	if x%ii==0:
         	    	check=False
        	if x%(ii+2)==0:
        		check=False
        	ii+=6
    return check

def Nprime(amount):
    """
    Returns array with N primes
    """
    
    primes = []
    found = 0
    number = 2
    
    while found<amount:
    	for x in primes:
    		if number%x == 0:
    			break
    	else:
    		primes.append(number)
    		found += 1
    	number +=1
    return primes
    
print(Nprime(21)[-1])
