# ********************************* Finding HCF *****************************

# This is the practice problem to find the HCF hy using python
def HCF(a, b):
    if a < b:
        lesser = a
    else:
        lesser = b
    for i in range(1, lesser + 1):
        if a%i==0 and b%i==0:
            HCF = i
    return HCF

if __name__ == '__main__':
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except Exception as E:
            print("Only integers are allowed...!\n")
        else:
            try:
                print(f"\nThe Highest Common Factorial (HCF) of {num1} and {num2} is {HCF(num1, num2)}")
            except Exception as E:
                print("Something went wrong...!")
            else:
                print("This is done...!\n")
            finally:
                print("** Thanks for your valuable time **\n")


