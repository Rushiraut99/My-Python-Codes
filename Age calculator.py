a = int(input("Please enter your Age / Birth year:"))



if a<125:

    isAge = True



elif a>1900 and a<2021:

    isAge = False



elif a>2021:

    print("You are not born yet")

    exit()



elif a<1900 and a>1800:

    print("You seems to be oldest person alive")

    exit()

else:

    print("Please enter valid data")

    exit()



if isAge == True:

    a = 2021-a



print(f"You will be 100 at {100+a}")



c = int(input("Enter the year you want your age in"))

print(f"You will be {c-a} years old in {c} ")

