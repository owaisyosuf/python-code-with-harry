# store 8 number in a set

s=set()

# n=int(input("enter number : "))
# s.add(n)
# n=int(input("enter number : "))
# s.add(n)
# n=int(input("enter number : "))
# s.add(n)
# n=int(input("enter number : "))
# s.add(n)
# n=int(input("enter number : "))
# s.add(n)
# print(" ".join(map(str, sorted(s))))

i=0
while(i<8):
  n=int(input("enter number : "))
  s.add(n)
  i+=1
  
print(" ".join(map(str,sorted(s))))  