tal = int(input("mata in ett tal: "))
if tal >= 0 and tal <9:
    print ("0-9 är är ensiffriga tal")
if tal >= 10 and tal <99:
     print  ("10-99 är tvåsiffriga tal")
if tal >= 100 and tal <999:
    print ("100-999 är tresiffriga tal")
if tal >1000:
    print ("1000+ är minst fyrsiffriga tal")
if tal <0:
    print ("tal mindre än 0 är negativa")