sugayflavor = input ("Enter pizza flavor (Hawaiian/BBQ/Cheese/Oreo): ").lower()

sugaysize = input('Enter size (Small/Medium/Large): ').lower()

if sugayflavor == "hawaiian":
    print("You selected Hawaiian Pizza. ")
    if sugaysize == 'small':
        price = 500
        print("Price:", price)
    elif sugaysize == 'medium':
        price = 700
        print("Price:", price)
    elif sugaysize == 'large':
        price = 900
        print("Price:", price)
    else:
        price = 0
        print("Invalid size. ")

elif sugayflavor == "bbq":
    print("You selected BBQ. ")
    if sugaysize == 'small':
        price = 500
        print("Price:", price)
    elif sugaysize == 'medium':
        price = 700
        print("Price:", price)
    elif sugaysize == 'large':
        price = 900
        print("Price:", price)
    else:
        price = 0
        print("Invalid size. ")

elif sugayflavor == "cheese":
    print("You selected Cheese. ")
    if sugaysize == 'small':
        price = 500
        print("Price:", price)
    elif sugaysize == 'medium':
        price = 700
        print("Price:", price)
    elif sugaysize == 'large':
        price = 900
        print("Price:", price)
    else:
        price = 0
        print("Invalid size. ")

elif sugayflavor == "oreo":
    print ('Not Available. ')
    if sugaysize == 'small':
        price = 500
        print("Price:", price)
    elif sugaysize == 'medium':
        price = 700
        print("Price:", price)
    elif sugaysize == 'large':
        price = 900
        print("Price:", price)
    else:
        price = 0
        print("Invalid size. ")








