x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# Poprawne, chociaż średniki w liniach 3 i 5 oraz nawias przy if niepotrzebne

# for i in "axby": (if ord(i) < 100: print (i))
# Niepoprawne, instrukcja "if ord(i) < 100: print (i)" nie jest instrukcją prostą, należy użyć wcięcia 

for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Poprawne, instrukcja print() jest instrukjcą prostą