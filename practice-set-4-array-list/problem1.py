#seven fruits in the list using input method

fruits=[]

no_of_fruits=int(input("how much fruits you want to add in ur list :"))

for i in range(no_of_fruits):
  fruits_name=input("enter fruits name :")
  fruits.append(fruits_name)

print(" ".join(fruits))

