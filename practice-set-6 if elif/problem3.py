# # a spam comment is defined as a text cantaining following key word
# w1="make a lot of money"
# w2="buy now"
# w3="subtribe this"
# w4="click this"

# msg=input("enter you message here : ").lower()
# if msg == w1 or msg == w2 or msg == w3 or msg==w4:
#   print("this is scam")
# else:
#   print("thank you")

spam={
  "msg1": "make a lot of money",
  "msg2": "buy now",
  "msg3": "subscribe this",
  "msg4": "click this"
}

msg=input("enter your message here : ").lower()

if msg in spam.values():
 print("this msg is spam")
else:
  print("thank you for contacting us")

 