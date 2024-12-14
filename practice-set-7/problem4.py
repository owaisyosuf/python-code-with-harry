# find number is prime or not

# user_input=int(input("enter number : "))

# if (user_input%2)==0:
#   print("its not a prime number")
# else:
#   print("this is prime number")

n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")