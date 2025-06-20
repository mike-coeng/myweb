def Euclid_Algo(a,b):
    # Define the 2 jugs
    if not a<=b:
            raise "invalid arguments due to a>b"
    # Define the algorithm
    while True:
        (a,b) = (b%a,a)
        if a == 0:
            break
    return b
print(Euclid_Algo(210,2560))

