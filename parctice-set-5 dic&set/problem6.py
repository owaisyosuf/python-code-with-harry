# get user input and store in dict with keypair value

dic={}


i=0
while(i<4):
  name=input("enter your name :")
  language=input("enter you language :")
  dic.update({name:language})
  i+=1

print(type(dic))
print(dic)

