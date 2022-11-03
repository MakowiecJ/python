while(True):
    try:
        n = input('Podaj x: ')
        npow = pow(float(n),3)
        print("x = {}\nx^3 = {}".format(n, npow))
    except ValueError:
        if n != 'stop': 
            print("Error, wprowadzono napis")
        else: break
