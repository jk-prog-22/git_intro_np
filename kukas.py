svars       = 70
kukas       = 4
svarsApedot = 0.758

for kuka in range(kukas):
    ieprSvars = svars
    svars = svars + svarsApedot
    print("Apēdu ", (kuka + 1), "kūku, bija", round(ieprSvars, 1), "kg, nu jau ", round(svars, 1), "kg")
    print(type(kuka), type(ieprSvars), type(svars))