print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

#
choice=int(input("Enter the choice(1-4):" ))

if choice==1:
    num1=int(input("Enter the first numebr:"))
    num2=int(input("Enter the second numebr:"))
    num=num1+num2
    print("The sum is:",num)

elif choice==2:
    num1=int(input("Enter the first numebr:"))
    num2=int(input("Enter the second numebr:"))
    num=num1-num2
    print("The difference is:",num)

elif choice==3:
    num1=int(input("Enter the first numebr:"))
    num2=int(input("Enter the second numebr:"))
    num=num1*num2
    print("The product is:",num)

elif choice==4:
    num1=int(input("Enter the first numebr:"))
    num2=int(input("Enter the second numebr:"))
    num=num1/num2
    print("The quotient is:",num)

else:
    print("invalid Entry")
