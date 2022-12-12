# ["+", "-", "/", "*" ]

print("1 => +"+"\n"+"2 => -"+"\n"+"3 = > *"+"\n"+"4 => /")

# try and except


try:
    Choise = int(input("What's your choise number : "))

    # if elif else statments

    if Choise == int(1):
        Num1 = int(input("Enter the num1 : "))
        Num2 = int(input("Enter the num2 : "))
        print(f"your Total is: {Num1 + Num2}")
    elif Choise == int(2):
        Num1 = int(input("Enter the num1 : "))
        Num2 = int(input("Enter the num2 : "))
        print(f"your Total is: {Num1 - Num2}")
    elif Choise == int(3):
        Num1 = int(input("Enter the num1 : "))
        Num2 = int(input("Enter the num2 : "))
        print(f"your Total is: {Num1 * Num2}")
    elif Choise == int(4):
        Num1 = int(input("Enter the num1 : "))
        Num2 = int(input("Enter the num2 : "))
        print(f"your Total is: {Num1 / Num2}")
    else:
        print("Choise those Number", "\n"+"1 => +" +
            "\n"+"2 => -"+"\n"+"3 = > *"+"\n"+"4 => /")
            
except NameError:
    print("NameError!!! Plz enter the number........")

except ValueError:
    print("ValueError!!! Plz enter the number........")