def tip_calculator() :
    total_amount = input("Enter the total amount:")
    tip_percerntage = input("Emter the parcerntage:")
    tip_amount = (int(total_amount) * int(tip_percerntage))/100
    print (tip_amount)

tip_calculator()
