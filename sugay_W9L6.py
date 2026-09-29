sugayflavor = input("Enter Pizza Flavor (Hawaiian/BBQ/Cheese/Oreo): ").lower()

match sugayflavor:

    case "hawaiian":
        print("You Selected Hawaiian Pizza. ")
        sugaysize = input("Enter Size (Small/Medium/Large): ").lower()

        if sugaysize == 'small':
           price = 100
           print("Price:", price)

        elif sugaysize == 'medium':
            price = 200
            print("Price", price)

        elif sugaysize == 'large':
            price = 300
            print("Price", price)

        else:
            price = 0
            print("Invalid size")


    case "bbq":
         print("You Selected BBQ Pizza. ")
         sugaysize = input("Enter Size (Small/Medium/Large): ").lower()

         if sugaysize == 'small':
             price = 100
             print("Price:", price)

         elif sugaysize == 'medium':
             price = 200
             print("Price", price)

         elif sugaysize == 'large':
             price = 300
             print("Price", price)

         else:
             price = 0
             print("Invalid size")


    case "cheese":
        print("You Selected Cheese Pizza. ")
        sugaysize = input("Enter Size (Small/Medium/Large): ").lower()

        if sugaysize == 'small':
           price = 100
           print("Price:", price)

        elif sugaysize == 'medium':
            price = 200
            print("Price", price)

        elif sugaysize == 'large':
            price = 300
            print("Price", price)

        else:
            price = 0
            print("Invalid size")





    case "oreo":
        print("Not Available. ")
        sugaysize = input("Enter Size (Small/Medium/Large): ").lower()

        if sugaysize == 'small':
           price = 100
           print("Price:", price)

        elif sugaysize == 'medium':
            price = 200
            print("Price", price)

        elif sugaysize == 'large':
            price = 300
            print("Price", price)

        else:
            price = 0
            print("Invalid size")

