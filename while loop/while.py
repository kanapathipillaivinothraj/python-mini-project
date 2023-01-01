

output = {
    "DOB": ""
}

# input
# is_valid => add list
# is_notValid => return input (while loop)

# while loop and while not loop


Dateofbirth = input("Enter Your date fo birth : ")


"""
output["DOB"] = str(Dateofbirth)
print(f" your value is: {Dateofbirth}")
print(output["DOB"])

"""
while Dateofbirth == "":
    print("plz enter your Your date fo birth ")
    Dateofbirth = input("Enter Your date fo birth : ")


# split("/" or ".")
while  Dateofbirth != "":
    output["DOB"] = str(Dateofbirth)
    print(f"your Your date fo birth is: {Dateofbirth}")
    print(output["DOB"])
    Dateofbirth = input("Enter Your date fo birth : ")
    

