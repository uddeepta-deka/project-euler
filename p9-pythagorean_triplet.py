__author__ = "Uddeepta Deka"

def findtriplet(N):
    """
    Returns Pythagorean triplet (a, b, c)
    with a + b + c = N
    """
    for a in range(1, N // 3 + 1):
        b = (N * N - 2 * N * a) / (2 * (N - a))
        c = N - a - b
        if b.is_integer() and c.is_integer():
            a, b, c = int(a), int(b), int(c)
            return (a, b, c)
    return None

if __name__=="__main__":
    perim = 1000
    triplet = findtriplet(perim)
    if triplet:
        triplet_prod = triplet[0] * triplet[1] * triplet[2]
        print(f"Pythagorean triplet with perimeter {perim} is: {triplet}. Their product is {triplet_prod}. ")
    else:
        print("No triplet found.")
