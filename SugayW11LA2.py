print("What pizza flavor do you want po?")

sugaypizza = [
    ("hawaiian", "Hawaiian Pizza"),
    ("bbq", "BBQ"),
    ("cheese", "Cheese"),
    ("oreo", "Oreo")
]

sugayprices = [
    ("small", 500),
    ("medium", 700),
    ("large", 900)
]

sugayflavor = input("Enter pizza flavor (Hawaiian/BBQ/Cheese/Oreo): ").lower()
sugaysize = input("Enter size (Small/Medium/Large): ").lower()

for flavor in sugaypizza:
    if sugayflavor == flavor[0]:

        if sugayflavor == "oreo":
            print("Not Available. ")
        else:
            print("You selected", flavor[1])

            for size in sugayprices:
                if sugaysize == size[0]:
                    print("Price", size[1])
                    break
            else:
                print("Invalid size. ")

        break
else:
    print("Invalid flavor. ")


