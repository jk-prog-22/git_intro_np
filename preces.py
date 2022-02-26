preces = [
    "Dirižabļi",
    "Cepumi",
    "Konfektes",
    "Lakstīgalas",
    "Zemenes"
]

kvantumi = [
    3, 548, 12, 2, 0
]

iteracija = 0
for prece in preces:
    if (kvantumi[iteracija] == 0):
        print("Mums nav", prece.lower())
    else:
        print("Mums ir", kvantumi[iteracija], prece.lower())
    iteracija += 1