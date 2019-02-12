def even_odd():
   number = input("Input the number:")
   number = int(number)
   if (number % 2 == 0):
       return "number is even"
   else:
       return "number is odd"


print(even_odd())
