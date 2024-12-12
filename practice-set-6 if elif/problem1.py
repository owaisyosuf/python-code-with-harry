# find the gretest number in 4
# def greatest_number():

#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     num3 = int(input("Enter the third number: "))
#     num4 = int(input("Enter the fourth number: "))

#     if num1 > num2 and num1 > num3 and num1 > num4:
#         print(num1)
#     elif num2 > num1 and num2 > num3 and num2 > num4:
#         print(num2)
#     elif num3 > num1 and num3 > num2 and num3 > num4:
#         print(num3)
#     else:
#         print(num4)
# greatest_number()

greatest_num=[]

for i in range(1,5):
    user_input=int(input("enter your number : "))
    greatest_num.append(user_input)
    
# print(user_input)
print(max(greatest_num))

# def large():
#     n1=int(input("enter your number : "))
#     n2=int(input("enter your number : "))
#     n3=int(input("enter your number : "))
#     n4=int(input("enter your number : "))

#     if n1>n2 and n1>n3 and n1 > n4:
#         print(n1)
#     elif n2>n1 and n1>n3 and n1 > n4:
#         print(n2)
#     elif n3>n1 and n3>n2 and n3 > n4:
#         print(n3)
#     else:
#         print(n4)
# large()    