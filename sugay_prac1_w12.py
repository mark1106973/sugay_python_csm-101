sugaypatients = {"Ana": [80,100,150], "Ben":[150,90,300]}
print()
for key, value in sugaypatients.items():
    print(key,value)
    for item in value:
            if item > 120:
                print(item,"High blood sugar")






















##patients = {"Mark" :(96,120,105),
##"Ana":(70,180,100)}

##normal = 120
##for pname,sugar in patients.items():
## print(pname, '-')
##   print(pname, '-')
##   dlow=0
##  for dsugar in sugar:
##      dlow=dsugar
##        print(dlow,"diabetic")