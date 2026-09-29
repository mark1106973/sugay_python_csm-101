from tkinter.font import names

students = {
    "Ana":[97, 95, 95],
    "Kirk":[70, 69, 71],
    "Liza":[69, 71, 66]
}
sugayhighest = 0
sugaynamehighest = ""
sugaylowest = 0
sugaynamelowest = ""
sugaytally = 0

for name, grade in students.items():
    sugayaverage = sum(grade) / len(grade)
    print(name,*grade, "Average: ", sugayaverage)
    if sugayaverage > sugayhighest:
        sugayhighest = sugayaverage
        sugaynamehighest = name

    else:
        sugayaverage > sugaylowest
        sugaylowest = sugayaverage
        sugaynamelowest = name

for g in grade:
    if g < 75:
        sugaytally = sugaytally + 1


print(f"Student {sugaynamehighest} got the highest average: {sugayhighest}")
print(f"Student {sugaynamelowest} got the lowest average: {sugaylowest}")
print(f"There are {sugaytally} grades which are below 75. ")
