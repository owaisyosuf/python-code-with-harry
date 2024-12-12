# find out whether a given name is present in list or not

# names=["owais", "hanif", "raheel" , "zahid"]

# user_name=input("enter your name : ")

# if user_name in names:
#   print ("welcome")
# else:
#   print("you are not into the list")


# with loop 5 time repeat
names=["owais", "hanif", "raheel" , "zahid"]
def checking():
  for i in range(5):
    user_name=input("enter your name : ")
    if user_name in names:
      print ("welcome")
    else:
      print("you are not into the list")
      i+=1

checking()