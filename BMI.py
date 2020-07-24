
# a function that obtains height input
def get_height():
    height=0.0
    height=float(input("Enter your height in inches"))
    while height<=0:
        height=float(input("try again owo"))
    return height

def get_weight():
    weight=0.0
    weight=float(input("enter your weight in pounds"))
    while weight<=0:
        weight=float(input("try again owo"))
    return weight

def calcBMI(height,weight):
    BMI=0.0
    BMI=(weight*703)/(height**2)
    return BMI

def displayBMI(BMI):
    print("your BMI is",BMI)

def BMIstatus(BMI):
    if (BMI<18.5):
        print("you are underweight")

    elif (BMI<25):
        print("you are optimal weight")

    else:
        print("you are overweight")

def main():
    height = 0.0
    weight = 0.0
    BMI = 0.0
    height=get_height()
    weight=get_weight()
    BMI=calcBMI(height,weight)
    displayBMI(BMI)
    BMIstatus(BMI)
    main()

main()

    


    
