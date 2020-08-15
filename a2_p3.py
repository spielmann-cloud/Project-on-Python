"""
@author: sarvar umurzakov
"""

""" Infinite Loop until user enter appropriate values for name and companyName. We also delete unnecessary spaces from
left and right side. """
while(True):
    name = input("Please enter your name: ")
    companyName = input("What is your company name? ")

    name = name.rstrip().lstrip()

    companyName = companyName.lstrip().rstrip()

    if(companyName == '' or name ==''):
        print("Invalid company name or name, please try it again\n")
        continue
    else:
        break

""" Next Line and appropriate output """
print()
print("Hi " + name + "! We can set setup your '" + companyName + "' sales menu.\n" +
      "Please enter 3 products and their prices that you would like to sell.")
print()

""" Using infinite Loop ask user to enter appropriate values of productName and productPrice """
while(True):
    print("Enter Product 1 and its price:")
    firstProductName = input("> ")
    firstProductName = firstProductName.rstrip().lstrip()
    if(firstProductName == ''):
        print("Invalid product name, try it again")
        print()
        continue
    try:
        firstProductPrice = float(input("> "))
        if(firstProductPrice <= 0):
            raise Exception
    except:
        print("Invalid number, please try it again")
        print()
    else:
        break

print()

while(True):
    print("Enter Product 2 and its price:")
    secondProductName = input("> ")
    secondProductName = secondProductName.rstrip().lstrip()

    if(secondProductName == ''):
        print("Invalid product name, try it again")
        print()
        continue
    try:
        secondProductPrice = float(input("> "))
        if(secondProductPrice <= 0):
            raise Exception
    except:
        print("Invalid number, please try it again")
        print()
    else:
        break


print()

while(True):
    print("Enter Product 3 and its price:")
    thirdProductName = input("> ")
    thirdProductName = thirdProductName.rstrip().lstrip()
    if(thirdProductName == ''):
        print("Invalid product name, try it again")
        print()
        continue
    try:
        thirdProductPrice = float(input("> "))
        if(thirdProductPrice <= 0):
            raise Exception
    except:
        print("Invalid number, please try it again")
        print()
    else:
        break

print()
print("This is what your customer will see as the menu.\n")

subtotal = 0.0
menu = {
    "1" : firstProductName,
    "2" : secondProductName,
    "3" : thirdProductName
}

""" nextStep variable to identify if user want to cancel transaction. Initially it is true """
nextStep = True
while(True):
    """ Printing menu """
    print("===========================================================\n" +
          "Please select what you want to buy from the following menu:")
    print("1. " + firstProductName + " (each $" + "{:.2f}".format(firstProductPrice) + ")\n" +
          "2. " + secondProductName + " (each $" + "{:.2f}".format(secondProductPrice) + ")\n" +
          "3. " + thirdProductName + " (each $" + "{:.2f}".format(thirdProductPrice) + ")\n" +
          "4. Done!")
    print("===========================================================")

    choice = input("> ")

    """ If entered choice is not in our menu """
    if(choice not in [str(i) for i in range(1,5)]):
        print()
        print("Sorry, " + choice + " is not a valid choice! Please select from the menu.")
        continue

    if(choice == "4"):
        if(subtotal == 0):
            print()
            print("Thank you for trying! Have a nice day")
            nextStep = False
        break

    """ We aks user to enter Integer value that is positive and greater than 0 """
    while(True):
        try:
            amount = int(input("How many " + menu[choice] + " do you want? "))
            if(amount <= 0):
                raise Exception
        except:
            print("Invalid number, try it again")
            print()
        else:
            break

    """ Counting subtotal for appropriate choice """
    if(choice == "1"):
        subtotal += amount * firstProductPrice
    elif(choice == "2"):
        subtotal += amount * secondProductPrice
    elif(choice == "3"):
        subtotal += amount * thirdProductPrice

    print("Current total: $" + "{:.2f}".format(subtotal))

""" invoice variable to identify if user chose invoice """
invoice = False

""" Ask user to enter i or c and when i then formatting Strings in appropriate format. If user entered invalid choice 
operation repeats. """
while(nextStep):
    print("Do you want to continue and see the invoice (i) or cancel the transaction (c)?")
    choice = input("> ")
    print()
    if(choice == "i"):
        print("Your invoice is here!\n")
        print("=====================")
        print("{0:<10} {1:>8}".format("Subtotal:", "${:.2f}".format(subtotal)))
        print("{0:<10} {1:>8}".format("Tax:","${:.2f}".format(subtotal * 0.13)))
        print("---------------------")
        print("{0:<10} {1:>8}".format("Total:","${:.2f}".format(subtotal * 0.13 + subtotal)))
        print("=====================")
        invoice = True
        break
    elif(choice == "c"):
        print("Thank you for trying!")
        break
    else:
        print("Sorry, " + choice + " is not a valid choice! Please select again.")

print()
""" Infinite Loop until user enters appropriate values for variables """
while(invoice):
    print("How would you like to pay? Select one from the following menu.\n(a) Cash\n(b) Prepaid Card")
    choice = input("> ")
    if(choice == "a"):
        print("Thank you for your payment. Have a nice day!")
        break
    elif(choice == "b"):
        number = input("Enter 4 digit card number: ")
        number = number.rstrip().lstrip()
        try:
            if(len(number) != 4):
                raise Exception
            number = int(number)
        except:
            print("Invalid number, please select again from the menu")
            continue


        second = number % 10
        number = int(number / 10)
        first = number % 10
        print()
        print("You have paid by xx" + str(first) + str(second) + ". Have a nice day!")
        break
    else:
        print("There is no such option in the menu, please select again")
        continue


