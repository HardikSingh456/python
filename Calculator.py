print("Choose your method")
print("1.for addition")
print("2.for subtraction")
print("3.for multiplication")
print("4.for division")
a=int(input(""))

if a==1:
    num1=input('Enter first number')
    num2=input('Enter second number')
    sum=int(num1)+int(num2)
    print('Your sum is:',sum)
elif a==2:
    num1=input('Enter first number')
    num2=input('Enter second number')
    ans=int(num1)-int(num2)
    print('Your subtraction is:',ans)
elif a==3:
    num1=input('Enter first number')
    num2=input('Enter second number')
    ans=int(num1)*int(num2)
    print('Your multiplication is:',ans)
elif a==4:
    num1=input('Enter first number')
    num2=input('Enter second number')
    ans=int(num1)/int(num2)
    print('Your division is:',ans)

else:
    print('you choose wrong method')
    
