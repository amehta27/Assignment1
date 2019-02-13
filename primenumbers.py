def primenumber():
  number = input("please enter the number:")
  number = int(number)

  message = ""

  if number == 1 or number == 2:
      message = "number is prime number"

  for index in range(number-1,1,-1):
      if(number % index == 0):
          message = "number is not prime number"
          break
      else:
          message = "number is prime number"

  return message

print(primenumber())
