def istriplet(a,b,c):
    """
    Returns True if (a,b,c) is a 
    Pythogorean triplet
    """
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
        
def findtriplet(N):
    """
    Prints Pythagorean triplet (a,b,c)
    with a+b+c = N
    """
    for a in range(3, int((N-3)/3)):
        for b in range(a+1,int((N-1-a)/2)):
            c = N-a-b
            if istriplet(a, b, c):
                print(a,b,c)
findtriplet(1000)
