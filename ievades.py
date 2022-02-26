def izvelne():
    print("Ievadi 1: Pievienot produktu.")
    print("Ievadi 2: Iziet.")
    return input("Darbība: ")

izvele = izvelne()

while True:
    if izvele == '1':
        produkts = input('Produkta nosaukums: ')
        daudzums = int(input('Pieejamais daudzums: '))
        izvele = izvelne()

    elif izvele == '2':
        break
