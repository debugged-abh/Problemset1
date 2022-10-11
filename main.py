# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

x = int(input("Enter balance on credit card:"))
y = float(input("Enter annual interest rate on credit card: "))
z = float(input("Enter minimum monthly payment on credit card: "))

for i in range(1,13):

    w=float(z*x)
    ip= float(y/12*x)
    pp=float(w-ip)
    rb=float(x-pp)
    x=rb
    print("Month:",i)
    print("Minimum monthly payment:",w)
    print("Remaining Balance:",rb)
    print(rb)








