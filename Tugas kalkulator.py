def addition(x, y): #pertambahan
  return x + y 
def substraction(x, y): #perkurangan
  return x - y
def multiplication(x, y): #perkalian
  return x * y
def division(x, y): #pembagian
  if y==0:
    return "Error: Cannot Divide by 0"
  return x/y

print("CALCULATOR \n-------------------------" )
while True: #pilihan kalo mau tambahin, tambahin aj
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. End")
    option = input("Choose operation (1-5): ")

    if option == "5":
        print("Calculator closed.")
        break

    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))

    if option == "1":
        result = addition(num_1, num_2)
        print(result, "\n-------------------------")
    elif option == "2":
        result = substraction(num_1, num_2)
        print(result, "\n-------------------------")
    elif option == "3":
        result = multiplication(num_1, num_2)
        print(result, "\n-------------------------")
    elif option == "4":
        result = division(num_1, num_2)
        print(result, "\n-------------------------")
    else:
        print("Invalid input. Please try again. \n-------------------------")

#\n ------------------------- biar lebih rapih


    