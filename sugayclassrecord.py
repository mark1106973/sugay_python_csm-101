sugayclassrecord = {"Mark": {"StudID": "1147576",
"Grade":[90,85,85,82,83,90,92]
},
"Chester": {"StudID": "6757411",
"Grade": [72,75,70,80,84,75,85]
},
"Sugay": {"StudID": "67217311",
"Grade": [77,62,60,59,60,59,67]
},
"Laput": {"StudID": "67214211",
"Grade": [97,96,98,100,99,95,90]

},
}

sugaystudent = input("Enter Student name: ").strip().lower()

student_names = {
    name.lower(): name
    for name in sugayclassrecord
}
if sugaystudent in student_names:
    actual_name = student_names[sugaystudent]

    print("\nStudent found!")

    sugaygrades = sugayclassrecord[actual_name]["Grade"]
    print("=========================")
    print("Grades: ", sugaygrades)


    average = sum(sugaygrades) /len(sugaygrades)
    print("=========================")
    print("Average: ", round(average, 2))


    if any(grade < 60 for grade in sugaygrades):
        print("=========================")
        print("Candidate for intervention")

    else:
        print("=========================")
        print("No intervention needed")
        print("=========================")


    print("Highest Grade: ", max(sugaygrades))
    print("=========================")
    print("Lowest Grade: ", min(sugaygrades))
    print("=========================")

else:
    print("\nSTUDENT NOT FOUND!")