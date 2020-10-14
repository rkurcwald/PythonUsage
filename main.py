import math
from decimal import *


def degrees():
    celsiusDeg=(float(input("Enter temperature in Celsius: ")))
    print('You wrote %.2f Celsius degrees to convert' %celsiusDeg)
    farenheit=(celsiusDeg* 9/5)+32
    kelvin = celsiusDeg+273.15
    print('\n\nConversion to Farenheit\n[F] %.2f'%farenheit)
    print('\nConversion to Kelvin\n[K] %.2f' % kelvin)

def calculateHypotenuse():
    catheus1 = (Decimal(input("Enter 1st catheus of triangle: ")))
    catheus2 = (Decimal(input("Enter 2nd catheus of triangle: ")))
    hypotenuse=math.sqrt((catheus1**2+catheus2**2))
    print("\nHypotenuse value: %.2f"%hypotenuse)

def toLowerCaseExample():
    text= input("Enter text: ")
    text=text.lower()
    print("Lower case: "+text)
    val= int(len(text))
    print("\nLength of entered text without changes: "+str(val))
    text=text.replace(" ","@@")
    val = int(len(text))
    print("\nAfter change: " + text)
    print("\nLength of entered text after changes: " + str(val))

def decoreText():
    text = input("Enter text: ")
    textList=list(text)
    print("List created from text:")
    print(textList)
    str="##"
    text=str.join(textList)
    text+=str
    print("Changed text: "+str+text)

def reverseName():
    text = input("Enter name: ")
    text=text[::-1]
    print(text)

def menuSwitch(val):
    switcher={
        1: degrees,
        2: calculateHypotenuse,
        3: toLowerCaseExample,
        4: decoreText,
        5: reverseName
        }
    return switcher.get(val,  "ERCODE #1: Out Of Bounds")()

def menu():
    val= int(input("Pick your program:\n1.Ex7\n2.Ex8\n3.Ex9\n4.Ex10\n5.Ex11\nWrite number: "))
    menuSwitch(val)


if __name__ == '__main__':
  # degrees()
  # calculateHypotenuse()
  # toLowerCaseExample()
  # decoreText()
  # reverseName()
    menu()
