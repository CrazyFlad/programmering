tal = int(input("mata in första talet: "))
tal2 = int(input("mata in andra talet: "))
tal3 = int(input("mata in tredje talet: "))
if tal > tal2 > tal3:
    print ("tal är det största")
if tal > tal3 > tal2:
    print ("tal är det största")
if tal2 > tal > tal3:
    print ("tal2 är det största")
if tal2 > tal3 > tal:
    print ("tal2 är det största")
if tal3 > tal2 > tal:
    print ("tal3 är det största")
if tal3 > tal > tal2:
    print ("tal3 är det största")
