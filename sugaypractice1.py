sugaystudents = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 79,
    "Diana": 95,

}
print("Student Grades")
print("-----------------")
print("Ana", sugaystudents["Ana"])
print("Ben", sugaystudents["Ben"])

sugaystudents["Ella"] = 88
sugaystudents["Carlo"] = 82
sugaystudents["Diana"] = 91

sugayname1 = input("Enter Student Name: ")
sugaygrade1 = int(input("Enter Grade: "))
sugaystudents[sugayname1] = sugaygrade1
print(sugaystudents)
print("\nUpdated Student Grades")
print("-------------------")

for name, grade in sugaystudents.items():
    print(name, ":", grade)

sugaysearch = input("\nEnter Student Name to search: ")
if sugaysearch in sugaystudents:
    print(sugaysearch, "has a grade of", sugaystudents[search])
else:
    print("Student not found. ")
