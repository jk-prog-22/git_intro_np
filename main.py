# Konstantes
vards       = "Nils"
dzejolis    = [
    "Ai jel, manu vieglu prātu,",
    "Jauns apņēmu līgaviņ`.",
    "Ne gadiņa nedzīvoju,",
    "Sola kungi karā ņemt."
]

# Printējam vārdu
print(vards)

# Ejam cauri dzejoļa masīvam
cikls = 0
for rindina in dzejolis:
    if (cikls % 2 != 0):
        atstarpe = "  "
    else:
        atstarpe = ""

    print(atstarpe + rindina)
    cikls += 1

# Izprintējam dzejoli
print(*dzejolis, sep = "\n")

# Ak, eglīte
zvaigznes = 6
for zvaigzne in range(zvaigznes):
    print(" " * (zvaigznes - (zvaigzne + 1)),'*' * (2 * zvaigzne + 1))

# Trijstūri
augstums = 3
for linija in range(augstums):
    print(" " * (augstums - (linija + 1)),'*' * (2 * linija + 1), sep = "\t\t")
    print(" " * (augstums - (linija + 1)),'*' * (2 * linija + 1))