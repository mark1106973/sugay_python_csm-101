sugaypatients =  {
    "Mark":[130,190,200,500,450,320],
    "Liza":[80,180,100,250,50,200,400]
}

for sugayname, sugayvalues in sugaypatients.items():
    print("Patient:", sugayname)
    print("Blood sugar summary -")

    for sugayvalue in sugayvalues:
        if sugayvalue >= 126:
            print(sugayvalue, "high")
        else:
            print(sugayvalue, "normal")

sugaymx = max(sugayvalues)
sugaymn = min(sugayvalues)
sugayaver = sum(sugayvalues)/len(sugayvalues)
sugaydiff = sugaymx - sugaymn

print("Max Blood Sugar: ", sugaymx)
print("Min Blood Sugar: ", sugaymn)
print("Average Blood Sugar: ", sugayaver)
print("difference: ", sugaydiff)
