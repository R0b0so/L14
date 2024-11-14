number = int(input("Enter a whole number"))
def cube(number):
    print(number*number*number)
def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
     print("NUMBER NOT DIVISIBLE BY 3")
by_three(number)
